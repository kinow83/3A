#include <stdio.h>


int check_user(TALLOC_CTX *ctx, rlm_sql_t *inst, REQUEST *request, rlm_sql_handle_t **handle,
		  VALUE_PAIR **pair, char const *query)
{
    char sql[1024] = 0;
    snprintf(sql, sizeof(sql), "%s", "SELECT user_id, user_name, passwd, status, passwd_lifetime, passwd_failcount, last_passwd_changed, valid_start_date, valid_end_date, last_login, mac_check, level, simultaneous, vlanid, groups_group_id FROM users WHERE user_id = '%s'", );

}