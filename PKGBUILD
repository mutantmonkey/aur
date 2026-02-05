pkgname=piper-tts
_pkgname=piper1-gpl
pkgver=1.4.1
pkgrel=2
pkgdesc="Fast and local neural text-to-speech engine"
arch=('x86_64')
url="https://github.com/OHF-Voice/piper1-gpl"
license=('GPL-3.0-or-later')
provides=('piper-tts')
conflicts=('piper-tts' 'piper')
depends=(glibc python-numpy python-onnxruntime python-pathvalidate)
optdepends=(
	'python-flask: http server'
	'python-onnx: patch voice with alignment'
	'python-pytorch: train'
)
makedepends=(git python-setuptools python-build python-installer python-wheel python-scikit-build cmake ninja)
source=("git+https://github.com/OHF-Voice/piper1-gpl.git#tag=v$pkgver")
sha256sums=('df1aa63504633df54e625c2a83997bba83d4c3d36504e431fb47964bc2aa4d0e')

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

