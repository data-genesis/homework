import random
rock = (random.randint(3, 20))

pairs = []
for n1 in range(1, rock):
    for n2 in range(n1 + 1, rock):
        if  rock % (n1 + n2) == 0:
            pairs.append(f"{n1}{n2}")
result = ''.join(pairs)
print(rock, result)
