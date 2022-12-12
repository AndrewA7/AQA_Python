# def for_dict(*lst):
#     return {element: element for element in lst}


def to_dict(lst):
    my_dict = {}
    for i in lst:
        my_dict[i] = i
    return my_dict

to_dict(["1", "qwe", "asd", "yrthr", "wtrwtge5hry", "rwtgheytge5tr", "twgerhetyr"])
