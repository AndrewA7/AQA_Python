text = input("Enter the text ")

new_text = text

for i in text:
    if i.isdigit():
        new_text = new_text.replace(i, "")


print(new_text)
