iterations = input("enter the number of iterations ")
while not iterations.isdigit():
    print("incorrect value")
    iterations = input("enter the number of iterations ")

test = []

for i in range(int(iterations)):
    number = input("enter number ")
    while number.isalpha():
        print("incorrect value")
        number = input("enter number ")
    with open("numbers.txt", "a") as numbers:
        numbers.write(number + " ")


