TARGETNAME	:= rlm_eap_pwd

ifneq "$(OPENSSL_LIBS)" ""
ifneq "$(TARGETNAME)" ""
TARGET		:= $(TARGETNAME).a
endif
endif

SOURCES		:= $(TARGETNAME).c eap_pwd.c

SRC_CFLAGS	:= 
TGT_LDLIBS	:= 

SRC_INCDIRS	:= ../../ ../../libeap/
TGT_PREREQS	:= libfreeradius-eap.a

