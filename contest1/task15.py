data = input().split(';')

numbers = []
amounts = 0

for i in data:
    if(i == ''):
        continue
    numbers.append(int(i))

for number in numbers:
        amounts += number

print(amounts / len(numbers))