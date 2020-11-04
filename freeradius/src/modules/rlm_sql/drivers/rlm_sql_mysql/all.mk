TARGETNAME	:= rlm_sql_mysql

ifneq "$(TARGETNAME)" ""
TARGET		:= $(TARGETNAME).a
endif

SOURCES		:= $(TARGETNAME).c

SRC_CFLAGS	:=  -I/usr/include/mysql -I/usr/include/mysql/mysql
SRC_CFLAGS	+= -I${top_srcdir}/src/modules/rlm_sql
TGT_LDLIBS	:= -L/usr/lib64/ -lmariadb 
