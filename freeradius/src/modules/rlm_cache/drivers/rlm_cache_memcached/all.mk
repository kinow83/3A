TARGETNAME	:= 

ifneq "$(TARGETNAME)" ""
TARGET		:= $(TARGETNAME).a
endif

SOURCES		:= $(TARGETNAME).c ../../serialize.c

SRC_CFLAGS	:= 
TGT_LDLIBS	:=   -lpthread 
