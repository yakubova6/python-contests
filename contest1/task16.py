sequence_length = int(input())
data = input().split()

temperatures = []
for i in data:
    temperatures.append(int(i))

result = []


for i in range(sequence_length):
    if i == 0 or i == sequence_length - 1:
        result.append(temperatures[i])
    else:
        average_value = (temperatures[i - 1] + temperatures[i] + temperatures[i + 1]) / 3
        result.append(average_value)

for num in result:
    print(float(num), end=" ")