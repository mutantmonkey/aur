# Maintainer: graysky <graysky AT archlinux DOT us>

pkgname='clean-chroot-manager'
pkgver=2.72
pkgrel=1
pkgdesc='Wrapper scripts for managing clean chroots (64-bit and 32-bit).'
arch=('any')
url='https://github.com/graysky2/clean-chroot-manager'
license=('MIT')
depends=('devtools')
conflicts=('clean_chroot_manager')
replaces=('clean_chroot_manager')
source=("http://repo-ck.com/source/$pkgname/$pkgname-$pkgver.tar.xz")
sha256sums=('8de0e5ff04e641034e25234fde53efd80a602a1cdb1f0ba05b9b98acc267c5d6')
install=ccm.install

build() {
  cd "$pkgname-$pkgver"
  make
}

package() {
  cd "$pkgname-$pkgver"
  make DESTDIR="$pkgdir" install
  install -Dm644 MIT "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
