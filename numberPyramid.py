row = 5
num = 189
for i in range(row):
    print(" " * ((row-i-1)*4), end=" ")
    for j in range (((i+1)*2) - 1):
        print(num, end=" ")
        num += 1
    print("\n")



