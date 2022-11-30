A = input("Enter numerics using comas ")
numeric_list = []
str_list = A.split(",")
C = []

for digit in str_list:
    numeric_list.append(int(digit))
    if int(digit) > 5:
        C.append(int(digit))

print(C)
