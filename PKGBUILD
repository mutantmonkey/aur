# Maintainer: Atte Lautanala <atte@lautana.la>
# Contributor: Trevor Mosey <trevor dot mosey at gmail dot com>

pkgname=flyctl
pkgver="0.2.89"
pkgrel="1"
pkgdesc="Command line tools for fly.io services"
arch=("x86_64")
url="https://github.com/superfly/flyctl"
license=("Apache-2.0")
makedepends=(go)
source=("$url/archive/v$pkgver/$pkgname-$pkgver.tar.gz")
b2sums=('cdc9a49a7dcec8c6588b538a580a85f16074746f2c3a702bed6272ffcd6d38c071d4867e5bbee96a0d76630f1b7ce0855153e99bf1b7326cd230528799a6bc03')

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
