# Maintainer: Atte Lautanala <atte@lautana.la>
# Contributor: Trevor Mosey <trevor dot mosey at gmail dot com>

pkgname=flyctl
pkgver="0.2.67"
pkgrel="1"
pkgdesc="Command line tools for fly.io services"
arch=("x86_64")
url="https://github.com/superfly/flyctl"
license=("Apache")
makedepends=(go)
source=("$url/archive/v$pkgver/$pkgname-$pkgver.tar.gz")
b2sums=('89fa9e1d41e5a3dc5c815e149d36598a50427831fc18e1f6e48e0347bb2abb2e3fe98302b4c25e1d02341ce7959ffb8acdf2d71ffd3775063aec50036d18d13b')

build() {
  cd "$pkgname-$pkgver"
  export CGO_LDFLAGS="${LDFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
  make VERSION=$pkgver build
}

check() {
  make -C "$pkgname-$pkgver" test
}

package() {
  cd "$pkgname-$pkgver"
  mkdir -p "$pkgdir/usr/bin"
  ln -s "/usr/bin/flyctl" "$pkgdir/usr/bin/fly"
  install -m755 "bin/flyctl" "$pkgdir/usr/bin"
}
