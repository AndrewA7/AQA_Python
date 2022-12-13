my_list = (1, 'qwe', True, 20)

def change(lst):
    new_list = list(lst)
    begining = new_list.pop()
    ending = new_list.pop(0)
    new_list.append(ending)
    new_list.insert(0, begining)
    print(new_list)
    return new_list



change([1, 'qwe', True, 20])
change([23,  45, "wergwr", "wfre"])
