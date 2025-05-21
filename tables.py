# n = int(input("enter n value: "))
def table(n):
        i=1
        while i<=10:
                multiple = n*i
                print(f"{n} * {i} = {multiple}")
                i+=1
table(6)