hard_side = int(input("enter side "))

third_triangle = hard_side
empty_space = 0

for i in range(hard_side):
    print(empty_space * " ", third_triangle * "*")
    third_triangle -= 1
    empty_space += 1

