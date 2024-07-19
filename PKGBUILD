# Maintainer: Atte Lautanala <atte@lautana.la>
# Contributor: Trevor Mosey <trevor dot mosey at gmail dot com>

pkgname=flyctl
pkgver="0.2.92"
pkgrel="1"
pkgdesc="Command line tools for fly.io services"
arch=("x86_64")
url="https://github.com/superfly/flyctl"
license=("Apache-2.0")
makedepends=(go)
source=("$url/archive/v$pkgver/$pkgname-$pkgver.tar.gz")
b2sums=('3d0e365d4c82fc1fafef9a134f18e5d48ffc9169c015dd204727775c16c729d6f4a9481c5bd91b8bcd2d8e087159c9495cb3ef08767df189b8a020b203dc44c4')

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
