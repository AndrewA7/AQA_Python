import json
import os
import platform



dict1 = {'one': '1', 'two': '2', 'three': '3'}

dict2 = {v: k for k, v in dict1.items()}

with open("answers.txt", "w") as new_file:
    new_file.write(str(dict2))

with open("test.txt", "a") as new_file:
    if platform.system() == "Darwin":
        os.rename("test.txt", "mac.txt")
    elif platform.system() == "Windows":
        os.rename("test.txt", "windows.txt")
    elif platform.system() == "Linux":
        os.rename("test.txt", "linux.txt")
    else:
        print("I don't know what do you use...")


def my_generator(start, finish):
    if start > finish:
        for i in range(finish, start + 1, 1):
            yield i
    else:
        for i in range(start, finish + 1, 1):
            yield i


my_gen = my_generator(1, -3)
for i in my_gen:
    print(i)


class A:
    name = "A"
    def __init__(self):
        self.name = "another A"


class B(A):
    name = "B"


class C(B):
    name = "C"
    def __init__(self):
        super().__init__()



print(A.name)
print(B.name)
print(C.name)
print(A().name)
print(C().name)


with open("answers.txt", "w") as created_before_file:
    created_before_file.write("*args і **kwargs - загальні ідіоми. що дозволяють передати у функцію \n "
                              "довільне число аргументів. *args повертає кортеж з переданими значеннями, \n"
                              "**kwargs повертає словник. *args і **kwargs повертають тільки дані,\n "
                              "які не були визначені раніше")


def some_arg_function(*args):
    print(args)


some_arg_function("qwe", True, 123, 11.4)


def some_kwarg_function(**kwargs):
    print(kwargs)


some_kwarg_function(a="qwe", b=True, c=123, d=11.4)

data = {"ID": "QQQ"}
with open("json_file.json", "r+") as json_file:
    new_json_file = json.loads(json_file.read())

new_json_file["glossary"]["GlossDiv"]["GlossList"]["GlossEntry"]["ID"] = "La-la-la"

with open("json_file.json", "w") as json_file:
    json.dump(new_json_file, json_file)
