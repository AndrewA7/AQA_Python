def is_power_of_two(number):
    if number == 1:
        return "yes"
    elif 1 < number < 2:
        return "no"
    else:
        return is_power_of_two(number / 2)


is_power_of_two(256)
is_power_of_two(125)
