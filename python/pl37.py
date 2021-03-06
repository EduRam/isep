

def passwd_check(passwd):

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

    # alternative implemetnation
    #if (any(c.islower() for c in passwd)
        #and any(c.isupper() for c in passwd)
        #and any(c in string.punctuation for c in passwd)
        #and any(c.isdigit() for c in passwd)):
        #break


# The following main() and == "__main__"
# is a well know python recipe.
# It permits running this script standalone
# or permits calling function passwd_check() from another script.

def main():
    passwd = input("Passwd: ")
    result = passwd_check(passwd)

    if (result):
        print("Passwd is Ok!")
    else:
        print("Passwd does not follow rules. Exit!")



if __name__ == "__main__":
    main()


