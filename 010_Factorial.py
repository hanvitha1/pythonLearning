# def f(n):
#     fact = 1
#     for i in range (1, n+1):
#         fact = fact * i
#     print(fact)
#     return fact
# n = 5
# res = f(n)


def fact(n):
    # fact = 1
    if n==0:
        return 1
    else:
        return n * fact(n-1)

n=5
res = fact(n)
print(res)


