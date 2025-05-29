row = 5
num = 100
n= ((row)*row)+((row-1)*(row-1))
print(n)
print(num + (n-1))
print(len (str(n)))
cal = len (str((num)+(n-1)))

# for i in range(row):
#     for j in range (((i+1)*2) - 1):
#         num += 1
# for i in range(row-2,-1,-1):
#     for j in range (((i+1)*2) - 1):
#         num += 1
# cal = len(str(num))

for i in range(row):
    print(" " * (row-i-1)* (cal+1), end=" ")
    for j in range (((i+1)*2) - 1):
        print("0"*(cal-len(str(num))), end= "")
        print(num, end=" ")
        num += 1
    print()
for i in range(row-2,-1,-1):
    print(" " * (row-i-1) * (cal + 1), end=" ")
    for j in range (((i+1)*2) - 1):
        print(" "*(cal-len(str(num))), end= "")
        print(num, end=" ")
        num += 1
    print()




