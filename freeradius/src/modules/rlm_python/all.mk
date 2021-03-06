TARGETNAME	:= 

ifneq "$(TARGETNAME)" ""
TARGET		:= $(TARGETNAME).a
endif

SOURCES		:= $(TARGETNAME).c

SRC_CFLAGS	:= 
TGT_LDLIBS	:= 

ifneq "$(TARGETNAME)" ""
install: $(R)$(modconfdir)/python/radiusd.py $(R)$(modconfdir)/python/example.py

$(R)$(modconfdir)/python: | $(R)$(modconfdir)
	@echo INSTALL $(patsubst $(R)$(raddbdir)%,raddb%,$@)
	@$(INSTALL) -d -m 750 $@

$(R)$(modconfdir)/python/radiusd.py: src/modules/rlm_python/radiusd.py | $(R)$(modconfdir)/python
	@$(ECHO) INSTALL $(notdir $<)
	@$(INSTALL) -m 755 $< $(R)$(modconfdir)/python

$(R)$(modconfdir)/python/example.py: src/modules/rlm_python/example.py | $(R)$(modconfdir)/python
	@$(ECHO) INSTALL $(notdir $<)
	@$(INSTALL) -m 755 $< $(R)$(modconfdir)/python
endif
