# Maintainer: Jakob Gahde <j5lx@fmail.co.uk>

pkgname=ocaml-seq
pkgver=base
pkgrel=1
pkgdesc="Dummy backward-compatibility package for iterators"
arch=('any')
url="https://github.com/ocaml/opam-repository"
license=('unknown')
depends=('ocaml')
makedepends=('git' 'ocaml-findlib' 'opam')
source=("git+https://github.com/ocaml/opam-repository.git")
sha512sums=('SKIP')

package() {
  cd "${srcdir}/opam-repository/packages/seq/seq.${pkgver}/files"

  opam-installer --libdir="${pkgdir}$(ocamlfind -printconf destdir)"
}
