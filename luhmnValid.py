def is_luhn_valid(cc): #Parametro ejemplo 5256783371567695

    num = map(int, str(cc))
    return sum(num[::-2] + [sum(divmod(d * 2, 10)) for d in num[-2::-2]]) % 10 == 0

# print(is_luhn_valid("4324i35345"))
num = 1000
print(num % 10)