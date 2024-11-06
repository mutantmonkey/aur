# Maintainer: Fredrick Brennan <copypaste@kittens.ph>
# Contributor: Markus Schaaf <markuschaaf@gmail.com>
# Contributor: Stephan Eisvogel <eisvogel at embinet dot de>
pkgname=python-xmp-toolkit
pkgver=2.0.2
pkgrel=1
pkgdesc='A library for working with XMP metadata'
arch=(any)
url='http://python-xmp-toolkit.readthedocs.org/'
license=(custom)
depends=('python>=3.5'
         'exempi>=2.2.0'
         'python-pytz')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/p/python-xmp-toolkit/python-xmp-toolkit-${pkgver}.tar.gz")
b2sums=('123b07624999bf0bde4872aed319681e3ec020ad45796ed07d44aa953cf79537bfc0489634bd2ff767f17f36d1e6ddb5852322a07e0a8f911f90c82be38054f2')
 
build() {
        cd "$srcdir/python-xmp-toolkit-${pkgver}"
        /usr/bin/python setup.py build
}
 
package() {
        cd "$srcdir/python-xmp-toolkit-${pkgver}"
        install -d "$pkgdir/usr/share/licenses/$pkgname"
        install -t "$pkgdir/usr/share/licenses/$pkgname" LICENSE
        /usr/bin/python setup.py install --root="$pkgdir" --prefix=/usr --optimize=1
}
