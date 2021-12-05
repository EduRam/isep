import json
import time
import os

class Model:

    version = 0

    def __init__(self):
        self.user_filename = "_users.json"
        self.rsrc_filename = "_rsrc.json"
        self.roles_filename = "_roles.json"
        self.map_roles_to_user_filename = "_map_roles_to_user"
        self.map_roles_to_rsrc_filename = "_map_roles_to_rsrc.json"

        self.map_roles_to_rsrc = dict()
        self.map_roles_to_user = dict()
        self.roles_dict = dict()
        self.resources_dict = dict()
        self.user_dict = dict()


    def add_user(self, email, bank, passwd):
        usr_list = list()
        usr_list.append(bank)
        usr_list.append(passwd)
        usr_list.append(int(time.time()))

        if not email in self.user_dict:
            self.user_dict[email] = usr_list
        else:
            return False



    def del_user(self, email):
        self.user_dict.pop(email, None)
        return


    def save(self):

        self.version =+ 1
        wip_filename = str(self.version) + ".wip"

        try:
            open(wip_filename, 'a').close()
        except OSError:
            print('Failed creating the file ' + wip_filename)
        else:
            print('File created ' + wip_filename)

        with open(str(self.version) + '_users.json', 'w') as fp:
            json.dump(self.user_dict, fp, indent=4, sort_keys=True)
        with open(str(self.version) + '_rsrc.json', 'w') as fp:
            json.dump(self.resources_dict, fp, indent=4, sort_keys=True)            
        with open(str(self.version) + '_roles.json', 'w') as fp:
            json.dump(self.roles_dict, fp, indent=4, sort_keys=True)            
        with open(str(self.version) + '_map_roles_to_user.json', 'w') as fp:
            json.dump(self.map_roles_to_user, fp, indent=4, sort_keys=True)            

        try:
            os.remove(wip_filename)
        except OSError:
            print('Failed creating the file ' + wip_filename)
        else:
            print('File removed ' + wip_filename)

        return

    
    def load_bootstrap(self):

        print("Load bootstrap")

        with open(self.user_filename) as json_file:
            self.user_dict = json.load(json_file)
        
        with open(self.rsrc_filename) as json_file:
            self.resources_dict = json.load(json_file)

        with open(self.roles_filename) as json_file:
            self.roles_dict = json.load(json_file)

        print("End bootstrap")
