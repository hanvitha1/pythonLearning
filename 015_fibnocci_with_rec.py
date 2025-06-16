n = 8
a = 0
b = 1

def fib(n, a, b):
    if n == 0:
        return b
    result = a + b
    print(result, end=" ")
    return fib(n-1, b, result)

print(a, b, end=" ")
fib(n-2, a, b)