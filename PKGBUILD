# Maintainer: Mort Yao <soi@mort.ninja>
# Contributor: Serge Zirukin <ftrvxmtrx@gmail.com>
# Contributor: Sergei Lebedev <superbobry@gmail.com>
# Contributor: Guillem Rieu <guillemr@gmx.net>
# Contributor: Sergey Plaksin <serp256@gmail.com>
# Contributor: Nicolas Pouillard <nicolas.pouillard@gmail.com>

pkgname=ocaml-menhir
pkgver=20141215
pkgrel=1
pkgdesc="Menhir is a LR(1) parser generator for the OCaml."
arch=("i686" "x86_64")
url="http://cristal.inria.fr/~fpottier/menhir/"
license=('GPL' 'QPL')
depends=('ocaml>=4.02')
makedepends=('ocaml-findlib')
options=(!strip !makeflags)
source=("http://cristal.inria.fr/~fpottier/menhir/menhir-$pkgver.tar.gz")
md5sums=('5e1d1ac11364adcfe445cd6e3cbf7fc3')

build() {
  cd "$srcdir/${pkgname/ocaml-/}-$pkgver"
  make PREFIX="/usr" all
}

package() {
  cd "$srcdir/${pkgname/ocaml-/}-$pkgver"
  export OCAMLFIND_DESTDIR="$pkgdir$(ocamlfind printconf destdir)"
  install -dm 755 "$OCAMLFIND_DESTDIR"
  make PREFIX="$pkgdir/usr" install
}
