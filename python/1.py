import inquirer


def do_action_list():
    print("List")


def do_action_exit():
    print("Exit!")
    exit(0)


def main():

    while True:
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



