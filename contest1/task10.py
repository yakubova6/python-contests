data = input().split()

number1 = int(data[0])
number2 = int(data[1])
number3 = int(data[2])

if number1 > number2:
    if number1 > number3:
        print(number1)
    else:
        print(number3)
else:
    if number2 > number3:
        print(number2)
    else:
        print(number3)
