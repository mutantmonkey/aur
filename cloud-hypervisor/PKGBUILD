# Maintainer: zer0def <zer0def@github>
pkgname=cloud-hypervisor
pkgver=41.0
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
source=("https://github.com/cloud-hypervisor/cloud-hypervisor/archive/v${pkgver}.tar.gz")

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

sha512sums=('00e37a38ddfc4556c0ef41e4db2552d613be50aeaede8e4ab297c0303943df5fa45ba8fee307410ecb3780c77fce9048e0ff95525336a3271d7d7e2ede61eac2')
b2sums=('35f58aee92ad60ad49704903d18d56d0216bc889d824afb88df46b83d6506d974b1038a5f923a6d0672e69106b195928da143cf99dfa380e034bc0047dec3267')
sha512sums=('41922825a958b9db279326a12a864bd699ee04ba4301d8903d77a94ef0473e58d9e687da320553d704c02f1c8949114bd6c693fe2ceed79bfe6221bccd1ed7e1')
b2sums=('f6f69cc4a897a1e6e3f117c541f05cd5db5e406b635c0f7d0c5b7d4f462c49000c1bf09946b06dc48db3e8469859fe1fd425717bed7ece9e7bc0bc766fccf8cf')
