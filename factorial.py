def f(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact
n = 5
res = f(n)
print(res)
