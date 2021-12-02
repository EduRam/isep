#

myInputName = input("Input name: ")
#myInputName = "raceacar"


# i = 0
# for myLeter in myInputName:
#       i = i + 1

# for i in range(len(myInputName))
#       myLetter = myInputName[i]

isPalindrome = True
endLen = len(myInputName)-1
for index, myLetter in enumerate(myInputName):

    endIndex = endLen - index;
    if (index > endIndex):
        print(str("Reached midle at index: {}").format(index))
        break

    endLetter = myInputName[endIndex]
    print(str("Start letter:{}  End letter:{}").format(myLetter, endLetter) ) 

    if (myLetter != endLetter):
        print(str("""\
ERROR: Mismatch letter: {} with {}
at index {} and end index: {} 
        """).format(myLetter, endLetter, index, endIndex))
        isPalindrome = False
        break


if (isPalindrome):
    print("Word " + str(myInputName) + " is palindrome.")



    

