# Generated by gem2arch (https://github.com/anatol/gem2arch)
# Maintainer: mutantmonkey <aur@mutantmonkey.in>

_gemname=base32
pkgname=ruby-$_gemname
pkgver=0.3.2
pkgrel=1
pkgdesc='Ruby extension for base32 encoding and decoding'
arch=(any)
url='https://github.com/stesla/base32'
license=('MIT')
depends=(ruby)
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha256sums=('532e9b19c5dd1fce281df67fc93a803ebd5d26426a93f6dda6612769bc46fe2c')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
