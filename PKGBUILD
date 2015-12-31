pkgname=('heka')
srcname='heka'
pkgdesc='Data collection and processing made easy'
pkgver='0.10.0'
pkgrel='1'
arch=('i686' 'x86_64')
url="https://github.com/mozilla-services/${srcname}"
license=('MPL2')

depends=('geoip')
makedepends=(
    'cmake'
    'gcc'
    'git'
    'go'
    'make'
    'mercurial'
    'patch'
)
optdepends=('geoip-citydata: GeoIpDecoder')
provides=("${pkgname[0]%-git}")
conflicts=("${pkgname[0]%-git}")

source=(
    "${srcname}::git+https://github.com/mozilla-services/${srcname}.git#tag=v${pkgver}"
    "cmake.patch"
)
sha512sums=(
    'SKIP'
    'SKIP'
)

prepare() {
    cd "${srcdir}/${srcname}"

    git apply "${srcdir}/cmake.patch"
}

build() {
    cd "${srcdir}/${srcname}"

    BUILD_DIR="${PWD}/build"
    export GOPATH="${BUILD_DIR}/heka"
    export GOBIN="${GOPATH}/bin"
    export PATH="${GOBIN}:${PATH}"
    export LD_LIBRARY_PATH="${BUILD_DIR}/heka/lib"
    export CTEST_OUTPUT_ON_FAILURE=1

    mkdir --parents "${BUILD_DIR}"
    cd "${BUILD_DIR}"
    cmake \
        -DCMAKE_INSTALL_PREFIX='/usr' \
        -DCMAKE_BUILD_TYPE='release' \
        -DHEKA_PATH='/usr/share/heka' \
        ..
    make
}

package() {
    cd "${srcdir}/${srcname}"

    BUILD_DIR="${PWD}/build"
    export GOPATH="${BUILD_DIR}/heka"
    export GOBIN="${GOPATH}/bin"
    export PATH="${GOBIN}:${PATH}"

    cd "${BUILD_DIR}"
    make DESTDIR="${pkgdir}" install

    install -D --directory "${pkgdir}/var/cache/hekad"
    install -D --directory "${pkgdir}/etc/heka/conf.d"
}
