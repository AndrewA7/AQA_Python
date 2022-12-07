with open("random_text.txt", "r") as random_text:
    text = random_text.read()


my_dict = {}.fromkeys(text.split(), 0)

for i in text.split():
    my_dict[i] += 1

my_sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))


result = []
for i in list(my_sorted_dict.keys())[0:5]:
    result.append((i, my_sorted_dict[i]))
print(result)

