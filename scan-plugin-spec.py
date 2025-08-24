"""Parse plugin.spec and /etc/hp/hplip.conf to generate a list of files to be installed in this pattern:
src,dst,link
"""

from os import environ
from re import match
from sys import stderr
from logging import getLogger
from logging import StreamHandler
from pathlib import Path
from configparser import ConfigParser


LOGGER = getLogger(__name__)
HPLIP_CONF = Path("/etc/hp/hplip.conf")
PLUGIN_SPEC = Path("plugin.spec")
# They need libjpeg.so.9, which is not packaged by archlinux.
BLACKLIST = "(hp2000S1|hpgt2500)_plugin_\\d+"
LOGGER.setLevel("INFO")
LOGGER.addHandler(StreamHandler(stderr))
OUTPUT_SEP = ","

match environ["CARCH"]:
    case "i686":
        arch = "x86_32"
    case "armv6h" | "armv7h":
        arch = "arm32"
    case "aarch64":
        arch = "arm64"
    case CARCH:
        arch = CARCH


hplip = ConfigParser()
hplip.read_string(HPLIP_CONF.read_text())
hplip_conf_dirs_home = hplip["dirs"]["home"]


def _eval(i: str, product: str) -> Path:
    return Path(
        i.replace("$ARCH", arch)
        .replace("$PRODUCT", product)
        .replace("$HOMEDIR", hplip_conf_dirs_home)
    )


def _output(items: list[Path]):
    print(OUTPUT_SEP.join(str(p) for p in items))


plugin_spec = ConfigParser()
plugin_spec.read_string(PLUGIN_SPEC.read_text())
_output([Path(PLUGIN_SPEC.name), Path(hplip_conf_dirs_home) / PLUGIN_SPEC.name])
for product in plugin_spec.options("products"):
    for item in plugin_spec["products"][product].split(","):
        if match(BLACKLIST, item):
            LOGGER.error("Item %s is in the blacklist, skipping...", item)
        else:
            LOGGER.info("Installing item %s for product %s...", item, product)
            src = _eval(plugin_spec[item]["src"], product)
            trg = _eval(plugin_spec[item]["trg"], product)
            link = plugin_spec[item].get("link")
            link = _eval(link, product) if link else None
            output_src = Path(src.name)
            if output_src.exists():
                output_items = [output_src, trg]
                if link:
                    output_items.append(link)
                _output(output_items)
            else:
                LOGGER.error("%s is not found, skipping...", output_src)
