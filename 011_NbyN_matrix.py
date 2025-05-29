size = int(input("enter the size of matrix: "))
n = size * size
num = 0
l1 = []
l2 = []
for i in range(1, n + 1):
    num += 1
    print(num, end=" ")
    l2.append(num)
    if num % size == 0:
        l1.append(l2)
        l2=[]
        print()
print(l1)





