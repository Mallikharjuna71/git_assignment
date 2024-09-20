def add(*n):
    total = 0
    for i in n:
        total += i
    return total

print(add(1, 2, 3))