TARGETNAME	:= 

ifneq "$(TARGETNAME)" ""
TARGET		:= $(TARGETNAME).a
endif

SOURCES		:= $(TARGETNAME).c logging_impl.c ike_conf.c
	      
SRC_CFLAGS	:= 
TGT_LDLIBS	:= 
TGT_LDLIBS	+= $(LIBS)
SRC_INCDIRS	:= ../../ ../../libeap/
TGT_PREREQS	:= libfreeradius-eap.a
