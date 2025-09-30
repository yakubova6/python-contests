n = int(input())
existing_users = set(input().split())

k = int(input())
applications = input().split()

new_users = set()
for user in applications:
    if user not in existing_users:
        new_users.add(user)

result = sorted(new_users)
print(" ".join(result))