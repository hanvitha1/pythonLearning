string = "hanvitha"
flag = True

for i in range(len(string)):
    flag = True
    for j in range(len(string)):
        if i != j and string[i] == string[j]:
            flag = False
            break
    if flag == True:
        print("first non repeating char", string[i])
        break
else:
    print("no non repeating char")




