import random
for i in range(100):
    a = random.randint(0, 1000)
    with open("random_numbers.txt", "a") as random_numbers:
        random_numbers.write(str(a) + "\n")
