import secrets
import string

def request_passwd():

    # Source:
    # https://docs.python.org/3/library/secrets.html#recipes-and-best-practices
    alphabet = string.ascii_letters + string.digits + string.punctuation

    

    while True:
        passwd = ''.join(secrets.choice(alphabet) for i in range(10))
        if (any(c.islower() for c in passwd)
                and any(c.isupper() for c in passwd)
                and any(c in string.punctuation for c in passwd)
                and sum(c.isdigit() for c in passwd) >= 1):
            break

    return passwd


passwd = request_passwd()
print(passwd)