# Maintainer: AlphaJack <alphajack at tuta dot io>

_pkgbase="piper-voices"
pkgname="$_pkgbase-common"
pkgver=1.0.1
pkgrel=2
pkgdesc="Voices for Piper text to speech system (common files)"
url="https://huggingface.co/rhasspy/$_pkgbase"
license=("MIT")
arch=("any")
depends=("piper-tts" "alsa-utils")
optdepends=(
 "speech-dispatcher: tts support for third party apps"
 "$_pkgbase-minimal: single voice for en-us"
 "$_pkgbase: voices for all languages")
source=(
 "https://huggingface.co/rhasspy/$_pkgbase/resolve/main/voices.json"
 "piper-tts-generic.conf"
 "piper-dispatcher"
)
b2sums=('SKIP'
        'ad4ff21c47b05bd7aef709c32ee5b1af0add40f070b649df0c62740ed46a19a87920d8099de331fd52c51e13692868630732cbd7ce6b1cc98ede59e831473f3f'
        '2dfdfe1d849ae26928754ec29a5f41036f91a11f9a51d201537bdfc61ff99ecd33c54b44120cb3feeeed28b5053b711e6111fc381f6182832b9909069fb138ce')
options=("!strip")
install="$pkgname.install"
backup=(etc/speech-dispatcher/modules/piper-tts-generic.conf)

package(){
 install -D -m 664 "$srcdir/voices.json" -t "$pkgdir/usr/share/$_pkgbase"
 install -D -m 664 "$srcdir/piper-tts-generic.conf" -t "$pkgdir/etc/speech-dispatcher/modules"
 install -D -m 775 "$srcdir/piper-dispatcher" -t "$pkgdir/usr/bin"
}
