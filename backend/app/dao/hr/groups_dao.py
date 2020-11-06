from app.lib.mariadb import DB
from app.lib.resource import DaoResource
from app.lib.ret import OK, FAIL

class GroupsDao(DaoResource):
    def get_groups(self):
        group_id = self.p.get("group_id")
        user_id = self.p.get("user_id")
        where_sql = ""

        if user_id:
            if group_id:
                where_sql += "AND A.group_id = '{}'".format(group_id)
            sql = """
                SELECT * FROM users_groups A, groups B
                WHERE A.group_id = B.group_id AND A.user_id = '{user_id}' {where_sql}
            """.format(user_id=user_id, where_sql=where_sql)
        else:
            if group_id:
                where_sql += "AND group_id = '{}'".format(group_id)
            sql = "SELECT * FROM groups WHERE 1=1 {where_sql}".format(where_sql=where_sql)
        return DB.select(sql)

    def get_groups_tree(self):
        group_id = self.p.get("group_id")
        where_sql = ""

        if group_id:
            where_sql += "AND group_id = '{}'".format(group_id)
        sql = """
            SELECT group_id, group_id `key`, group_name, group_name label, parent_group_id, mac_check, vlanid, created, changed
            FROM groups WHERE 1=1 {where_sql}
        """.format(where_sql=where_sql)
        ok, res = DB.select(sql)
        if not ok:
            return self.fail_message(res)

        root = list(filter(lambda g: g["group_id"] == g["parent_group_id"], res))
        print(root)
        res  = list(filter(lambda g: g["group_id"] != g["parent_group_id"], res))
        tree = root[0]


        self.get_groups_subtree(res, tree)        
        self.debug_groups_tree(tree)

        return OK([tree])
   
    def debug_groups_tree(self, tree, depth=0):
        msg = ""
        for i in range(depth):
            msg += " "
        msg += "{} ({})".format(tree["group_id"], tree["group_name"])
        print(msg)
        if tree.get("children"):
            for g in tree.get("children"):
                self.debug_groups_tree(g, depth+1)

    def get_groups_subtree(self, groups, tree):
        for g in groups:
            if not g.get("tag") and tree["group_id"] == g["parent_group_id"]:
                g["tag"] = True
                if tree.get("children"):
                    tree.get("children").append(g)                    
                else:
                    tree["children"] = [g]
                self.get_groups_subtree(groups, g)

    def set_group(self):
        ok, res = self.required(["group_id", "group_name"])
        if not ok:
            return self.fail_required(res)

        group_id = self.p.get("group_id")
        group_name = self.p.get("group_name")
        parent_group_id = self.p.get("parent_group_id")
        if not parent_group_id:
            parent_group_id = group_id
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