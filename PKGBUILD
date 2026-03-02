# Maintainer: mh4ckwascut <mh4ckt3mh4ckt1c4s@archlinux.org>
# Contributor: Fredrick Brennan <copypaste@kittens.ph>
# Contributor: Markus Schaaf <markuschaaf@gmail.com>
# Contributor: Stephan Eisvogel <eisvogel at embinet dot de>
pkgname=python-xmp-toolkit
_name=python_xmp_toolkit
pkgver=2.1.0
pkgrel=1
pkgdesc='A library for working with XMP metadata'
arch=(any)
url='http://python-xmp-toolkit.readthedocs.org/'
license=(LicenseRef-custom)
depends=('python>=3.7'
         'exempi>=2.2.0'
         'python-pytz')
makedepends=(python-build python-installer python-wheel python-flit-core)
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha256sums=('ca0aa2c60d418dd2558767db59953ab5954fb5b87dc0b50cecd60566b0b4e2da')
 
build() {
        cd "${_name}-${pkgver}"
	python -m build --wheel --no-isolation
}
 
package() {
        cd "${_name}-${pkgver}"
	python -m installer --destdir="$pkgdir" dist/*.whl
	install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" LICENSE
}
