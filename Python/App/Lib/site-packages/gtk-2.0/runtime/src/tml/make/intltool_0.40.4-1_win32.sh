# This is a shell script that calls functions and scripts from
# tml@iki.fi's personal work environment. It is not expected to be
# usable unmodified by others, and is included only for reference.

MOD=intltool
VER=0.40.4
REV=1
ARCH=win32

THIS=${MOD}_${VER}-${REV}_${ARCH}

RUNZIP=${MOD}_${VER}-${REV}_${ARCH}.zip
DEVZIP=${MOD}-dev_${VER}-${REV}_${ARCH}.zip

HEX=`echo $THIS | md5sum | cut -d' ' -f1`
TARGET=c:/devel/target/$HEX

usedev

(

set -x

PERL=$INTLTOOL_PERL ./configure --prefix=$TARGET &&

make install &&

make check &&

cd /devel/target/$HEX &&
rm -f /tmp/$RUNZIP &&
zip -r -D /tmp/$RUNZIP . &&
rm -f /tmp/$DEVZIP

) 2>&1 | tee /devel/src/tml/make/$THIS.log

(cd /devel && zip /tmp/$DEVZIP src/tml/make/$THIS.{sh,log}) &&
manifestify /tmp/$RUNZIP /tmp/$DEVZIP
