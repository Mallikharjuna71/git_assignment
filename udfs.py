def add(*n):
    total = 0
    for i in n:
        total += i
    return total

print(add(1, 2, 3))

def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)