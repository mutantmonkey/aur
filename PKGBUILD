## Contributor: nikicat <develniks at gmail dot com>
# Contributor: danilo <gezuru at gmail dot com>
# Contributor: Jason Begley <jayray at digitalgoat dot com>
# Contributor: Ray Kohler <ataraxia937 at gmail dot com>
# Contributor: Daniel Riedemann <daniel.riedemann [at] googlemail [dot] com>
# Contributor: 458italia <svenskaparadox [at] gmail dot com>
# Contributor: Thermi <noel [at] familie-kuntze dot com>
# Former maintainer: dkorzhevin <dkorzhevin at gmail dot com>
# Maintainer: Thermi <noel [at] familie-kuntze dot de>

pkgname=strongswan
pkgver=5.3.5
pkgrel=1
pkgdesc="open source IPsec implementation"
url='http://www.strongswan.org'
license=("GPL")
arch=('i686' 'x86_64')
depends=('curl' 'gmp' 'iproute2' 'openssl' 'sqlite')
conflicts=('openswan')
options=(!libtool)
backup=(
	etc/ipsec.conf 
	etc/swanctl/swanctl.conf
	etc/strongswan.conf 
	etc/strongswan.d/{charon-logging.conf,charon.conf,pki.conf,pool.conf,scepclient.conf,starter.conf,swanctl.conf}
	etc/strongswan.d/charon/{aesni.conf,attr-sql.conf,attr.conf,cmac.conf,connmark.conf,\
constraints.conf,curl.conf,des.conf,dhcp.conf,dnskey.conf,eap-aka-3gpp2.conf,eap-aka.conf,\
eap-gtc.conf,eap-identity.conf,eap-md5.conf,eap-mschapv2.conf,eap-radius.conf,eap-sim-file.conf,\
eap-sim.conf,eap-simaka-pseudonym.conf,eap-simaka-reauth.conf,eap-tls.conf,ext-auth.conf,farp.conf,\
fips-prf.conf,forecast.conf,gmp.conf,ha.conf,hmac.conf,kernel-netlink.conf,md5.conf,nonce.conf,openssl.conf,\
pem.conf,pgp.conf,pkcs1.conf,pkcs12.conf,pkcs7.conf,pkcs8.conf,pubkey.conf,random.conf,rc2.conf,resolve.conf,\
revocation.conf,sha1.conf,sha2.conf,socket-default.conf,sql.conf,sqlite.conf,sshkey.conf,stroke.conf,updown.conf,\
vici.conf,x509.conf,xauth-eap.conf,xauth-generic.conf,xcbc.conf,chapoly.conf}
)

source=("https://download.strongswan.org/strongswan-${pkgver}.tar.bz2")

# md5 is broken. We use sha256 now. Alternatively, we could check the signature of the file, but that
# doesn't yield any more security and just increases the work users initially have to invest.
sha256sums=('2c84b663da652b1ff180a1a73c24a3d7b9fc4b9b8ba6bd07f94a1e33092e6350')

# We don't build libipsec because it would get loaded before kernel-netlink and netkey, which
# would case processing to be handled in user space. Also, the plugin is experimental. If you need it,
# add --enable-libipsec and --enable-kernel-libipsec

build() {
  cd ${srcdir}/${pkgname}-${pkgver}

  ./configure --prefix=/usr \
        --sbindir=/usr/bin \
        --sysconfdir=/etc \
        --libexecdir=/usr/lib \
        --with-ipsecdir=/usr/lib/strongswan \
        --enable-sqlite \
        --enable-openssl --enable-curl \
        --enable-sql --enable-attr-sql \
        --enable-farp --enable-dhcp \
        --enable-eap-sim --enable-eap-sim-file --enable-eap-simaka-pseudonym \
        --enable-eap-simaka-reauth --enable-eap-identity --enable-eap-md5 \
        --enable-eap-gtc --enable-eap-aka --enable-eap-aka-3gpp2 \
        --enable-eap-mschapv2 --enable-eap-radius --enable-xauth-eap \
        --enable-ha --enable-vici --enable-swanctl --enable-systemd --enable-ext-auth \
        --disable-mysql --disable-ldap -enable-cmd --enable-forecast --enable-connmark \
	--enable-aesni --enable-eap-ttls --enable-radattr --enable-xauth-pam --enable-xauth-noauth \
	--enable-eap-dynamic --enable-eap-peap --enable-eap-tls --enable-chapoly
#	--enable-ruby-gems --enable-python-eggs
  make
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  make DESTDIR=${pkgdir} install
}

