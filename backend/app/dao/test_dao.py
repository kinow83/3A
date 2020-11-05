from app.lib.mariadb import DB
from app.lib.resource import DaoResource
from app.lib.ret import OK, FAIL
from app.api.hr.groups_api import *
from app.api.hr.users_api import *
from app.api.lg.radauthlog_api import *

if __name__ == '__main__':
    p = {
        "group_id": "a",
        "group_name": "a",
        "parent_group_id": "a",
    }
    GroupsDao(p).set_group()
    p = {
        "group_id": "aa",
        "group_name": "aa",
        "parent_group_id": "a",
    }
    GroupsDao(p).set_group()
    p = {
        "group_id": "ab",
        "group_name": "ab",
        "parent_group_id": "a",
    }
    GroupsDao(p).set_group()
    p = {
        "group_id": "abb",
        "group_name": "abb",
        "parent_group_id": "ab",
    }
    GroupsDao(p).set_group()
    p = {
        "group_id": "aaa",
        "group_name": "aaa",
        "parent_group_id": "aa",
    }
    GroupsDao(p).set_group()
    GroupsDao({}).get_groups_tree()