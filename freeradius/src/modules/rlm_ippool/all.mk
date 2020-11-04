#
# $Id$
#
TARGETNAME		:= 

ifneq "$(TARGETNAME)" ""
SUBMAKEFILES		:= rlm_ippool.mk rlm_ippool_tool.mk

# Used by SUBMAKEFILES
rlm_ippool_CFLAGS	:= 
rlm_ippool_LDLIBS	:= 
endif
