another_hard_side = int(input("enter side "))

another_third_triangle = 0
another_empty_space = another_hard_side

for i in range(another_hard_side):
    another_third_triangle += 1
    another_empty_space -= 1
    print(another_empty_space * " ", another_third_triangle * "*")