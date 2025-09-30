data = input()

reversed_string = ''.join(reversed(data))

if (data.lower() != reversed_string.lower()):
    print("NO")
else:
    print("YES")