# Maintainer: mutantmonkey <aur@mutantmonkey.mx>
# Contributor: Boudhayan Gupta <bgupta@kde.org>

_npmname=netlify-cli
_npmver=3.35.1

pkgname=netlify
pkgver=${_npmver}
pkgrel=1
pkgdesc="Create, deploy, and delete new sites hosted on Netlify straight from your terminal"

arch=(any)
url="https://www.netlify.com/docs/cli/"
depends=('nodejs')
makedepends=('npm')
license=('MIT')
options=('!strip')
source=("https://registry.npmjs.org/${_npmname}/-/${_npmname}-${_npmver}.tgz")
noextract=("${_npmname}-${_npmver}.tgz")
sha256sums=('baff0002e28b40a6a3aaae691cb6a9147f044620cef426bf39d52e16eccfb4f7')

package() {
    cd ${srcdir}
    local _npmdir="${pkgdir}/usr/lib/node_modules/"
    mkdir -p ${_npmdir}
    cd ${_npmdir}
    npm install -g --prefix "${pkgdir}/usr" ${_npmname}@${_npmver}

    # Fix file ownership and permissions
    chown -R 0:0 "${pkgdir}/usr"
    find "${pkgdir}/usr" -perm -o+w,g+w -exec chmod o-w,g-w {} +
}
