

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def get_group_list(self):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        group_list = [node.text() for node in root.children()]
        self.close_group_editor()
        return group_list

    def add_new_group(self, name):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        input.set_text(name)
        input.type_keys("\n")
        self.close_group_editor()

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")

    def close_group_editor(self):
        self.group_editor.close()
        self.group_editor  = None

    def delete_group(self, name):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        group_index = self.get_group_index_by_name(name)
        root = tree.tree_root()
        root.children()[group_index].click()

        self.group_editor.window(auto_id="uxDeleteAddressButton").click()
        delete_window = self.app.application.window(title="Delete group")
        delete_window.window(auto_id="uxDeleteAllRadioButton").click()
        delete_window.window(auto_id="uxOKAddressButton").click()

        self.close_group_editor()

    def get_group_index_by_name(self, name):
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        i = 0
        for node in root.children():
            if node.text() == name:
                return i
            i = i + 1

        return i

    def check_group_exist(self, group):
        group_list = self.get_group_list()
        return group in group_list

