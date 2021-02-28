# Maintainer: robertfoster
# Contributor: Jakob Gahde <j5lx@fmail.co.uk>

pkgname=ocaml-xmlplaylist
pkgver=0.1.5
pkgrel=1
pkgdesc="OCaml module to parse various RSS playlist formats"
arch=('i686' 'x86_64')
url="https://github.com/savonet/ocaml-xmlplaylist"
license=('LGPL2.1')
depends=('ocaml' 'ocaml-xmlm')
makedepends=('ocaml-findlib' 'dune')
options=('!strip')
source=("${url}/archive/v${pkgver}.tar.gz")

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  dune build
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  DESTDIR="${pkgdir}" dune install --prefix "/usr" --libdir "lib/ocaml"

  install -dm755 "${pkgdir}/usr/share/"
  mv "${pkgdir}/usr/doc" "${pkgdir}/usr/share/"
}

sha256sums=('07c26aefbb36a0fd6295e40b2f41a900442ec24614a834e84cb8163c4bd54d46')
