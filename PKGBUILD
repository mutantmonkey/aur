# Maintainer: Alexandre Pujol <alexandre@pujol.io>
# shellcheck disable=SC2034,SC2154,SC2164

pkgbase=apparmor.d
pkgname=(apparmor.d apparmor.d.enforced)
pkgver=0.4900
pkgrel=1
pkgdesc="Full set of apparmor profiles"
arch=('x86_64' 'armv6h' 'armv7h' 'aarch64')
url="https://github.com/roddhjav/apparmor.d"
license=('GPL-2.0-only')
depends=('apparmor>=4.1.0' 'apparmor<5.0.0')
makedepends=('go' 'git' 'just')
source=("https://github.com/roddhjav/$pkgbase/releases/download/v$pkgver/$pkgbase-$pkgver.tar.gz"
        "https://github.com/roddhjav/$pkgbase/releases/download/v$pkgver/$pkgbase-$pkgver.tar.gz.asc")
sha512sums=('62b639bbadc19f63c8325ba57e306f58f17e7d976d4ebabdf101c3004e74272058b26abeb826845ae3931c0072f16c29c7727d6e5f6b73b5cfc577c153e3856e'
            'SKIP')

# The public key is found at https://pujol.io/keys
# gpg --recv-keys 06A26D531D56C42D66805049C5469996F0DF68EC
validpgpkeys=('06A26D531D56C42D66805049C5469996F0DF68EC')

build() {
  cd "$srcdir/$pkgbase-$pkgver"
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOPATH="${srcdir}"
  export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw -tags=dev"
  export DISTRIBUTION=arch
  local -A modes=(
    # Mapping of modes to just build target
    [default]=complain
    [enforced]=enforce
  )
  for mode in "${!modes[@]}"; do
    just build=".build/$mode" "${modes[$mode]}"
  done
}

_conflicts() {
  local mode="$1"
  local pattern=".$mode"
  if [[ "$mode" == "default" ]]; then
    pattern=""
  else
    echo "$pkgbase"
  fi
  for pkg in "${pkgname[@]}"; do
    if [[ "$pkg" == "${pkgbase}${pattern}" ]]; then
      continue
    fi
    echo "$pkg"
  done
}

_install() {
  local mode="${1:?}"
  cd "$srcdir/$pkgbase-$pkgver"
  just build=".build/$mode" destdir="$pkgdir" install
}

package_apparmor.d() {
  mode=default
  pkgdesc="$pkgdesc (complain mode)"
  mapfile -t conflicts < <(_conflicts $mode)
  _install $mode
}

package_apparmor.d.enforced() {
  mode=enforced
  pkgdesc="$pkgdesc (enforced mode)"
  mapfile -t conflicts < <(_conflicts $mode)
  _install $mode
}
