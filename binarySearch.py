s = 89
arr = [1, 4, 7, 12, 13, 15, 18, 24]
low = 0
high = len(arr) - 1
flag = False
while mid>=0:
    mid = (low + high) // 2
    if arr[mid] == s:
        print(mid)
        break
    elif arr[mid] < s:
        low = mid+1
    elif arr[mid] > s:
        high = mid-1
if flag == False:
    print(f"index {mid}")
else:
    print("element not found")
