# Maintainer: AdmiringWorm <kim.nordmo@gmail.com>
# Contributor: nirnakinho <aur at dominikbodi dot de>

pkgname=dnscontrol
pkgver=4.13.0
pkgrel=1
pkgdesc="Synchronize your DNS to multiple providers from a simple DSL"
arch=('x86_64' 'armv7h' 'aarch64')
url="https://stackexchange.github.io/${pkgname}/"
license=('MIT')
depends=('glibc')
makedepends=('go')
provides=("${pkgname}=${pkgver}")
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/StackExchange/${pkgname}/archive/v${pkgver}.tar.gz")
b2sums=('61c23759bf3103b1d37ff19cae2db338f4c73f9981842f08d44c357d2fab970bbe1b592ec0a1b0877de51096883b3d66d43108f869e057768c4ec78da7595b08')

prepare(){
  cd "$pkgname-$pkgver"
  mkdir -p build/
#  mkdir -p gopath/src/github.com/StackExchange
#  ln -rTsf $pkgname-$pkgver gopath/src/github.com/StackExchange/dnscontrol
}

build() {
  cd "$pkgname-$pkgver"
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
  go build -o build
}

package() {
  cd "$pkgname-$pkgver"
  install -Dm755 build/${pkgname} "${pkgdir}/usr/bin/${pkgname}"
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
