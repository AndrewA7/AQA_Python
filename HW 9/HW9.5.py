with open("text5.txt", "r") as text:
    text_new = text.read()


words = 0
for i in text_new.split():
    if i.isalpha():
        words += 1

print(f"this text has {words} words")
