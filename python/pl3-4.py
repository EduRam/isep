#
from statistics import mean, median, stdev, variance

my_array = [1, 2, 3, 4, 5]

def positiveNumber(list):
    posNumber = 0
    negNumber = 0
    for number in list:
        if number > 0:
            posNumber += 1
        else:
            negNumber += 1 
    return (posNumber, negNumber)



print("Max   : {}".format(max(my_array)))
print("Min   : {}".format(min(my_array)))
print("Mean  : {}".format(mean(my_array)))
print("Median: {}".format(median(my_array)))
print("Varian: {}".format(variance(my_array)))

tuple = positiveNumber(my_array)
print("PosNum: {}".format(tuple[0]))
print("NegNum: {}".format(tuple[1]))

