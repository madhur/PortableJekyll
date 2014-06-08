# Call MinGW32 Makefile with the dependencies libcurl is build.
export DEVELPACKAGE = 1
ifeq ($(findstring lib64,$(wildcard ../lib64/)),lib64)
export ARCH = w64
endif

all:
ifeq ($(ARCH),w64)
	@echo compiling 64-bit samples ...
	$(MAKE) -f Makefile.m32 SSL=1 SSH2=1 ZLIB=1 RTMP=1 SSPI=1 WINIDN=1
else
	@echo compiling 32-bit samples ...
	$(MAKE) -f Makefile.m32 SSL=1 SSH2=1 ZLIB=1 RTMP=1 SSPI=1 IDN=1
endif

clean:
	$(MAKE) -f Makefile.m32 clean

vclean:
	$(MAKE) -f Makefile.m32 vclean

