text = input("Enter the text ")
list_numbers = []

for i in text:
    if i.isdigit() and int(i) not in list_numbers:
        list_numbers.append(int(i))

print(f"the number of digits is: {len(list_numbers)}")
