TARGETNAME		:= rlm_sql

ifneq "$(TARGETNAME)" ""
SUBMAKEFILES := $(TARGETNAME).mk \
	$(wildcard ${top_srcdir}/src/modules/rlm_sql/drivers/rlm_sql_*/all.mk)

rlm_sql_CFLAGS	:= 
rlm_sql_LDLIBS	:= 
endif



