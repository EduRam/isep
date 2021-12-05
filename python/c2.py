import inquirer
import c2_mdl
from pprint import pprint

model = c2_mdl.Model()

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
            print(model.user_dict)
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
    print("""
        Missing validation:
        1. Is a well formatted email
        2. Email already existent.
    """)
    return True


def do_action_register_users():

    questions = [
        inquirer.Text('email',      message="Email ?", validate=email_check,),
        inquirer.Text('bank',       message="Bank account ?"),
        inquirer.Text('password',   message="Password ?", validate=passwd_check,)
    ]    

    answers = inquirer.prompt(questions)
    pprint(answers)

    model.add_user(answers['email'], answers['bank'], answers['password'])

    return



def do_action_save():
    model.save()
    return


def do_action_delete_users():

    questions = [
        inquirer.List(
            'action', 
            message="Select user to delete: ?", 
            choices=model.user_dict.keys(), 
        ),
    ]

    answers = inquirer.prompt(questions)
    action = answers['action']
    model.del_user(action)

    return


def init():
    print("init")
    model.load_bootstrap()
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
                '1. Register Users', 
                '2. Delete Users', 
                '3. Register Resources',
                '4. Delete Resources',
                '5. Register Roles',
                '6. Delete Roles',
                'XXX. Faltam as seguintes',
                'YYY. Verificar a possiblidade de menus dentro de menus',
                'Exit',
            ], 
        ),
    ]

    while True:

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
        else:
            print("Not implemented yet")
            exit(1)


# classic main entry point
if __name__ == '__main__':
    main()



