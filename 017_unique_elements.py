my_list = [1,2,3,4,5,4,5,2,6,7]
unique_items = []

for i in my_list:
    if i not in unique_items:
        unique_items.append(i)

print(unique_items)