def f(n):
    if n>100:
        return None
    else:
        print(n, end = " ")
        f(n+1)
f(1)