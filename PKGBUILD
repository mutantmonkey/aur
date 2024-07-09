# Maintainer: Atte Lautanala <atte@lautana.la>
# Contributor: Trevor Mosey <trevor dot mosey at gmail dot com>

pkgname=flyctl
pkgver="0.2.84"
pkgrel="1"
pkgdesc="Command line tools for fly.io services"
arch=("x86_64")
url="https://github.com/superfly/flyctl"
license=("Apache-2.0")
makedepends=(go)
source=("$url/archive/v$pkgver/$pkgname-$pkgver.tar.gz")
b2sums=('b0212647360eb5e880e974f3ebdb02ed37e85d48041b651b27917d04ac87adaad5b65773393d7f94720f3a4252f02c27603f35640213a5091494bb7e57025bed')

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
