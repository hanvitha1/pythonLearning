# def fib(n):
#     L = [1, 1]
#     if n == 1:
#         return L[:1]
#     elif n == 2:
#         return L[:2]
#     else:
#         while (n - 2) > 0:
#             # print (L)
#             L.append(L[-1] + L[-2])
#             n -= 1
#         return L
# for i in range(1, 10):
#     print(i, fib(i))

n=10
a=0
b=1
i=0
while i < n:
    print(a, end = " ")
    temp = b
    b=a+b
    a=temp
    i = i + 1


# a = 0
# b = 1
# n = 6
#
# def fib(n, a, b):
#     if n == 1:
#         return b
#     result = a + b
#     print(result, end=" ")
#     return fib(n-1, b, result)
#
# print(a, b, end=" ")
# fib(n-2, a, b)












