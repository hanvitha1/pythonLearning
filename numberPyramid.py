row = 5
num = 10
for i in range(row):
    print("   " * (row-i-1), end=" ")
    for j in range (((i+1)*2) - 1):
        print(num, end=" ")
        num += 1
    print()
for i in range(row-2,-1,-1):
    print("   " * (row-i-1), end=" ")
    for j in range (((i+1)*2) - 1):
        print(num, end=" ")
        num += 1
    print()



