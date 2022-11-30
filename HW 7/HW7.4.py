a = int(input("Enter N "))
list_of_digits = []


while a != 0:
    print(f"We need {a} numerics.")
    digit = int(input("Enter 1 number "))
    list_of_digits.append(digit)
    a -= 1

list_of_digits.reverse()

print(list_of_digits)
