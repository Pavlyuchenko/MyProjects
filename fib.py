# Trying to make O(n) Fibonnaci sequence

def fib(n):
    if n == 1 or n == 2:
        return 1
    elif n < 1:
        return None

    temp1 = 1
    temp2 = 1

    for i in range(2, n):
        temp1, temp2 = temp2, temp1 + temp2

    return temp2


print(fib(10000))