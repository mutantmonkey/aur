# Maintainer: Michael Gerhaeuser <michael.gerhaeuser@gmail.com>

pkgname=python-inifile
_pkgname=python-inifile
pkgver=0.4
pkgrel=4
pkgdesc="Ini file library for Python."
arch=(any)
url="https://github.com/mitsuhiko/python-inifile"
license=('BSD')
depends=(python)
makedepends=(python-setuptools)
options=(!emptydirs)
source=("https://github.com/mitsuhiko/$_pkgname/archive/$pkgver.tar.gz")
sha256sums=('4fc1ce989f35b4233731bb4bdf80db59e1e3396de3ef15677dbfe2097569db64')

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1

  # license
  install -Dm 644 LICENSE \
    "$pkgdir/usr/share/licenses/${pkgname}/LICENSE"
}
