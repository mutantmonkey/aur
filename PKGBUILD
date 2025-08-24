# Maintainer: Carl Smedstad <carsme@archlinux.org>
# Contributor: andmars <andreas.marschall @ unitybox.de>
# Contributor: PyroPeter <googlemail.com @ abi1789>
# Contributor: Ivan Shapovalov <intelfx@intelfx.name>

pkgname=hplip-plugin
pkgver=3.25.6
pkgrel=1
pkgdesc="Binary plugin for HPs hplip printer driver library"
arch=(x86_64 aarch64 armv6h armv7h i686)
url="https://developers.hp.com/hp-linux-imaging-and-printing/binary_plugin.html"
license=(LicenseRef-HPLIP-LICENSE)
backup=(var/lib/hp/hplip.state)
# https://developers.hp.com/hp-linux-imaging-and-printing/plugins
_date=2025-08
source=("$pkgname-$pkgver.run::https://developers.hp.com/sites/default/files/$_date/hplip-$pkgver-plugin.run"
        "$pkgname-$pkgver.run.asc::https://developers.hp.com/sites/default/files/$_date/hplip-$pkgver-plugin.run.asc")
sha256sums=('0cd770036532a2d706c0f449ee1e3ef9b4de7b6cea5aaf2e76fe2da3f97f6ffc'
            'SKIP')
validpgpkeys=('82FFA7C6AA7411D934BDE173AC69536A2CF3A243') # HPLIP (HP Linux Imaging and Printing) <hplip@hp.com>

# Thank you @Toolybird for the solution
_user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
DLAGENTS=("https::/usr/bin/curl --user-agent ${_user_agent// /\\ } -qgb '' -fLC - --retry 3 --retry-delay 3 -o %o %u")

prepare() {
  sh "$pkgname-$pkgver.run" --target "$srcdir/$pkgname-$pkgver" --noexec
}

package() {
  # While hplip-plugin requires the version of hplip to match exactly,
  # specifying such a requirement breaks the ability to upgrade hplip.
  depends=(gcc-libs glibc sane libusb-compat "hplip>=$pkgver")

  cd "$srcdir/$pkgname-$pkgver"

  case $CARCH in
  "i686")
    _arch='x86_32'
    ;;
  "x86_64")
    _arch='x86_64'
    ;;
  "armv6h" | "armv7h")
    _arch='arm32'
    ;;
  "aarch64")
    _arch='arm64'
    ;;
  esac

  install -Dm644 -t "$pkgdir/usr/share/hplip" plugin.spec
  install -Dm644 -t "$pkgdir/usr/share/hplip/data/firmware" hp_laserjet_*.fw.gz
  install -Dm755 -t "$pkgdir/usr/share/hplip/fax/plugins" fax_marvell-"$_arch".so
  install -Dm755 -t "$pkgdir/usr/share/hplip/prnt/plugins" hbpl1-"$_arch".so
  install -Dm755 -t "$pkgdir/usr/share/hplip/prnt/plugins" lj-"$_arch".so
  install -Dm755 -t "$pkgdir/usr/share/hplip/scan/plugins" bb_*-"$_arch".so

  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" license.txt

  # Create hplip.state used by hplip-tools
  cat << EOF > hplip.state
[plugin]
installed = 1
eula = 1
version = $pkgver
EOF
  install -Dm644 -t "$pkgdir/var/lib/hp" hplip.state

  # Create symlinks
  find "$pkgdir/usr/share/hplip" -type f -name "*.so" | while read -r f; do
    lib_dir="${f%/*}"
    lib_name="${f##*/}"
    ln -vsf "$lib_name" "$lib_dir/${lib_name%%-*}.so"
  done
}

# Note: to check the install, perform: hp-diagnose_plugin
