from app.lib.mariadb import DB
from app.lib.resource import DaoResource

class GroupsDao(DaoResource):
    def get_groups(self):
        group_id = self.p.get("group_id")
        if group_id:
            sql = "SELECT * FROM groups WHERE group_id = '{group_id}'".format(group_id=group_id)
            return DB.select(sql)
        else:            
            sql ="SELECT * FROM groups"
            return DB.select(sql)

    def set_user(self):
        ok, cause = self.required(["group_id", "group_name", "parent_group_id"])
        if not ok:
            return False, cause

        group_id = self.p.get("group_id")
        group_name = self.p.get("group_name")
        parent_group_id = self.p.get("parent_group_id")
        sql = """
            INSERT INTO users (group_id, group_name, parent_group_id) VALUES
            ('{group_id}', '{group_name}', '{parent_group_id}')
        """.format(group_id=group_id, group_name=group_name, parent_group_id=parent_group_id)
        return DB.insert(sql)

    def del_group(self):
        ok, cause = self.required(["group_id"])
        if not ok:
            return False, cause

        group_id = self.p.get("group_id")
        ok, cause = self.get_groups()
        if not ok:
            return False, cause
        if len(cause):
            return False, "unknown group_id: {user_id}".format(group_id=group_id)
        
        sql = "DELETE FROM groups WHERE group_id = '{group_id}'".format(group_id=group_id)
        return DB.delete(sql)