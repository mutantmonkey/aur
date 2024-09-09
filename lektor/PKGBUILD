# Maintainer: Michael Gerhaeuser <michael.gerhaeuser@gmail.com>
pkgname=lektor
_pkgname=Lektor
pkgver=3.3.12
pkgrel=1
pkgdesc="A static content management system."
arch=(any)
url="https://www.getlektor.com"
license=('BSD-3-Clause')
depends=(python python-pip
    python-requests python-babel python-flask python-watchdog
    python-click python-pyasn1 python-ndg-httpsclient
    python-mistune1 python-inifile python-exifread python-slugify
    python-filetype python-setuptools)
makedepends=(python-build python-installer python-wheel python-setuptools-scm)
options=(!emptydirs)
source=("https://files.pythonhosted.org/packages/source/L/$_pkgname/$pkgname-$pkgver.tar.gz")
sha256sums=('a856e5f94f77f8c960f6c3f21675338ac32e205bf035582063b17ea137035b03')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl

  # license
  install -Dm 644 LICENSE \
    "$pkgdir/usr/share/licenses/${pkgname}/LICENSE"
}
