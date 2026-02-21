# Maintainer: Дамјан Георгиевски <gdamjan@gmail.com>
# Maintainer: zer0def <zer0def@github>
pkgname=cloud-hypervisor
pkgver=51.0
pkgrel=1
pkgdesc="A Virtual Machine Monitor for modern Cloud workloads"
url="https://github.com/cloud-hypervisor/cloud-hypervisor"
arch=('x86_64' 'aarch64')
license=('Apache-2.0')
depends=(
    gcc-libs
    glibc
)
optdepends=(
  'virtiofsd: rust implementation of virtiofsd'
)
makedepends=('rust')
options=('!lto' '!debug')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/cloud-hypervisor/cloud-hypervisor/archive/v${pkgver}.tar.gz")

prepare() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    cargo fetch --locked
}

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  cargo build --release --locked --features fw_cfg
}

package() {
  install -Dm755 -t "${pkgdir}/usr/bin" \
    "${srcdir}/${pkgname}-${pkgver}/target/release/ch-remote" \
    "${srcdir}/${pkgname}-${pkgver}/target/release/cloud-hypervisor"
  #install -Dm755 -t "${pkgdir}/usr/lib/cloud-hypervisor" \
  #  "${srcdir}/${pkgname}-${pkgver}/target/release/vhost_user_blk" \
  #  "${srcdir}/${pkgname}-${pkgver}/target/release/vhost_user_fs" \
  #  "${srcdir}/${pkgname}-${pkgver}/target/release/vhost_user_net"
}

sha512sums=('8368a5e9fe143b36b62d04e812bac11abd1f3bb2c4c27e0b7971a2174ec636ea5186e180249ca081e9e92a7bce8dba709ffb762f1fb5fb1b5c54405e8c6b0ef7')
b2sums=('8a901f64be192d9507a2a007fca182fddfe90a921d236d26ac73b2c4fac51891ee8043885d7ab0eb6e5a44b4be6e59a1883b932ca55e5e86b9a99075a60d989c')
