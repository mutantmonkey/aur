pkgname=piper-tts
_pkgname=piper1-gpl
pkgver=1.3.0
pkgrel=1
pkgdesc="Fast and local neural text-to-speech engine"
arch=('x86_64')
url="https://github.com/OHF-Voice/piper1-gpl"
license=('GPL-3.0-or-later')
provides=('piper-tts')
conflicts=('piper-tts')
depends=(glibc python-numpy python-onnxruntime)
optdepends=(
	'python-flask: http server'
	'python-pytorch: train'
)
makedepends=(git python-setuptools python-build python-installer python-wheel python-scikit-build cmake ninja)
source=("git+https://github.com/OHF-Voice/piper1-gpl.git#tag=v$pkgver")
sha256sums=('4283f56d438c74cc5c790917264e557af6fd2acfa1ff4942f9628c7b78733314')

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

