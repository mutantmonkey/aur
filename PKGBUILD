# Maintainer: Дамјан Георгиевски <gdamjan@gmail.com>
# Maintainer: zer0def <zer0def@github>
pkgname=cloud-hypervisor
pkgver=46.0
pkgrel=1
pkgdesc="A Virtual Machine Monitor for modern Cloud workloads"
url="https://github.com/cloud-hypervisor/cloud-hypervisor"
arch=('x86_64' 'aarch64')
license=('Apache:2.0')
optdepends=(
  'virtiofsd: rust implementation of virtiofsd'
  'qemu-headless: for /usr/lib/qemu/virtiofsd'
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

sha512sums=('516dba582218a9c4ebfdbb4c866f121284e91886542ec063b0fd98c9dbd65bf4585c01d4e4214ac72eadd359799ba26c0a0878d06e156b7af29c08c3e66894b5')
b2sums=('f9bf84aeada20e44fc8fce179dbef20b699108a1be3806b83963e97f877bfbb1bfc3c4717bee9141cab3a4a4b07eaa652428438bea22ab8b52d43d0d4cc94389')
