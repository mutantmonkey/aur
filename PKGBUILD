# Maintainer: Hao Long <aur@esd.cc>

pkgname=cloudflared-bin
pkgver=2018.6.2
pkgrel=1
pkgdesc="An Argo Tunnel client which proxies any local webserver through the Cloudflare network"
arch=("x86_64" "arm")
url="https://developers.cloudflare.com/argo-tunnel/"
license=("custom")
provides=("cloudflared")
conflicts=("cloudflared")
source=("https://raw.githubusercontent.com/cloudflare/cloudflared/master/LICENSE"
        "cloudflared.yml"
        "cloudflared@.service")
source_x86_64=("https://bin.equinox.io/c/VdrWdbjqyF/cloudflared-stable-linux-amd64.tgz")
source_arm=("https://bin.equinox.io/c/VdrWdbjqyF/cloudflared-stable-linux-arm.tgz")
sha256sums=('6a486a0f6c00e87cce1caf0aa8db45ea9fefd0bf91d9be6fc44460160dc0dbda'
            '4e06eb54143d872f73707ed2bba2ba2198649d3066df741bd0cfda5d1a5f334d'
            'a2d6beef87b531ec43837ce1c2ebd7411058466a11bd6a899a8659582b25e3c2')
sha256sums_x86_64=('13f34fbfef05104496c913807b21c3c8b09b519537acbaa3a8d70ade5dcf97b2')
sha256sums_arm=('829b42e05df6d0b47b0180b84247a3ab43bdfaf443aa027306382fda053a0592')

package() {
    # Install License
    install -Dm644 LICENSE ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE

    # Install Binary
    install -Dm755 cloudflared ${pkgdir}/usr/bin/cloudflared

    # Configuration File
    install -Dm644 cloudflared.yml ${pkgdir}/etc/cloudflared/cloudflared.yml.example
    install -Dm644 cloudflared@.service ${pkgdir}/usr/lib/systemd/system/cloudflared@.service
}

# vim: ts=2 sw=2 et:
