TARGETNAME	:= 

ifneq "$(TARGETNAME)" ""
TARGET		:= $(TARGETNAME).a
endif

SOURCES		:= $(TARGETNAME).c

SRC_CFLAGS	:= 
TGT_LDLIBS	:= 

ifneq "$(TARGETNAME)" ""
install: $(R)$(bindir)/rad_counter

$(R)$(bindir)/rad_counter: src/modules/rlm_counter/rad_counter | $(R)$(bindir)
	@$(INSTALL) -m 755 src/modules/rlm_counter/rad_counter $(R)$(bindir)/
endif
