# Maintainer: Guillaume Horel <guillaume.horel@gmail.com>
pkgname=python-fpdf2
_name=${pkgname#python-}
pkgver=2.8.2
pkgrel=1
pkgdesc='Simple PDF generation for Python'
arch=(any)
url='https://pyfpdf.github.io/fpdf2/'
license=(LGPL-3.0-only)
conflicts=('python-fpdf')
depends=(python python-pillow python-defusedxml python-fonttools)
optdepends=(
    'python-endesive: signing support'
    'python-uharfbuzz: text shaping support'
    'python-cryptography: encryption support'
)
makedepends=(python-build python-installer python-setuptools python-wheel)
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
sha256sums=('3a2c6699c39b23b786fc6ad9fc3de5432e59f6b6383bb9ab4ce1f994a5f3e762')

build() {
    cd "$_name-$pkgver"
    python -m build --wheel --no-isolation
}

package() {
	cd "$_name-$pkgver"
	python -m installer --destdir="$pkgdir" dist/*.whl
}
