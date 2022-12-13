def sum_range(start, end):
    if start > end:
        end, start = start, end
    number_list = [i for i in range(start, end + 1)]
    return sum(number_list)


print(sum_range(0, 2))

