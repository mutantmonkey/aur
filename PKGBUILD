# Maintainer: Daniel Egeberg <daniel.egeberg@gmail.com>
# Contributor: Sven-Hendrik Haase <sh@lutzhaase.com>
# Contributor: TingPing <tingping@tingping.se>

pkgname=plex-media-player
pkgver=1.2.3
_gitrev=589
_gitver=59a54305
_fullname="$pkgname-$pkgver.$_gitrev-$_gitver"
pkgrel=1
pkgdesc='Next generation Plex Desktop Client'
arch=('i686' 'x86_64' 'armv7h')
license=('GPL')
url='https://github.com/plexinc/plex-media-player'
depends=('mpv' 'qt5-webengine>=5.6' 'libcec3' 'sdl2' 'qt5-x11extras' 'qt5-quickcontrols' 'p8-platform' 'protobuf')
makedepends=('cmake' 'conan')
source=("$_fullname.tar.gz::https://github.com/plexinc/plex-media-player/archive/v${pkgver}.${_gitrev}-${_gitver}.tar.gz"
        'plex-media-player.desktop')
noextract=("plex-web-client-konvergo-$_webclientver.cpp.tbz2")
sha512sums=('a8f0d4eaf7abdf761135cfabf46ff833c8ce0d34affd7c538e85afc0c58d8bae76922b49be8e7dcc5f85358b83346d6f6c5628f41cbe57f353948ea28db6553e'
            'f24d70646babc2d248d6159442e3b9d5518276e7d8e33004f13d260953ebcd741067c507a47de25c24842e4391f4c403cdb46dc989b52fa1dde38a7312382db1')

prepare() {
	cd "$_fullname"

	# All this git version junk fails, just remove it we already have the version
	sed -i 's|include(GetGitRevisionDescription)||
	        s|get_git_head_revision(REFSPEC FULL_GIT_REVISION)||' \
	       CMakeModules/VersionConfiguration.cmake

    sed -i 's|#include <libcec/|#include <libcec3/|' \
           src/input/InputCEC.h

    conan_remote="https://conan.plex.tv"
    msg2 "Checking for plex conan remote"
    if conan remote list | grep -q plex; then
        msg2 "plex remote exists for conan"
    else
        msg2 "Adding ${conan_remote} as a conan remote"
        conan remote add plex "$conan_remote"
    fi

	mkdir -p build
    cd build
    conan install ..
}

build() {
	cd "$_fullname/build"

	cmake -DCMAKE_INSTALL_PREFIX='/usr' -DCMAKE_BUILD_TYPE='Release' -DCMAKE_SKIP_RPATH=1 \
	      -DFULL_GIT_REVISION="$_gitver" -DQTROOT='/usr/share/qt' -DCEC_INCLUDE_DIR=/usr/include/libcec3 \
          -DCEC_LIBRARY=/usr/lib/libcec.so.3 ..
	make
}

package() {
	cd "$_fullname/build"

	DESTDIR="$pkgdir" make install

	install -Dm644 "$srcdir/plex-media-player.desktop" "$pkgdir/usr/share/applications/plex-media-player.desktop"
	install -Dm644 ../resources/images/icon.png "$pkgdir/usr/share/icons/hicolor/256x256/apps/plex-media-player.png"
}
