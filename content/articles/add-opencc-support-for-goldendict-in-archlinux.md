---
Title: Add Opencc Support for Goldendict in Archlinux
Date: 2020-1-23 18:20
Category: Tutorial
Tags: Tutorial
Slug: add-opencc-support-for-goldendict-in-archlinux
Summary: Tutoral of adding Opencc support for Goldendict in Archlinux
---

First, download `PKGBUILD` and `goldendict.changelog`: `$ yay -G goldendict`

After that, edit the `PKGBUILD` file in the folder `goldendict`.  
From:  
``` bash
...
depends=('hunspell' 'libxtst' 'libzip' 'libao' 'qt5-webkit' 'qt5-svg' 'qt5-x11extras' 'qt5-tools' 'phonon-qt5' 'ffmpeg')
...
build(){
    cd "${srcdir}"/$pkgname-1.5.0-RC2  
    qmake-qt5 "CONFIG+=no_epwing_support" PREFIX="/usr"

    make
}  
...
```
To:  
``` bash
...
depends=('hunspell' 'libxtst' 'libzip' 'libao' 'qt5-webkit' 'qt5-svg' 'qt5-x11extras' 'qt5-tools' 'phonon-qt5' 'ffmpeg' 'opencc')
...
build(){
    cd "${srcdir}"/$pkgname-1.5.0-RC2
    qmake-qt5 "CONFIG+=no_epwing_support chinese_conversion_support" PREFIX="/usr"

    make
}
...
```

In the end, build and install goldendict: `$ makepkg -si`
