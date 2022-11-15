a = int(input("Enter a "))
b = int(input("Enter b "))
c = int(input("Enter c "))

if not(a > 10 and b > 10 and c > 10):
    print("no")
elif not(a % 3 == 0 and b % 3 == 0):
    print("no")
else:
    print("yes")

