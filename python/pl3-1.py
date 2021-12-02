# comment
import math

myInputValueI = int(input("Input value: "))

sqrootF = math.sqrt(myInputValueI)

isSqrootInteger = sqrootF.is_integer()

if (isSqrootInteger):
     msg = "Value: {} is the perfect square of: {} "
     print(msg.format(sqrootF, myInputValueI)) 
else:
     print("Value: " + str(myInputValueI) + " doest not have a perfect square" ) 
