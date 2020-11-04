#######################################################################
#
# TARGET should be set by autoconf only.  Don't touch it.
#
# The SOURCES definition should list ALL source files.
#
# SRC_CFLAGS defines addition C compiler flags.  You usually don't
# want to modify this, though.  Get it from autoconf.
#
# The TGT_LDLIBS definition should list ALL required libraries.
#
#######################################################################

TARGETNAME	:= rlm_yubikey

ifneq "$(TARGETNAME)" ""
TARGET		:= $(TARGETNAME).a
endif

SOURCES		:= $(TARGETNAME).c validate.c decrypt.c

SRC_CFLAGS	:= 
TGT_LDLIBS	:= 
