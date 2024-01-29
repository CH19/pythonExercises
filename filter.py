condition = lambda num: num > 18
formaterNum = lambda num: "{} ages".format(num)
ages = [12,43,24,56,7,67,54,3,45,28,19,34,23,54,32,12,56]

newAges = list(filter(condition, ages))
dataAges = list(map(formaterNum, ages))
print(newAges)
print(dataAges)