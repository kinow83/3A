TARGETNAME	:= 

ifneq "$(TARGETNAME)" ""
TARGET		:= $(TARGETNAME).a
endif

SOURCES		:= $(TARGETNAME).c

SRC_CFLAGS	:=  
SRC_CFLAGS  += -I${top_srcdir}/src/modules/rlm_sql

# Comment this out if you're experiencing build errors
SRC_CFLAGS  += -Wno-strict-prototypes
TGT_LDLIBS	:= 
