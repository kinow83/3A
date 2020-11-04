TARGETNAME	:= 

ifneq "$(TARGETNAME)" ""
TARGET		:= $(TARGETNAME).a
endif

SOURCES		:= $(TARGETNAME).c

SRC_CFLAGS	:= 
SRC_CFLAGS	+= -I${top_srcdir}/src/modules/rlm_sql
TGT_LDLIBS	:= 
