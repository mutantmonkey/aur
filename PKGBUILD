# Contributor: alphazo <alphazo@gmail.com>
# Original PKGBUILD generated by pip2arch

pkgname=ntfy
pkgver=2.4.4
pkgrel=1
pkgdesc="A utility for sending push notifications to different backends (Pushover, Pushbullet, XMPP and various desktop notification systems)"
url="https://github.com/dschep/ntfy"
depends=('python' 'python-requests' 'python-yaml' 'python-appdirs' 'xorg-xprop' 'python-ruamel-yaml')
makedepends=('python3')
optdepends=('python-dbus')
license=('GPLv3')
arch=('any')
source=(https://github.com/dschep/ntfy/archive/v$pkgver.tar.gz)
md5sums=('7dd5055618202cccb9f7e066ec8125ee')

build() {
    cd "$srcdir/${pkgname}-${pkgver}"
    python setup.py build
}

package() {
    cd "$srcdir/${pkgname}-${pkgver}"
    python setup.py install --root="$pkgdir" --optimize=1 
}
