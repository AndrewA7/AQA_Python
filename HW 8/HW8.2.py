permissions_dict = {"read": "R", "write": "W", "execute": "X"}
N = 0
M = 0
try:
    N = int(input("how many files do you need? "))
except ValueError:
    print("you entered incorrect values")

file_permissions = {}

for i in range(N):
    file, *permissions = input("enter the file name and permissions ").split()
    file_permissions[file] = set(permissions)


try:
    M = int(input("How many operation you need? "))
except ValueError:
    print("you entered incorrect values")

try:
    for i in range(M):
        operation, file = input("Enter the operation and file ").split()
        if permissions_dict[operation] in file_permissions[file]:
            print("OK")
        else:
            print("Access denied")
except KeyError:
    print("incorrectly entered data ")