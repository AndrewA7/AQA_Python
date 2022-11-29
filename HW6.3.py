input_string = input("Enter something ")


if input_string.startswith("abc"):
    input_string_new = input_string.replace("abc", "www", 1)
    print(input_string_new)
else:
    input_string_new = input_string + " zzz"
    print(input_string_new)
