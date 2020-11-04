TARGETNAME	:= rlm_realm

ifneq "$(TARGETNAME)" ""
TARGET		:= $(TARGETNAME).a
endif

SOURCES		:= rlm_realm.c

TRUSTROUTER	= 

SRC_CFLAGS	:= 
TGT_LDLIBS	:= 

ifneq "$(TRUSTROUTER)" ""
TGT_LDLIBS	+= -ltr_tid
SOURCES		+= trustrouter.c
endif
