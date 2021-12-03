import secrets
import sys


# copy past from
# https://stackoverflow.com/questions/3041986/apt-command-line-interface-like-yes-no-input
def query_yes_no(question, default="yes"):
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")


random_value = secrets.randbelow(10)
is_to_repeat = True


while (is_to_repeat):

    has_found = False
    user_tries = 0

    while (not has_found):

        guess = int(input("Guess number: "))

        if (guess < random_value):
            print("Value is too low")
        elif (guess > random_value):
            print("Value is too high")
        else:
            print("Bingo!")
            has_found = True

        user_tries += 1

    print("Number of tries was: {}".format(user_tries))

    is_to_repeat = bool(query_yes_no("Try again ?", default="yes"))

print("End!")