with open("text1.txt", "r") as text:
    string_text = text.read()


numbers = []

for i in string_text.split():
    if i.replace("-", "").replace(".", "", 1).isdigit():
        numbers.append(i)


print(numbers)

