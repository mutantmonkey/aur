# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
# Contributor: Michael Riegert <michael at eowyn net>
# Contributor: Felix Golatofski <contact@xdfr.de>
# Contributor: Sibren Vasse <arch@sibrenvasse.nl>
# Contributor: Daniel M. Capella <polyzen@archlinux.info>
# Contributor: Morten Linderud <morten@linderud.pw>

pkgname=python-pychromecast
_name=${pkgname#python-}
pkgver=14.0.3
pkgrel=1
pkgdesc="Library for Python 3 to communicate with the Google Chromecast"
arch=('any')
url="https://github.com/home-assistant-libs/pychromecast"
license=('MIT')
depends=(
  'python-casttube'
  'python-protobuf'
  'python-zeroconf'
)
makedepends=(
  'python-build'
  'python-installer'
  'python-setuptools'
  'python-wheel'
)
source=("$_name-$pkgver.tar.gz::$url/archive/refs/tags/$pkgver.tar.gz")
sha256sums=('e94529102d5d631c85eddd2aa0c1a9b9cd8d5cf773a98ec8804b6e03eaa6071a')

prepare() {
  cd "$_name-$pkgver"

  # relax requirements
  sed -i 's/~=/>=/g' pyproject.toml
}

build() {
  cd "$_name-$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "$_name-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl

  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
}
