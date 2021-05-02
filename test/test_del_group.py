

def test_del_group(app):
    group_name = 'my group'
    old_list = app.groups.get_group_list()
    if not app.groups.check_group_exist(group_name):
        app.groups.add_new_group(group_name)
        old_list = app.groups.get_group_list()
    app.groups.delete_group(group_name)
    new_list = app.groups.get_group_list()
    assert len(old_list) - 1 == len(new_list)
