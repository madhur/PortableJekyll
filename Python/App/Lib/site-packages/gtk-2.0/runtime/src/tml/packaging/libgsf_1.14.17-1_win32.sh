# This is a shell script that calls functions and scripts from
# tml@iki.fi's personal work environment. It is not expected to be
# usable unmodified by others, and is included only for reference.

MOD=libgsf
VER=1.14.17
REV=1
ARCH=win32

THIS=${MOD}_${VER}-${REV}_${ARCH}

RUNZIP=${MOD}_${VER}-${REV}_${ARCH}.zip
DEVZIP=${MOD}-dev_${VER}-${REV}_${ARCH}.zip

GNOMERUNZIP=${MOD}-gnome_${VER}-${REV}_${ARCH}.zip
GNOMEDEVZIP=${MOD}-gnome-dev_${VER}-${REV}_${ARCH}.zip

HEX=`echo $THIS | md5sum | cut -d' ' -f1`
TARGET=c:/devel/target/$HEX

usedev
usemsvs6

(

set -x

DEPS=`latest --arch=${ARCH} glib pkg-config atk pango gtk+ libIDL ORBit2 libbonobo GConf gnome-vfs libxml2 zlib intltool`
PROXY_LIBINTL=`latest --arch=${ARCH} proxy-libintl`
ZLIB=`latest --arch=${ARCH} zlib`

PKG_CONFIG_PATH=/dummy
for D in $DEPS; do
    PATH="/devel/dist/${ARCH}/$D/bin:$PATH"
    [ -d /devel/dist/${ARCH}/$D/lib/pkgconfig ] && PKG_CONFIG_PATH=/devel/dist/${ARCH}/$D/lib/pkgconfig:$PKG_CONFIG_PATH
done

# Avoid the silly "relink" stuff in libtool
sed -e 's/need_relink=yes/need_relink=no # no way --tml/' <ltmain.sh >ltmain.temp && mv ltmain.temp ltmain.sh

# Avoid using "file" in libtool. Otherwise libtool won't create a
# shared library, and give the warning "Trying to link with static lib
# archive [...] But I can only do this if you have shared version of
# the library, which you do not appear to have." I know what I am
# doing, I do want to link with a static libintl now. (The
# proxy-libintl libintl wrapper.)

sed -e 's!file /!dont-want-to-use-file!' <configure >configure.temp && mv configure.temp configure

CC='gcc -mthreads' \
CPPFLAGS="-DBONOBO_DISABLE_DEPRECATED \
-I/devel/dist/${ARCH}/${PROXY_LIBINTL}/include \
-I/devel/dist/${ARCH}/${ZLIB}/include" \
LDFLAGS="-L/devel/dist/${ARCH}/${PROXY_LIBINTL}/lib -Wl,--exclude-libs=libintl.a \
-L/devel/dist/${ARCH}/${ZLIB}/lib" \
CFLAGS=-O \
./configure --disable-gtk-doc --without-python --disable-static --prefix=$TARGET &&

# Do NOT use libtool-cache for libgsf! It breaks build in tools
make -j3 install &&
./libgsf-zip &&

mv /tmp/${MOD}-${VER}.zip /tmp/$RUNZIP &&
mv /tmp/${MOD}-dev-${VER}.zip /tmp/$DEVZIP

mv /tmp/${MOD}-gnome-${VER}.zip /tmp/$GNOMERUNZIP &&
mv /tmp/${MOD}-gnome-dev-${VER}.zip /tmp/$GNOMEDEVZIP

) 2>&1 | tee /devel/src/tml/packaging/$THIS.log

(cd /devel && zip /tmp/$DEVZIP src/tml/packaging/$THIS.{sh,log}) &&
manifestify /tmp/$RUNZIP /tmp/$DEVZIP &&
manifestify /tmp/$GNOMERUNZIP /tmp/$GNOMEDEVZIP
