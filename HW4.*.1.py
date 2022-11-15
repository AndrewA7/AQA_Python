print("choose the number between 100 and 999")

number = int(input("enter the number "))
if not 99 < number < 1000:
    print("incorrect value")
    exit()

a = number // 100
b = number // 10 % 10
c = number % 10
reversed_number = c*100 + b*10 + a

print(f"revert number is {reversed_number}")
