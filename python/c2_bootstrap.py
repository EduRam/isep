import json

def create_bootstrap():
    user_dict = dict()

    # List is: bank, passwd, passwd_date
    user_list = ["1", "12345678", "1"]
    user_dict["usr1"]=user_list
    user_list = ["2", "12345678", "2"]
    user_dict["usr2"]=user_list
    user_list = ["3", "12345678", "3"]
    user_dict["usr3"]=user_list
    user_list = ["4", "12345678", "4"]
    user_dict["usr4"]=user_list

    has_sucess = False
    with open('_users.json', 'w') as fp:
        json.dump(user_dict, fp, indent=4, sort_keys=True)


    resources_dict = dict()

    resources_dict["rsrc1"]="/files"
    resources_dict["rsrc2"]="/emplyees"
    resources_dict["rsrc3"]="/bank"
    resources_dict["rsrc4"]="/marketing"

    with open('_rsrc.json', 'w') as fp:
        json.dump(resources_dict, fp, indent=4, sort_keys=True)


    roles_dict = dict()

    roles_dict["role1"]="human resources"
    roles_dict["role2"]="finance team"
    roles_dict["role3"]="management"

    with open('_roles.json', 'w') as fp:
        json.dump(roles_dict, fp, indent=4, sort_keys=True)


    map_roles_to_user = dict()
    map_roles_to_user["role1"]=["usr1"]
    map_roles_to_user["role2"]=["usr1", "usr2"]
    map_roles_to_user["role3"]=["usr1", "usr2", "usr3"]
    with open('_map_roles_to_user.json', 'w') as fp:
        json.dump(map_roles_to_user, fp, indent=4, sort_keys=True)


    map_roles_to_rsrc = dict()
    map_roles_to_rsrc["role1"]=["usr1"]
    map_roles_to_rsrc["role2"]=["usr1", "usr2"]
    map_roles_to_rsrc["role3"]=["usr1", "usr2", "usr3"]
    with open('_map_roles_to_rsrc.json', 'w') as fp:
        json.dump(map_roles_to_rsrc, fp, indent=4, sort_keys=True)



# classic main entry point
if __name__ == '__main__':
    create_bootstrap()
