import json

class Model:

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

    
    def load_bootstrap(self):

        print("Load bootstrap")

        with open(self.user_filename) as json_file:
            self.user_dict = json.load(json_file)
        
        with open(self.rsrc_filename) as json_file:
            self.resources_dict = json.load(json_file)

        with open(self.roles_filename) as json_file:
            self.roles_dict = json.load(json_file)

        print("End bootstrap")
