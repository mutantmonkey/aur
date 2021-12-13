# Maintainer: Taiko2k <captain dot gxj at gmail dot com>

pkgname=python-isounidecode
_name=${pkgname#python-}
pkgver=0.3
pkgrel=3
pkgdesc="Conversion and transliteration of unicode into ascii or iso-8859-1"
arch=('any')
url="https://github.com/redvasily/isounidecode"
license=('BSD 3-Clause')
depends=('python')
makedepends=('python-setuptools')
source=("https://pypi.org/packages/source/${_name:0:1}/$_name/$_name-$pkgver.tar.gz")
sha256sums=('4db0a962c6341826c9a69acaabc2f923a5b124d53a335be892ef29173bc31c5b')
 
build() {
    cd "$_name-$pkgver"
    python setup.py build
}
 
package() {
    cd "$_name-$pkgver"
    python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}

