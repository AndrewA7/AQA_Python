N = int(input("Enter N "))
A = []


for i in range(N):
    values = int(input("enter new value "))
    A.append(values)


max_number = A[0]
min_number = max_number

for maximum in A:
    if maximum >= max_number:
        max_number = maximum

for minimum in A:
    if minimum < min_number:
        min_number = minimum

print(f"max value is {max_number}, min value is {min_number}")