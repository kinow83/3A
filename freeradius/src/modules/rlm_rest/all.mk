TARGETNAME	:= 

ifneq "$(TARGETNAME)" ""
TARGET		:= $(TARGETNAME).a
endif

SOURCES		:= $(TARGETNAME).c rest.c

SRC_CFLAGS	:=  
TGT_LDLIBS	:=  




