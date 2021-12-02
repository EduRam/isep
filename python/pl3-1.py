# comment
import math

my_input_value = int(input("Input value: "))

sqroot = math.sqrt(my_input_value)

is_sqroot = sqroot.is_integer()

if (is_sqroot):
     msg = "Value: {} is the perfect square of: {} "
     print(msg.format(sqroot, my_input_value)) 
else:
     print("Value: " + str(my_input_value) + " doest not have a perfect square" ) 
