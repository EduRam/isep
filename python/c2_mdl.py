import json
import time
import hashlib
import glob
import os

class Model:

    version = 0
    salt = ''

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

        if email in self.users_dict:
            print("User already exists. You may try to delete it and try again.")
            return


        # (cyber) do not store plain passwords
        # Key derivation and key stretching algorithms are designed for secure password hashing. 
        # Naive algorithms such as sha1(password) are not resistant against brute-force attacks. 
        # A good password hashing function must be tunable, slow, and include a salt.        
        # Source: https://docs.python.org/3/library/hashlib.html

        passwd_hash_bytes = hashlib.pbkdf2_hmac('sha256', passwd.encode('utf-8'), str(self.salt).encode('utf-8'), 100000)

        # convert to hex, so it is only represented with letters and numbers 
        # (not special characters)
        passwd_hex_string = passwd_hash_bytes.hex()

        usr_list = list()
        usr_list.append(bank)
        usr_list.append(passwd_hex_string)
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

        for role in self.map_role_to_resources:
            for resource in self.get_role_resources(role):
                if rsrc == resource:
                    print("Could not remove resource: {} because it is associated with role: {}".format(rsrc, role))
                    return


        self.resources_dict.pop(rsrc, None)
        return


    def add_role(self, role, role_description):
        if not role in self.roles_dict:
            self.roles_dict[role] = role_description
        else:
            return False        
        return


    def del_role(self, role):

        for user in self.map_user_to_roles:
            for test_role in self.get_user_roles(user):
                if test_role == role:
                    print("Could not remove role: {} because it is associated with user: {}".format(role, user))
                    return

        self.roles_dict.pop(role, None)
        return


    # (CYBER) calculate a unique hash for all files
    # This will be used to detect if anyone changed the files
    def calculate_global_checksum(self, version):

        version_user_filename   = str(version) + self.user_filename
        version_rsrc_filename   = str(version) + self.rsrc_filename
        version_roles_filename  = str(version) + self.roles_filename
        version_map_user_to_roles_filename      = str(version) + self.map_user_to_roles_filename
        version_map_role_to_resources_filename  = str(version) + self.map_role_to_resources_filename

        sha256_hash = hashlib.sha256()

        with open(version_user_filename, "rb") as f:
            # Read and update hash string value in blocks of 4K
            for byte_block in iter(lambda: f.read(4096),b""):
                sha256_hash.update(byte_block)
        with open(version_rsrc_filename, "rb") as f:
            # Read and update hash string value in blocks of 4K
            for byte_block in iter(lambda: f.read(4096),b""):
                sha256_hash.update(byte_block)
        with open(version_roles_filename, "rb") as f:
            # Read and update hash string value in blocks of 4K
            for byte_block in iter(lambda: f.read(4096),b""):
                sha256_hash.update(byte_block)
        with open(version_map_user_to_roles_filename, "rb") as f:
            # Read and update hash string value in blocks of 4K
            for byte_block in iter(lambda: f.read(4096),b""):
                sha256_hash.update(byte_block)
        with open(version_map_role_to_resources_filename, "rb") as f:
            # Read and update hash string value in blocks of 4K
            for byte_block in iter(lambda: f.read(4096),b""):
                sha256_hash.update(byte_block)        

        # add version as salt
        sha256_hash.update(str(version).encode('utf-8'))        

        # add secret key as salt
        sha256_hash.update(str(self.salt).encode('utf-8'))        

        # hexdigest represents values in a print friendly way
        return sha256_hash.hexdigest()


    # remove all files, below current version
    # those are older versions of database
    # only call this after sucessull creation of
    # all files, including checksum.
    def remove_previous_version(self, version):

        files_to_delete = list()

        version_user_filename   = str(version) + self.user_filename
        files_to_delete.append(version_user_filename)

        version_rsrc_filename   = str(version) + self.rsrc_filename
        files_to_delete.append(version_rsrc_filename)

        version_roles_filename  = str(version) + self.roles_filename
        files_to_delete.append(version_roles_filename)

        version_map_user_to_roles_filename      = str(version) + self.map_user_to_roles_filename
        files_to_delete.append(version_map_user_to_roles_filename)

        version_map_role_to_resources_filename  = str(version) + self.map_role_to_resources_filename
        files_to_delete.append(version_map_role_to_resources_filename)

        version_checksum  = str(version) + ".checksum"
        files_to_delete.append(version_checksum)

        try:
            for file in files_to_delete:
                os.remove(file)
        except OSError:
            print('Failed removing older db version files. ')
        else:
            print('Previous db version removed.')

        return


    def save(self):

        current_version = self.version
        self.version = int(time.time())
        #self.version = 0

        version_user_filename   = str(self.version) + self.user_filename
        version_rsrc_filename   = str(self.version) + self.rsrc_filename
        version_roles_filename  = str(self.version) + self.roles_filename
        version_map_user_to_roles_filename      = str(self.version) + self.map_user_to_roles_filename
        version_map_role_to_resources_filename  = str(self.version) + self.map_role_to_resources_filename


        try:
            with open(version_user_filename, 'w') as fp:
                json.dump(self.users_dict, fp, indent=4, sort_keys=True)

            with open(version_rsrc_filename, 'w') as fp:
                json.dump(self.resources_dict, fp, indent=4, sort_keys=True)            

            with open(version_roles_filename, 'w') as fp:
                json.dump(self.roles_dict, fp, indent=4, sort_keys=True)            

            with open(version_map_user_to_roles_filename, 'w') as fp:
                json.dump(self.map_user_to_roles, fp, indent=4, sort_keys=True)            

            with open(version_map_role_to_resources_filename, 'w') as fp:
                json.dump(self.map_role_to_resources, fp, indent=4, sort_keys=True)            


            checksum = self.calculate_global_checksum(self.version)
            print(checksum)

            checksum_filename = str(self.version) + ".checksum"
            with open (checksum_filename, 'w') as f: f.write (checksum)

            # remove older files
            self.remove_previous_version(current_version)

        except OSError:
            print('Failed creating the files ')
        else:
            print('File created ' + checksum_filename)

        return



    
    def load_bootstrap(self):

        print("Load bootstrap")

        with open(self.user_filename) as json_file:
            self.users_dict = json.load(json_file)
        
        with open(self.rsrc_filename) as json_file:
            self.resources_dict = json.load(json_file)

        with open(self.roles_filename) as json_file:
            self.roles_dict = json.load(json_file)

        with open(self.map_user_to_roles_filename) as json_file:
            self.map_user_to_roles = json.load(json_file)

        with open(self.map_role_to_resources_filename) as json_file:
            self.map_role_to_resources = json.load(json_file)


        print("End bootstrap")




    def load(self):

        print("Load")


        # find file with checksum
        # no checksum, no party!
        file_list = glob.glob('*.checksum', recursive = False)

        if not file_list:
            print("Missing checksum file. Load bootstraped data!")
            self.load_bootstrap()
            return

        # i am only expecting only one checksum file
        # but if there are more, then use only the last(more recent).
        # this could happen if something went wrong while removing previous database version
        checksum_filename = sorted(file_list)[0] 
        
        # get version from checksum_filename
        # by spliting filename in two parts.
        # 1231231231.checksum
        version_list = checksum_filename.split(".", 1)

        if len(version_list) != 2:
            print("Wrong checksum filename. Exit immediately!")
            exit(1)

        version = int(version_list[0])

        # (cyber) version is a date
        # verify if local computer date did not go back in time
        # (or the database version date is not from the future)
        current_time = int(time.time())

        if current_time <= version:
            print("Wrong database version/time reference. It cannot be on the future. Exit immediately!")
            exit(1)


        # read checksum from checksum file
        expected_checksum = ''
        with open(checksum_filename, 'r') as checksum_file:
            expected_checksum = str(checksum_file.readlines()[0])

        if not expected_checksum:
            print("Empty checksum. Do not trust database. Exit immediately!")
            exit(1)


        current_checksum = self.calculate_global_checksum(version)

        # (CYBER) 
        # If checksum does not match, do not trust.

        if current_checksum != expected_checksum:
            print("Checksum does not match. Do not trust database. Exit immediately!")
            print('current_checksum:  ' + current_checksum)
            print('expected_checksum: ' + expected_checksum)

            exit(1)


        self.version = int(version)

        version_user_filename   = str(self.version) + self.user_filename
        version_rsrc_filename   = str(self.version) + self.rsrc_filename
        version_roles_filename  = str(self.version) + self.roles_filename
        version_map_user_to_roles_filename      = str(self.version) + self.map_user_to_roles_filename
        version_map_role_to_resources_filename  = str(self.version) + self.map_role_to_resources_filename

        with open(version_user_filename) as json_file:
            self.users_dict = json.load(json_file)
        
        with open(version_rsrc_filename) as json_file:
            self.resources_dict = json.load(json_file)

        with open(version_roles_filename) as json_file:
            self.roles_dict = json.load(json_file)

        with open(version_map_user_to_roles_filename) as json_file:
            self.map_user_to_roles = json.load(json_file)

        with open(version_map_role_to_resources_filename) as json_file:
            self.map_role_to_resources = json.load(json_file)

        print("End load")


    def set_salt(self, salt):
        self.salt = str(salt)