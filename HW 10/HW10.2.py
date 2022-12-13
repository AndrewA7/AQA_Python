
def to_dict(lst):
    try:
        my_dict = {i: i for i in lst}
        return my_dict
    except TypeError:
        print("Type error")
        exit()



aaa = to_dict(["1", "asd", 23, "yrthr", "wtrwtge5hry", "rwtgheytge5tr", "twgerhetyr"])

print(aaa)

