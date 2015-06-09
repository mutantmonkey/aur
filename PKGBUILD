# Maintainer: mutantmonkey <aur@mutantmonkey.in>
pkgname=tor-control-port-proxy
pkgver=0.3
pkgrel=2
pkgdesc="Whitelisting Tor control port proxy written in Python"
arch=('any')
url="https://github.com/mutantmonkey/tor-control-port-proxy"
license=('WTFPL')
depends=('python' 'stem')
options=(!emptydirs)
source=('git+https://github.com/mutantmonkey/tor-control-port-proxy.git')
sha256sums=('SKIP')

package() {
  cd $srcdir/tor-control-port-proxy
  install -Dm755 tor-control-port-proxy \
    "${pkgdir}/usr/bin/tor-control-port-proxy"
  install -Dm644 tor-control-port-proxy.service \
    "${pkgdir}/usr/lib/systemd/system/tor-control-port-proxy.service"
  install -Dm644 COPYING \
    "${pkgdir}/usr/share/licenses/${pkgname}/COPYING"
}

# vim:set ts=2 sw=2 et:
