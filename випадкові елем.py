import random

p = []

for i in range(5):
    element = input("Введіть елемент: ")
    p.append(element)

chosen = random.choice(p)
print("Випадковий вибір:", chosen)
