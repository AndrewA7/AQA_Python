def sum_range(start, end):
    if start > end:
        end, start = start, end
    number_list = []
    for i in range(start, end + 1):
        number_list.append(i)
    return sum(number_list)


print(sum_range(0, 3))

