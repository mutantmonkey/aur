# Maintainer: Jan Houben <jan@nexttrex.de>
# Contributor: Jesus Alvarez <jeezusjr at gmail dot com>
#
# This PKGBUILD was generated by the archzfs build scripts located at
#
# http://github.com/archzfs/archzfs
#
# ! WARNING !
#
# The archzfs packages are kernel modules, so these PKGBUILDS will only work with the kernel package they target. In this
# case, the archzfs-linux packages will only work with the default linux package! To have a single PKGBUILD target many
# kernels would make for a cluttered PKGBUILD!
#
# If you have a custom kernel, you will need to change things in the PKGBUILDS. If you would like to have AUR or archzfs repo
# packages for your favorite kernel package built using the archzfs build tools, submit a request in the Issue tracker on the
# archzfs github page.
#
pkgbase="zfs-linux"
pkgname=("zfs-linux" "zfs-linux-headers")
_zfsver="0.8.1"
_kernelver="5.3.arch1-1"
_extramodules="5.3.0-arch1-1-ARCH"

pkgver="${_zfsver}_$(echo ${_kernelver} | sed s/-/./g)"
pkgrel=1
makedepends=("linux-headers=${_kernelver}")
arch=("x86_64")
url="https://zfsonlinux.org/"
source=("https://github.com/zfsonlinux/zfs/releases/download/zfs-${_zfsver}/zfs-${_zfsver}.tar.gz"
        "linux-5.3-compat-rw_semaphore-owner.patch"
        "linux-5.3-compat-retire-rw_tryupgrade.patch"
        "linux-5.3-compat-Makefile-subdir-m-no-longer-supported.patch")
sha256sums=("0af79fde44b7b8ecb94d5166ce2e4fff7409c20ed874c2d759db92909e6c2799"
            "c65c950abda42fb91fb99c6c916a50720a522c53e01a872f9310a4719bae9e2a"
            "19f798a29c00874874751880f1146c5849b8ebdb6233d8ae923f9fdd4661de19"
            "6c4627875dd1724f64a196ea584812c99635897dc31cb23641f308770289059a")
license=("CDDL")
depends=("kmod" "zfs-utils=${_zfsver}" "linux=${_kernelver}")
prepare() {
    cd "${srcdir}/zfs-${_zfsver}"
    patch -Np1 -i ${srcdir}/linux-5.3-compat-rw_semaphore-owner.patch
    patch -Np1 -i ${srcdir}/linux-5.3-compat-retire-rw_tryupgrade.patch
    patch -Np1 -i ${srcdir}/linux-5.3-compat-Makefile-subdir-m-no-longer-supported.patch
}

build() {
    cd "${srcdir}/zfs-${_zfsver}"
    ./autogen.sh
    ./configure --prefix=/usr --sysconfdir=/etc --sbindir=/usr/bin --libdir=/usr/lib \
                --datadir=/usr/share --includedir=/usr/include --with-udevdir=/lib/udev \
                --libexecdir=/usr/lib/zfs-${_zfsver} --with-config=kernel \
                --with-linux=/usr/lib/modules/${_extramodules}/build \
                --with-linux-obj=/usr/lib/modules/${_extramodules}/build
    make
}

package_zfs-linux() {
    pkgdesc="Kernel modules for the Zettabyte File System."
    install=zfs.install
    provides=("zfs" "spl")
    groups=("archzfs-linux")
    conflicts=("zfs-dkms" "zfs-dkms-git" "zfs-dkms-rc" "spl-dkms" "spl-dkms-git" 'zfs-linux-git' 'zfs-linux-rc' 'spl-linux')
    replaces=("spl-linux")
    cd "${srcdir}/zfs-${_zfsver}"
    make DESTDIR="${pkgdir}" install
    cp -r "${pkgdir}"/{lib,usr}
    rm -r "${pkgdir}"/lib
    # Remove src dir
    rm -r "${pkgdir}"/usr/src
}

package_zfs-linux-headers() {
    pkgdesc="Kernel headers for the Zettabyte File System."
    provides=("zfs-headers" "spl-headers")
    conflicts=("zfs-headers" "zfs-dkms" "zfs-dkms-git" "zfs-dkms-rc" "spl-dkms" "spl-dkms-git" "spl-headers")
    cd "${srcdir}/zfs-${_zfsver}"
    make DESTDIR="${pkgdir}" install
    rm -r "${pkgdir}/lib"
    # Remove reference to ${srcdir}
    sed -i "s+${srcdir}++" ${pkgdir}/usr/src/zfs-*/${_extramodules}/Module.symvers
}
