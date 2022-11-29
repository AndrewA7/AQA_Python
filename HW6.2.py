char = [",", ".", "?", "!", "(", ")"] #Список може бути розширено

input_text = input("Enter the text ")
what_to_find = input("Enter what to find ")
text = input_text

for sign in char:
    text = text.replace(sign, "")

text_list = text.split()
print(text)

if what_to_find in text_list:
    print("YES")
else:
    print("NO")


