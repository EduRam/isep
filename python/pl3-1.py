# comment
import math

myInputValueI = int(input("Input value: "))

sqrootF = math.sqrt(myInputValueI)

isSqrootInteger = sqrootF.is_integer()

if (isSqrootInteger):
     print("Value: " + str(sqrootF) + " is the perfect square of: " + str(myInputValueI)) 
else:
     print("Value: " + str(myInputValueI) + " doest not have a perfect square" ) 
