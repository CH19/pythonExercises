def arithmetic_arranger(nums, output=False):
    splitNumbers = lambda num: num.split(" ")
    newList = list(map(splitNumbers, nums))
    
    for n in range(0, len(newList)):
        result = ""
        if(len(newList[n][0]) > 4 | len(newList[n][2]) > 4):
            print("Error: max num is 4")
        if(output):
            result = makeOperation(newList[n][1], newList[n][0], newList[n][2])
        print("    {}".format(newList[n][0]))
        print("{}  {}".format(newList[n][1], newList[n][2]))
        print("------")
        print(result)
        print("")
def makeOperation(symbol, num1, num2):
    n1 = int(num1)
    n2 = int(num2)
    match symbol:
        case "+":
            return n1 + n2
        case "-":
            return n1 - n2
        case "*":
            return n1 * n2
        case "/": 
            return n1 / n2
        case _:
            return ""
# print(makeOperation("*", 2, 5))
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

