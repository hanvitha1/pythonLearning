#unique elements in array using dictionary
s = [1, 2, 3, 4, 5, 3, 4, 1]
d = {}
for i in range(len(s)):
    if s[i] in d:
        d[s[i]] += 1
    else:
        d[s[i]] = 1

for j in d:
    if d[j] == 1:
        print(j, end=" ")
