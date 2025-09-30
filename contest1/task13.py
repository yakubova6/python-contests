data = input().split()

low = int(data[0])
high = int(data[1])

counter_odd = 0

for i in range (low, high+1):
    if(i % 2 == 0):
        continue
    else:
        counter_odd += 1

print(counter_odd)