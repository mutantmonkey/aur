# Maintainer: Дамјан Георгиевски <gdamjan@gmail.com>
# Maintainer: zer0def <zer0def@github>
pkgname=cloud-hypervisor
pkgver=49.0
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
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/cloud-hypervisor/cloud-hypervisor/archive/v${pkgver}.tar.gz")

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

sha512sums=('82ed95bc05f8c4f38ddc4485c00226c7929c81fb4cb391961d7a16a74a29e3cc072077a9991ce55d7d54c7f14cb64ce06865005da3dc916fb8c3e2cb5318989a')
b2sums=('69775d964911a4d97488d85e209ae681d043d2b197ddb31880045c359ce2e6029066d44583774db7aaa57243bc3011a8cdd0071ed70288cd310a88100f47203f')
