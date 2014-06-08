# This is a shell script that calls functions and scripts from
# tml@iki.fi's personal work environment. It is not expected to be
# usable unmodified by others, and is included only for reference.

MOD=librsvg
VER=2.32.1
REV=1
ARCH=win32

THIS=${MOD}_${VER}-${REV}_${ARCH}

RUNZIP=${MOD}_${VER}-${REV}_${ARCH}.zip
DEVZIP=${MOD}-dev_${VER}-${REV}_${ARCH}.zip
ENGINEZIP=svg-gtk-engine_${VER}-${REV}_${ARCH}.zip
LOADERZIP=svg-gdk-pixbuf-loader_${VER}-${REV}_${ARCH}.zip

HEX=`echo $THIS | md5sum | cut -d' ' -f1`
TARGET=c:/devel/target/$HEX

usedev

(

set -x

DEPS=`latest --arch=${ARCH} zlib gettext-runtime glib atk pango cairo gdk-pixbuf gtk+ freetype fontconfig libgsf libcroco libxml2 libpng`

GETTEXT_RUNTIME=`latest --arch=${ARCH} gettext-runtime`
WIN_ICONV=`latest --arch=${ARCH} win-iconv`

PKG_CONFIG_PATH=/dummy
for D in $DEPS; do
    PATH="/devel/dist/${ARCH}/$D/bin:$PATH"
    [ -d /devel/dist/${ARCH}/$D/lib/pkgconfig ] && PKG_CONFIG_PATH=/devel/dist/${ARCH}/$D/lib/pkgconfig:$PKG_CONFIG_PATH
done

patch --verbose -p1 --fuzz=0 <<'EOF' &&
commit 5025519279c301362ec5a053d83be72d92bd5695
Author: Tor Lillqvist <tml@iki.fi>
Date:   Mon Dec 27 19:16:38 2010 +0200

    Pick loader DLL from correct place
    
    We install the loader DLL in gdk-pixbuf's tree. When zipping up the
    loader package, move it from there to be under our own install tree,
    and remove the unnecessary libtool archive and import library.

diff --git a/librsvg-zip.in b/librsvg-zip.in
index e295e85..0e8c314 100755
--- a/librsvg-zip.in
+++ b/librsvg-zip.in
@@ -22,15 +22,17 @@ rm $DEVZIP
 zip -r -D $DEVZIP -@ <<EOF
 bin/rsvg-convert.exe
 bin/rsvg-view.exe
-include/librsvg-2
+include/librsvg-2.0
 lib/librsvg-2.dll.a
 lib/pkgconfig/librsvg-2.0.pc
 EOF
 
-gtk_binary_version=`pkg-config --variable=gtk_binary_version gtk+-2.0`
-
 rm $ENGINEZIP
-zip $ENGINEZIP lib/gtk-2.0/${gtk_binary_version}/engines/libsvg.dll
+zip $ENGINEZIP lib/gtk-2.0/@GTK2_BINARY_VERSION@/engines/libsvg.dll
 
 rm $LOADERZIP
-zip $LOADERZIP lib/gtk-2.0/${gtk_binary_version}/loaders/svg_loader.dll
+mkdir -p lib/gdk-pixbuf-2.0/@gdk_pixbuf_binary_version@/loaders
+mv @gdk_pixbuf_binarydir@/loaders/libpixbufloader-svg.dll lib/gdk-pixbuf-2.0/@gdk_pixbuf_binary_version@/loaders
+rm -f @gdk_pixbuf_binarydir@/loaders/libpixbufloader-svg.dll.a
+rm -f @gdk_pixbuf_binarydir@/loaders/libpixbufloader-svg.la
+zip $LOADERZIP lib/gdk-pixbuf-2.0/@gdk_pixbuf_binary_version@/loaders/libpixbufloader-svg.dll
EOF

# Avoid the silly "relink" stuff in libtool
sed -e 's/need_relink=yes/need_relink=no # no way --tml/' <ltmain.sh >ltmain.temp && mv ltmain.temp ltmain.sh

CC='gcc -mthreads' CPPFLAGS="-I/devel/dist/${ARCH}/${GETTEXT_RUNTIME}/include -I/devel/dist/${ARCH}/${WIN_ICONV}/include" LDFLAGS="-L/devel/dist/${ARCH}/${GETTEXT_RUNTIME}/lib -Wl,--enable-auto-image-base" CFLAGS=-O2 ./configure --disable-gtk-doc --disable-static --prefix=$TARGET &&

PATH=/devel/target/$HEX/bin:$PATH make -j4 install &&

echo 'To add SVG for support to your gdk-pixbuf installation for Windows, 
follow these instructions:

1. Download the svg pixbuf loader. You can find it here:
http://ftp.gnome.org/pub/gnome/binaries/win32/librsvg/

2. Download the dependencies:
libcroco: http://ftp.gnome.org/pub/gnome/binaries/win32/libcroco/
libgsf: http://ftp.gnome.org/pub/gnome/binaries/win32/libgsf/
libxml2: http://ftp.gnome.org/pub/gnome/binaries/win32/dependencies
bzip2: http://ftp.gnome.org/pub/gnome/binaries/win32/dependencies

3. Unzip them to the appropriate location (eg, your main application
directory) so that for instance librsvg-2-2.dll ends up in the same
directory as your application'"'"'s .exe. Note that the svg_loader.dll
should not be there, but in gdk-pixbuf'"'"'s loaders directory,
lib\gdk-pixbuf-2.0\2.10.0\loaders.

4. Run gdk-pixbuf-query-loaders to re-create the loaders.cache
file. It might be better that you redirect the output of this
command to create the file rather than edit the file by hand. An
example command follows:

  bin\gdk-query-pixbufloaders >lib\gdk-pixbuf-2.0\2.10.0\loaders.cache' >$TARGET/svg-gdk-pixbuf-loader.README.txt

./librsvg-zip &&

(cd $TARGET && zip /tmp/svg-gdk-pixbuf-loader_${VER}-${REV}_${ARCH}.zip svg-gdk-pixbuf-loader.README.txt) &&

mv /tmp/${MOD}-${VER}.zip /tmp/$RUNZIP &&
mv /tmp/${MOD}-dev-${VER}.zip /tmp/$DEVZIP &&

mv /tmp/svg-gtk-engine-${VER}.zip /tmp/$ENGINEZIP
mv /tmp/svg-gdk-pixbuf-loader-${VER}.zip /tmp/$LOADERZIP

) 2>&1 | tee /devel/src/tml/packaging/$THIS.log

(cd /devel && zip /tmp/$DEVZIP src/tml/packaging/$THIS.{sh,log}) &&
manifestify /tmp/$RUNZIP /tmp/$DEVZIP &&

manifestify /tmp/$ENGINEZIP
manifestify /tmp/$LOADERZIP
