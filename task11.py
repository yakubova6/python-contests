data = input().split()

point_a = int(data[0])
point_b = int(data[1])
point_c = int(data[2])

diff_a_and_b = abs(point_a - point_b)
diff_a_and_c = abs(point_a - point_c)

if diff_a_and_b > diff_a_and_c:
    print(f"C {diff_a_and_c}")
else:
    print(f"B {diff_a_and_b}")