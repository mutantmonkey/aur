pkgname=piper-tts
_pkgname=piper1-gpl
pkgver=1.4.1
pkgrel=1
pkgdesc="Fast and local neural text-to-speech engine"
arch=('x86_64')
url="https://github.com/OHF-Voice/piper1-gpl"
license=('GPL-3.0-or-later')
provides=('piper-tts')
conflicts=('piper-tts' 'piper')
depends=(glibc python-numpy python-onnxruntime)
optdepends=(
	'python-flask: http server'
	'python-pytorch: train'
)
makedepends=(git python-setuptools python-build python-installer python-wheel python-scikit-build cmake ninja)
source=("git+https://github.com/OHF-Voice/piper1-gpl.git#tag=v$pkgver")
sha256sums=('f98407f9f95b980e2087a0c1b9d7056bf0fba5978ed3a0cfa1720b10e6eb59eb')

prepare() {
	cd ${_pkgname}
	sed -i 's/"cmake", "ninja"//' pyproject.toml
}

build() {
  cd ${_pkgname}
  python -m build --wheel --no-isolation
}

package() {
  cd ${_pkgname}
  python -m installer --destdir="$pkgdir" dist/*.whl

  # avoid conflict with GTK application 'piper'
  mv "$pkgdir"/usr/bin/piper "$pkgdir"/usr/bin/piper-tts

  rm "$pkgdir"/usr/COPYING
}

