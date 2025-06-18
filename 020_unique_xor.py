#unique elements in list using xor
s = [1,2,3,1,2]
l = []
for i in range (len(s)):
    count = 0
    for j in range (len(s)):
        if i != j and (s[i] ^ s[j]) == 0:
            count += 1
    if count == 0:
        l.append(s[i])
print(l)

# #repeating elements in list using xor
# s = [1,2,3,4,1,2]
# l = []
# for i in range (len(s)):
#     count = 0
#     for j in range (len(s)):
#         if i != j and (s[i] ^ s[j]) == 0:
#             count += 1
#     if count > 0 and s[i] not in l:
#         l.append(s[i])
# print(l)
