# Maintainer: Дамјан Георгиевски <gdamjan@gmail.com>
# Maintainer: zer0def <zer0def@github>
pkgname=cloud-hypervisor
pkgver=48.0
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
  cargo build --release --locked
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

sha512sums=('3228cd974de9d5aadcda385d1f4d7580b5aeb55c49d8eec6d13734894a8ac8038d768eaa9f867b1df6768d2bfa392d48e1abb5a69121703ba20281c946b01c16')
b2sums=('d2f7a9d938f6e1717934c12ff8b7127f03e71641999193fde5a11fb249da9e10b09f6620b287c046b308de93865f96989fa88a16ae0a5fe00294b3586fc6e8ce')
