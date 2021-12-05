import inquirer
import c2_mdl


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


def init():
    print("init")
    model.load_bootstrap()


def main():

    init()

    questions = [
        inquirer.List(
            'action', 
            message="Select an action: ?", 
            choices=[
                'Exit',
                '0. List all',
                '1. Register Users', 
                '2. Delete Users', 
                '3. Register Resources',
                '4. Delete Resources',
                '5. Register Roles',
                '6. Delete Roles',
                'XXX. Faltam as seguintes',
                'YYY. Verificar a possiblidade de menus dentro de menus',
            ], 
        ),
    ]

    while True:

        answers = inquirer.prompt(questions)
        print(answers)

        action = answers['action']
        if action == 'Exit':
            do_action_exit()
        elif action.startswith('0'):
            do_action_list()
        else:
            print("Not implemented yet")
            exit(1)


# classic main entry point
if __name__ == '__main__':
    main()



