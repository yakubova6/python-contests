amount = float(input())

counter_5000 = int(amount // 5000)
amount = amount % 5000

counter_1000 = int(amount // 1000)
amount = amount % 1000

counter_500 = int(amount // 500)
amount = amount % 500

counter_200 = int(amount // 200)
amount = amount % 200

counter_100 = int(amount // 100)
amount = amount % 100

print(f"{counter_5000} {counter_1000} {counter_500} {counter_200} {counter_100}")
