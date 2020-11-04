TARGETNAME	:= 

ifneq "$(TARGETNAME)" ""
TARGET		:= $(TARGETNAME).a
endif

SOURCES		:= $(TARGETNAME).c attrmap.c ldap.c clients.c groups.c edir.c 

SRC_CFLAGS	:= 
TGT_LDLIBS	:= 
