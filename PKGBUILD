# Maintainer: fossdd <fossdd@pwned.life>
pkgname=lyrebird-proxy
pkgver=0.2.0
pkgrel=1
pkgdesc="pluggable transport proxy for Tor, implementing obfs4"
url="https://gitlab.torproject.org/tpo/anti-censorship/pluggable-transports/lyrebird"
license=('BSD-3-Clause')
arch=('x86_64' 'aarch64' 'armv7h')
depends=('glibc')
makedepends=('go')
source=("$pkgname-$pkgver.tar.bz2::https://gitlab.torproject.org/tpo/anti-censorship/pluggable-transports/lyrebird/-/archive/lyrebird-$pkgver/lyrebird-lyrebird-$pkgver.tar.bz2"
        lyrebird-proxy.service)
sha256sums=('d079566692bd7ed8e7c2421e3ad5539ade7effabc69b286ecd4a25a076546045'
            '63b16cb083656a661d1cbe0198f2f3bb0fabc6bb09ad4501d1c470c7b3f832ab')
b2sums=('90b129e198f2a5d70715734f0b98e67a83b92f88de278c53da2eda53b34a788600cbb92a34e6ecee704fc18060399091fc743abca0bd8f564ccccc7700c59a51'
        'a5e898ccf657f541ed8c406c4f1970c5b8bd7389725899aced3f9d2b0f134d3f4e804d065f9018789a1403f209d5ad04e8af1dc4ffe719e844fabee53d1a7fe3')

build() {
  cd "$srcdir/lyrebird-lyrebird-$pkgver"

  export CGO_CPPFLAGS="$CPPFLAGS"
  export CGO_CFLAGS="$CFLAGS"
  export CGO_CXXFLAGS="$CXXFLAGS"
  export CGO_LDFLAGS="$LDFLAGS"
  export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"

  go build -v -o lyrebird ./cmd/lyrebird
}

package() {
  cd "$srcdir/$pkgname-$pkgver"

  install -Dm0755 lyrepird "$pkgdir/usr/bin/lyrebird"
  install -Dm0644 "$srcdir/lyrebird-proxy.service" "$pkgdir/usr/lib/systemd/system/lyrebird-proxy.service"

  install -Dm0644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
