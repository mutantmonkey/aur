# Maintainer: Jesus Alvarez <jeezusjr at gmail dot com>
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
pkgname="zfs-linux-git"
pkgver=0.6.5_r345_gdfbc863_4.6.4_1
pkgrel=1
pkgdesc="Kernel modules for the Zettabyte File System."
depends=("kmod" "spl-linux-git" "zfs-utils-linux-git" "linux=4.6.4")
makedepends=("linux-headers=4.6.4" "git")
arch=("x86_64")
url="http://zfsonlinux.org/"
source=("git+https://github.com/zfsonlinux/zfs.git")
sha256sums=("SKIP")
groups=("archzfs-linux-git")
license=("CDDL")
install=zfs.install
provides=("zfs")
replaces=("zfs-git")

build() {
    cd "${srcdir}/zfs"
    ./autogen.sh
    ./configure --prefix=/usr --sysconfdir=/etc --sbindir=/usr/bin --libdir=/usr/lib \
                --datadir=/usr/share --includedir=/usr/include --with-udevdir=/lib/udev \
                --libexecdir=/usr/lib/zfs-0.6.5.7 --with-config=kernel \
                --with-linux=/usr/lib/modules/4.6.4-1-ARCH/build \
                --with-linux-obj=/usr/lib/modules/4.6.4-1-ARCH/build
    make
}

package() {
    cd "${srcdir}/zfs"
    make DESTDIR="${pkgdir}" install
    cp -r "${pkgdir}"/{lib,usr}
    rm -r "${pkgdir}"/lib
    # Remove reference to ${srcdir}
    sed -i "s+${srcdir}++" ${pkgdir}/usr/src/zfs-*/4.6.4-1-ARCH/Module.symvers
}
