#

my_input_name = input("Input name: ")

my_map = dict()

for my_letter in my_input_name:
    print(my_letter)

    if my_letter in my_map:

        frequency = my_map[my_letter] 
        my_map[my_letter] = frequency + 1
        
    else:
        my_map[my_letter] = 1

print(my_map)




