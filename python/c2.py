import argparse
import time
import re
import inquirer
from inquirer.questions import Password
import c2_mdl
from pprint import pprint
import os
import logging

# this is a class
# but only one instance is necessary
# singleton how to ?
model = c2_mdl.Model()

# some global constants
IBAN_SIZE = 21
MAX_FIELD_CHAR_SIZE = 64
DAY_IN_SECONDS = 24 * 60 * 60
SEVEN_DAYS_IN_SECONDS = 7 * DAY_IN_SECONDS

# carefull ... we must use global keyword inside functions, 
# if we need to change this variable.
expiration_days = 30 

# salt
salt = ""



def do_action_list():
    print("List")

    questions = [
        inquirer.List(
            'action', 
            message="Select an action: ?", 
            choices=[
                ('Back','back'),
                '1. List Users',
                '2. List Resources',
                '3. List Roles',
            ], 
        ),
    ]

    while True:
        answers = inquirer.prompt(questions)
        action = answers['action']
        if action == 'back':
            break
        elif action.startswith('1'):
            pprint(model.users_dict)
        elif action.startswith('2'):
            pprint(model.resources_dict)
        elif action.startswith('3'):
            pprint(model.roles_dict)


def do_action_exit():
    print("Exit!")
    logging.info('Exit')    
    exit(0)



def passwd_check(answers, passwd):

    has_digit = False
    has_lo_letter = False
    has_up_letter = False
    has_symbol = False

    len_passwd = len(passwd)

    if len_passwd < 8 or len_passwd > 16:
        return False

    for char in passwd:
        if char.isdigit():
            has_digit = True
        if char.islower():
            has_lo_letter = True
        if char.isupper():
            has_up_letter = True
        if not char.isalnum():
            has_symbol = True

    # if all is true
    is_valid_passwd = has_digit and has_lo_letter and has_up_letter and has_symbol
    return is_valid_passwd



def nib_check(answers, anything):

    if len(anything) != IBAN_SIZE:
        return False
    if not anything.isnumeric():
        return False

    return True


def max_length(answers, anything):

    if len(anything) == 0 or len(anything) > 16:
        return False

    return True


def email_check(answers, email):

    if len(email) == 0 or len(email) > MAX_FIELD_CHAR_SIZE:
        return False

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return True
    return False



def do_action_register_users():

    questions = [
        inquirer.Text('email',          message="Email ?",          validate=email_check,),
        inquirer.Text('bank',           message="Bank account NIB (21 digits) ?",   validate=nib_check,),
        inquirer.Password('password',   message="Password ?",       validate=passwd_check,)
    ]    

    print("\n\n")
    answers = inquirer.prompt(questions)
    pprint(answers)

    model.add_user(answers['email'], answers['bank'], answers['password'])
    logging.info('Add user: ' + str(answers['email']))

    return


def do_action_delete_users():

    choices_list = list(model.users_dict.keys())
    choices_list.append('< Back')

    questions = [
        inquirer.List(
            'action', 
            message="Select user to delete: ?", 
            choices=choices_list, 
        ),
    ]

    print("\n\n")
    answers = inquirer.prompt(questions)
    action = answers['action']

    if action == '< Back':
        return   
    else:
        model.del_user(action)
        logging.info('Delete user: ' + str(action))

    return


def do_action_register_rsrc():

    questions = [
        inquirer.Text('rsrc',       message="Resource name ?",  validate=max_length,),
        inquirer.Text('url',        message="URL ?",  validate=max_length,),
    ]    

    print("\n\n")
    answers = inquirer.prompt(questions)
    #pprint(answers)

    model.add_rsrc(answers['rsrc'], answers['url'])
    logging.info('Register resource: ' + str(answers['rsrc']))

    return


def do_action_delete_rsrc():
    
    choices_list = list(model.resources_dict.keys())
    choices_list.append('< Back')

    questions = [
        inquirer.List(
            'action', 
            message="Select resource to delete: ?", 
            choices=choices_list, 
        ),
    ]

    print("\n\n")
    answers = inquirer.prompt(questions)
    action = answers['action']

    if action == '< Back':
        return   
    else:
        model.del_rsrc(action)
        logging.info('Delete resource: ' + str(action))


    return


def do_action_register_role():

    questions = [
        inquirer.Text('role',           message="Role name ?",  validate=max_length,),
        inquirer.Text('description',    message="Role description ?",  validate=max_length,),
    ]    

    print("\n\n")
    answers = inquirer.prompt(questions)
    pprint(answers)

    model.add_role(answers['role'], answers['description'])
    logging.info('Add role: ' + str(answers['role']))

    return



def do_action_delete_role():

    choices_list = list(model.roles_dict.keys())
    choices_list.append('< Back')

    questions = [
        inquirer.List(
            'action', 
            message="Select role to delete: ?", 
            choices=choices_list, 
        ),
    ]

    print("\n\n")
    answers = inquirer.prompt(questions)
    action = answers['action']

    if action == '< Back':
        return   
    else:
        model.del_role(action)
        logging.info('Delete role: ' + str(action))


    return


def do_action_save():
    model.save()

    logging.info('Save model ' + str(model.version))

    return


def init(args):
    
    logging.basicConfig(filename='trace.log', level=logging.INFO, format='%(asctime)s %(message)s')
    logging.info('Started')

    while True:
        salt = str(inquirer.password(message='Please enter secret word (1 to 8 characters)')),
        if len(salt) > 0 or len(salt) < 8:
            break

    #if args.passwd:
    #    salt = args.passwd

    logging.info('Set salt: xxxxx')

    model.set_salt(salt)


    # (cyber) should ignore to continue if more than 100000 files present
    # on current directory ?
    all_files = os.listdir()
    if len(all_files) > int(1000):
        print("Too many files found on current directory. Exit immediately!")
        logging.info("Too many files found on current directory. Exit immediately!")
        exit(1)



    #if args.demo:
    #    model.load_bootstrap()
    #else:
    #    model.load()

    model.load()

    expiration_days = 30

    return


def do_action_update_user_roles():
    print("")

    questions = [
        inquirer.List(
            'user_email', 
            message="Select user email: ", 
            choices=model.users_dict.keys(), 
        ),
    ]

    print("\n\n")
    answers = inquirer.prompt(questions)
    user_selected = answers['user_email']

    current_user_roles = model.get_user_roles(user_selected)
    all_roles = model.roles_dict.keys()

    questions_user_roles = [
        inquirer.Checkbox(
            user_selected,
            message = "Roles: ",
            choices = all_roles,
            default = current_user_roles,
        ),
    ]

    answers = inquirer.prompt(questions_user_roles)
    #pprint(answers)
    model.map_user_to_roles.update(answers)

    logging.info("Update user roles: !" + user_selected)

    return



def do_action_update_roles_resources():

    print("")

    questions = [
        inquirer.List(
            'role', 
            message="Select role: ", 
            choices=model.roles_dict.keys(), 
        ),
    ]

    print("\n\n")
    answers = inquirer.prompt(questions)
    role_selected = answers['role']

    current_role_resources = model.get_role_resources(role_selected)
    all_resources = model.resources_dict.keys()

    questions_roles = [
        inquirer.Checkbox(
            role_selected,
            message = "Resources: ",
            choices = all_resources,
            default = current_role_resources,
        ),
    ]

    answers = inquirer.prompt(questions_roles)
    #pprint(answers)
    model.map_role_to_resources.update(answers)

    logging.info("Update roles resources " + role_selected)

    return


def do_action_list_user_resources():

    print("")

    questions = [
        inquirer.List(
            'user_email', 
            message="Select user email: ", 
            choices=model.users_dict.keys(), 
        ),
    ]

    print("\n\n")
    answers = inquirer.prompt(questions)
    user_selected = answers['user_email']

    # we are going to search for all resources for a user
    # resources names will be added to a collection of type "set".
    # A "set" collection will filter for us, for duplicates.
    # python sets are defined between "{" "}"
    user_rsrcs_set = set()

    user_roles = model.get_user_roles(user_selected)
    for role in user_roles:
        for resource in model.get_role_resources(role):
            user_rsrcs_set.add(resource + " - " + model.resources_dict[resource])


    is_empty = (len(user_rsrcs_set) == 0)
    if is_empty:
        print("\n" + "No resources found!")
    else:
        # this print construction
        # will print each element on the set
        # one element per line
        print("\n".join(user_rsrcs_set))

    logging.info("List user resources " + user_selected)

    return



def do_action_list_export():

    users_with_passwd_about_to_expire_list = list()

    for user in model.users_dict:

        user_params_list = model.users_dict[user]

        # 0 is banck account number (int)
        # 1 is the passwd (anything)
        # 2 is the last modified epoch date passwd has changed (int)
        user_passwd_last_modified_time_sec = user_params_list[2]

        # get epoch date that passwd will expire (in seconds)
        #       last_modified_time_sec is epoch
        #       EXPIRATION_DAYS_IN_SECONDS is relative
        passwd_expiration_date_in_seconds = int(user_passwd_last_modified_time_sec) + (int(expiration_days) * DAY_IN_SECONDS)
        
        # current epoch time in seconds
        current_time_in_sec = int(time.time())

        # epcoh date 7 days in the future
        future_seven_day_time_in_sec = current_time_in_sec + SEVEN_DAYS_IN_SECONDS

        # compare future date with passwd already expired
        #if True:
        if passwd_expiration_date_in_seconds < future_seven_day_time_in_sec:
            users_with_passwd_about_to_expire_list.append(user)

    # end for user in model.users_dict:

    if len(users_with_passwd_about_to_expire_list) == 0:
        print("No users have passwd about to expire in the next 7 days.")
        return

    # mode "wt" is:
    # w - file to write
    # t - in text mode (but already is the default)
    # (CYBER): shows all parameters be explicit ?
    with open('passwd_about_to_expire.txt', mode='wt', encoding='utf-8') as myfile:
        myfile.write('\n'.join(users_with_passwd_about_to_expire_list))

    logging.info("Export users to file passwd_about_to_expire.txt")

    return
    

# experiration day must be
# a number
# and between 1 and 120 
def validate_expiration_days(answers, current):

    if not current.isnumeric() or int(current) <= 0 or int(current) > 120:
        raise errors.ValidationError('', reason='Invalid day! Must be between 1 and 120.')

    return True


def do_action_change_expiration():
    global expiration_days
    print("Current number of days to expire: {}".format(expiration_days))

    questions = [
        inquirer.Text('expiration_days', 
            message="New passwd expiration days: ",
            validate=validate_expiration_days),
    ]
    answers = inquirer.prompt(questions)
    pprint(answers)
    expiration_days = answers['expiration_days']

    logging.info("Change expiration to " + str(expiration_days))

    return



def main(args):

    init(args)

    questions = [
        inquirer.List(
            'action', 
            message="Select an action: ?", 
            choices=[
                ('Save',                            'save'),
                ('List all',                        'list_all'),
                ('Register User',                   'register_users'),
                ('Delete User',                     'delete_users'),
                ('Register Resource',               'register_rsrc'),
                ('Delete Resource',                 'delete_rsrc'),
                ('Register Role',                   'register_role'),
                ('Delete Role',                     'delete_role'),
                ('Associate roles to User',         'update_user_roles'),
                ('Add resources to roles',          'update_roles_resources'),
                ('List user resources',             'list_user_resources'),
                ('Export emails/users to expire',   'export'),
                ('Change passwd expiration',        'change_expiration'),                
                ('Exit', 'exit'),
            ], 
        ),
    ]

    while True:

        print("\n\n")
        answers = inquirer.prompt(questions)
        action = answers['action']

        logging.info("Selected action " + str(action))

        if action == 'exit':
            do_action_exit()
        if action == 'save':
            do_action_save()
        elif action.startswith('list_all'):
            do_action_list()
        elif action.startswith('register_users'):
            do_action_register_users()
        elif action.startswith('delete_users'):
            do_action_delete_users()
        elif action.startswith('register_rsrc'):
            do_action_register_rsrc()
        elif action.startswith('delete_rsrc'):
            do_action_delete_rsrc()
        elif action.startswith('register_role'):
            do_action_register_role()
        elif action.startswith('delete_role'):
            do_action_delete_role()
        elif action.startswith('update_user_roles'):
            do_action_update_user_roles()
        elif action.startswith('update_roles_resources'):
            do_action_update_roles_resources()
        elif action.startswith('list_user_resources'):
            do_action_list_user_resources()
        elif action.startswith('export'):
            do_action_list_export()
        elif action.startswith('change_expiration'):
            do_action_change_expiration()
        else:
            print("Not implemented yet")
            exit(1)


# idiomatic main entry point
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--passwd", help = "Password")
    parser.add_argument("demo", nargs='?')
    args = parser.parse_args()
    main(args)

