import re
import inquirer
import c2_mdl
from pprint import pprint

model = c2_mdl.Model()

MAX_FIELD_CHAR_SIZE = 64

def do_action_list():
    print("List")

    questions = [
        inquirer.List(
            'action', 
            message="Select an action: ?", 
            choices=[
                'Back',
                '1. List Users',
                '2. List Resources',
                '3. List Roles',
            ], 
        ),
    ]

    while True:
        answers = inquirer.prompt(questions)
        action = answers['action']
        if action == 'Back':
            break
        elif action.startswith('1'):
            print(model.users_dict)
        elif action.startswith('2'):
            print(model.resources_dict)
        elif action.startswith('3'):
            print(model.roles_dict)


def do_action_exit():
    print("Exit!")
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


def email_check(answers, email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return True
    return False




def do_action_register_users():

    questions = [
        inquirer.Text('email',      message="Email ?", validate=email_check,),
        inquirer.Text('bank',       message="Bank account ?", validate=email_check,),
        inquirer.Password('password',   message="Password ?", validate=passwd_check,)
    ]    

    print("\n\n")
    answers = inquirer.prompt(questions)
    pprint(answers)

    model.add_user(answers['email'], answers['bank'], answers['password'])

    return


def do_action_delete_users():

    questions = [
        inquirer.List(
            'action', 
            message="Select user to delete: ?", 
            choices=model.users_dict.keys(), 
        ),
    ]

    print("\n\n")
    answers = inquirer.prompt(questions)
    action = answers['action']
    model.del_user(action)

    return


def do_action_register_rsrc():

    questions = [
        inquirer.Text('rsrc',       message="Resource name ?"),
        inquirer.Text('url',        message="URL ?"),
    ]    

    print("\n\n")
    answers = inquirer.prompt(questions)
    pprint(answers)

    model.add_rsrc(answers['rsrc'], answers['url'])

    return


def do_action_delete_rsrc():

    questions = [
        inquirer.List(
            'action', 
            message="Select resource to delete: ?", 
            choices=model.resource_dict.keys(), 
        ),
    ]

    print("\n\n")
    answers = inquirer.prompt(questions)
    action = answers['action']
    model.del_rsrc(action)

    return


def do_action_register_role():

    questions = [
        inquirer.Text('role',           message="Role name ?"),
        inquirer.Text('description',    message="Role description ?"),
    ]    

    print("\n\n")
    answers = inquirer.prompt(questions)
    pprint(answers)

    model.add_role(answers['role'], answers['description'])

    return



def do_action_delete_role():

    questions = [
        inquirer.List(
            'action', 
            message="Select role to delete: ?", 
            choices=model.roles_dict.keys(), 
        ),
    ]

    print("\n\n")
    answers = inquirer.prompt(questions)
    action = answers['action']
    model.del_role(action)

    return


def do_action_save():
    model.save()
    return


def init():
    print("init")
    model.load_bootstrap()
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
    all_roles = model.roles_dict.keys();

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
    all_resources = model.resources_dict.keys();

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
    return



def main():

    init()

    questions = [
        inquirer.List(
            'action', 
            message="Select an action: ?", 
            choices=[
                'Save',
                '0. List all',
                '1. Register User', 
                '2. Delete User', 
                '3. Register Resource',
                '4. Delete Resource',
                '5. Register Role',
                '6. Delete Role',
                '7. Associate roles to User',
                '8. Add resources to roles',
                '9. XXX Export emails/users about to expire ',
                'Exit',
            ], 
        ),
    ]

    while True:

        print("\n\n")
        answers = inquirer.prompt(questions)
        action = answers['action']
        if action == 'Exit':
            do_action_exit()
        if action == 'Save':
            do_action_save()
        elif action.startswith('0'):
            do_action_list()
        elif action.startswith('1'):
            do_action_register_users()
        elif action.startswith('2'):
            do_action_delete_users()
        elif action.startswith('3'):
            do_action_register_rsrc()
        elif action.startswith('4'):
            do_action_delete_rsrc()
        elif action.startswith('5'):
            do_action_register_role()
        elif action.startswith('6'):
            do_action_delete_role()
        elif action.startswith('7'):
            do_action_update_user_roles()
        elif action.startswith('8'):
            do_action_update_roles_resources()
        else:
            print("Not implemented yet")
            exit(1)


# classic main entry point
if __name__ == '__main__':
    main()



