# Arch Packages

PKGBUILDs used for my personal repository, including AUR packages from myself and others.

## Automatic Builds
All packages in this repository are built automatically using [geschenkerbauer](https://github.com/mutantmonkey/geschenkerbauer) running on hosted GitHub Actions runners. They can be found at the following URL:
https://deadbeef.ninja/archlinux-user/mutantmonkey/os/x86_64/

If you'd like to configure Pacman to use this repository, add the following lines to pacman.conf:
```
[mutantmonkey]
Server = https://deadbeef.ninja/archlinux-user/mutantmonkey/os/$arch
```

The `mutantmonkey-keyring` package contains the necessary signing keys.

All packages built since July 4, 2024 will have an associated attestation that
they were built using GitHub Actions. This can be be verified using:
`gh attestation verify -R mutantmonkey/aur <filename>`
