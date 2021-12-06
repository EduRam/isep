import json
import time
import os

class Model:

    version = 0

    def __init__(self):
        self.user_filename = "_users.json"
        self.rsrc_filename = "_rsrc.json"
        self.roles_filename = "_roles.json"
        self.map_user_to_roles_filename = "_map_user_to_roles.json"
        self.map_role_to_resources_filename = "_map_role_to_rsrcs.json"

        self.map_role_to_resources = dict()
        self.map_user_to_roles = dict()
        self.roles_dict = dict()
        self.resources_dict = dict()
        self.users_dict = dict()


    def get_role_resources(self, role):
        # return a list of roles for user
        # if user does not have roles, return empty list
        return self.map_role_to_resources.get(role, [])


    def get_user_roles(self, user_email):
        # return a list of roles for user
        # if user does not have roles, return empty list
        return self.map_user_to_roles.get(user_email, [])


    def add_user(self, email, bank, passwd):
        usr_list = list()
        usr_list.append(bank)
        usr_list.append(passwd)
        usr_list.append(int(time.time()))

        if not email in self.users_dict:
            self.users_dict[email] = usr_list
        else:
            return False



    def del_user(self, email):
        self.users_dict.pop(email, None)
        return


    def add_rsrc(self, rsrc, url):
        if not rsrc in self.resources_dict:
            self.resources_dict[rsrc] = url
        else:
            return False        
        return


    def del_rsrc(self, rsrc):
        self.resources_dict.pop(rsrc, None)
        return


    def add_role(self, role, role_description):
        if not role in self.roles_dict:
            self.roles_dict[role] = role_description
        else:
            return False        
        return


    def del_role(self, role):
        self.roles_dict.pop(role, None)
        return




    def save(self):

        self.version =+ 1
        wip_filename = str(self.version) + ".wip"

        try:
            with open(str(self.version) + self.user_filename, 'w') as fp:
                json.dump(self.users_dict, fp, indent=4, sort_keys=True)

            with open(str(self.version) + self.rsrc_filename, 'w') as fp:
                json.dump(self.resources_dict, fp, indent=4, sort_keys=True)            

            with open(str(self.version) + self.roles_filename, 'w') as fp:
                json.dump(self.roles_dict, fp, indent=4, sort_keys=True)            

            with open(str(self.version) + self.map_user_to_roles_filename, 'w') as fp:
                json.dump(self.map_user_to_roles, fp, indent=4, sort_keys=True)            

            with open(str(self.version) + self.map_role_to_resources_filename, 'w') as fp:
                json.dump(self.map_role_to_resources, fp, indent=4, sort_keys=True)            

            open(wip_filename, 'a').close()
        except OSError:
            print('Failed creating the file ' + wip_filename)
        else:
            print('File created ' + wip_filename)

            #remove previous files version


        return

    
    def load_bootstrap(self):

        print("Load bootstrap")

        with open(self.user_filename) as json_file:
            self.users_dict = json.load(json_file)
        
        with open(self.rsrc_filename) as json_file:
            self.resources_dict = json.load(json_file)

        with open(self.roles_filename) as json_file:
            self.roles_dict = json.load(json_file)

        print("End bootstrap")
