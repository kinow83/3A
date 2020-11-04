TARGETNAME	:= rlm_unix

ifneq "$(TARGETNAME)" ""
TARGET		:= $(TARGETNAME).a
endif

SOURCES		:= $(TARGETNAME).c

SRC_CFLAGS	:= 
TGT_LDLIBS	:= 
