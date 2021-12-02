#

my_input_name = input("Input name: ")
#my_input_name = "raceacar"


# i = 0
# for myLeter in myInputName:
#       i = i + 1

# for i in range(len(myInputName))
#       myLetter = myInputName[i]

is_palindrome = True
end_length = len(my_input_name)-1
for index, my_letter in enumerate(my_input_name):

    end_index = end_length - index;
    if (index > end_index):
        print(str("Reached midle at index: {}").format(index))
        break

    end_letter = my_input_name[end_index]
    print(str("Start letter:{}  End letter:{}").format(my_letter, end_letter) ) 

    if (my_letter != end_letter):
        print(str("""\
ERROR: Mismatch letter: {} with {}
at index {} and end index: {} 
        """).format(my_letter, end_letter, index, end_index))
        is_palindrome = False
        break


if (is_palindrome):
    print("Word " + str(my_input_name) + " is palindrome.")
else:
    print("Word " + str(my_input_name) + " is not palindrome.")



    

