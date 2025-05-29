s = 16
arr = [1, 4, 7, 12, 13, 15, 18]
low = 0
high = len(arr) - 1
flag = False
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == s:
        flag = True
        break
    elif arr[mid] < s:
        low = mid+1
    elif arr[mid] > s:
        high = mid-1
    mid = low +high // 2
if flag == True:
    print(f"index {mid}")
else:
    print("element not found")



