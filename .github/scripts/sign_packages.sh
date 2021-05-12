#!/bin/bash
install -d -m0700 /tmp/signify
echo "$SIGNIFY_SECRET_KEY" > /tmp/signify/pkg.sec
sha512sum *.pkg.tar.* > SHA512SUMS
signify -S -s /tmp/signify/pkg.sec -m SHA512SUMS -x SHA512SUMS.sig <<< "$SIGNIFY_PASSWORD"
rm -rf /tmp/signify
