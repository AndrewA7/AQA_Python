a = 10
list_of_digits = []
b = 0

while a != 0:
    print(f"We need {a} numerics.")
    digit = int(input("Enter 1 number "))
    list_of_digits.append(digit)
    a -= 1

numeric = int(input("what number to find? "))

for i in list_of_digits:
    if i is numeric:
        b += 1

print(f"your number meets {b} times")
print(list_of_digits)