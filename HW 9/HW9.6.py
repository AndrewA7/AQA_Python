with open("file.txt", "r") as file:
    sum_file = file.read().split()

number_list = []
for i in sum_file:
    number_list.append(float(i))

print(sum(number_list))
