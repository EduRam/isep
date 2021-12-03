import secrets

random_value = secrets.randbelow(10)
user_tries = 0
is_to_retry = True

while (is_to_retry):
    
    guess = int(input("Guess number: "))

    if (guess < random_value):
        print("Value is too low")
    elif (guess > random_value):
        print("Value is too high")
    else:
        print("Bingo!")
        is_to_retry = False
    
    user_tries += 1


print("Number of tries was: {}".format(user_tries))

