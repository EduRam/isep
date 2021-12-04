from pl37 import *

import secrets
import string


def request_passwd():

    # Source:
    # https://docs.python.org/3/library/secrets.html#recipes-and-best-practices
    alphabet = string.ascii_letters + string.digits + string.punctuation

    while True:

        #passwd = ''.join(secrets.choice(alphabet) for i in range(10))

        # the following examples is to test if previous function is
        # really working for other cases
        passwd = ''.join(secrets.choice(alphabet) for i in range(8))


        if passwd_check(passwd):
            break
        else:
            print("Not valid pass {}. Generate a new one!".format(passwd))

    return passwd


passwd = request_passwd()
print(passwd)