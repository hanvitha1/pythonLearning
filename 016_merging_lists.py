# a = [1, 2, 3, 5, 7]
# b = [2, 3, 4, 6, 8]
# c = a + b
# merged = []
# for i in c:
#     if i not in merged:
#         merged.append(i)
#
# for i in range(len(merged)):
#     for j in range(i + 1, len(merged)):
#         print(i)
#         if merged[i] > merged[j]:
#             merged[i], merged[j] = merged[j], merged[i]
#
# print(merged)


a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

merged = []

for i in a:
    if i not in merged:
        merged.append(i)

for i in b:
    if i not in merged:
        merged.append(i)

print(merged)