TARGETNAME	:= 

ifneq "$(TARGETNAME)" ""
TARGET		:= $(TARGETNAME).a
endif

SOURCES		:= rlm_perl.c

SRC_CFLAGS	:= 
TGT_LDLIBS	:= 
