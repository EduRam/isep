#

myInputName = input("Input name: ")

myDict = dict()

for myLetter in myInputName:
    print(myLetter)

    if myLetter in myDict:

        frequencyValue = myDict[myLetter] 
        myDict[myLetter] = frequencyValue + 1
        
    else:
        myDict[myLetter] = 1

print(myDict)




