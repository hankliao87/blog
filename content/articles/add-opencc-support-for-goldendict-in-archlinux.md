---
Title: Add Opencc Support for Goldendict in Archlinux
Date: 2020-1-23 18:20
Category: Tutorial
Tags: Tutorial
Slug: add-opencc-support-for-goldendict-in-archlinux
Summary: Tutorial of adding opencc support for goldendict in archlinux
---

<div class="mx-auto" style="width:75%;">
  <figure class="figure">
    <img src="{attach}/images/add-opencc-support-for-goldendict-in-archlinux-option.png" class="figure-img img-fluid rounded" alt="">
    <figcaption class="figure-caption text-center">The transliteration option in goldendict with opencc support.</figcaption>
  </figure>
</div>


When you install goldendict using `yay`, you won't see the `Chinese Conversion` section in the transliteration option. This is because the method of building goldendict provided by the community doesn't add the dependent package of the chinese conversion. According to the [README of goldendict](https://github.com/goldendict/goldendict#building-with-chinese-conversion-support), we just need to add the dependent package `opencc` before building it.  

First, download `PKGBUILD` and `goldendict.changelog`: `$ yay -G goldendict`  

After that, edit the `PKGBUILD` file in the folder `goldendict`.  
Change from  
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
to  
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
