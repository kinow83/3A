TARGETNAME	:= 

ifneq "$(TARGETNAME)" ""
TARGET		:= $(TARGETNAME).a
endif

SOURCES		:= $(TARGETNAME).c krb5.c

SRC_CFLAGS	:=   
SRC_CFLAGS	+= -DKRB5_DEPRECATED
TGT_LDLIBS	:=  -lcrypto -L/lib -Wl,-rpath,/lib -lcrypto 
