from app.lib.mariadb import DB
from app.lib.resource import DaoResource
from app.lib.ret import OK, FAIL

class GroupsDao(DaoResource):
    def get_groups(self):
        group_id = self.p.get("group_id")
        if group_id:
            sql = "SELECT * FROM groups WHERE group_id = '{group_id}'".format(group_id=group_id)
            return DB.select(sql)
        else:            
            sql ="SELECT * FROM groups"
            return DB.select(sql)

    def set_group(self):
        ok, res = self.required(["group_id", "group_name", "parent_group_id"])
        if not ok:
            return self.fail_required(res)

        group_id = self.p.get("group_id")
        group_name = self.p.get("group_name")
        parent_group_id = self.p.get("parent_group_id")
        sql = """
            INSERT INTO groups (group_id, group_name, parent_group_id) VALUES
            ('{group_id}', '{group_name}', '{parent_group_id}')
        """.format(group_id=group_id, group_name=group_name, parent_group_id=parent_group_id)
        return DB.insert(sql)

    def del_group(self):
        ok, res = self.required(["group_id"])
        if not ok:
            return self.fail_required(res)

        group_id = self.p.get("group_id")
        ok, res = self.get_groups()
        if not ok:
            return FAIL(res)
        if not len(res):
            return self.fail_unknown("group_id", group_id)
        
        sql = "DELETE FROM groups WHERE group_id = '{group_id}'".format(group_id=group_id)
        return DB.delete(sql)

    def mod_group(self):
        ok, res = self.required(["group_id", "group_name", "parent_group_id"])
        if not ok:
            return self.fail_required(res)

        group_id = self.p.get("group_id")
        ok, res = self.get_groups()
        if not ok:
            return FAIL(res)
        if not len(res):
            return self.fail_unknown("group_id", group_id)

        group_id = self.p.get("group_id")
        group_name = self.p.get("group_name")
        parent_group_id = self.p.get("parent_group_id")
        sql = """
            UPDATE groups SET group_name='{group_name}', parent_group_id='{parent_group_id}'
            WHERE group_id='{group_id}'
        """.format(group_id=group_id, group_name=group_name, parent_group_id=parent_group_id)
        return DB.update(sql)