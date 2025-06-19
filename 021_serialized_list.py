lis = [2,4,3,[4,2,8],6,7,[9,3,0,1],2]
lis1 = [ ]
for i in lis:
    if type(i) == list:
        lis1.extend(i)
    else:
        lis1.append(i)
print(lis1)