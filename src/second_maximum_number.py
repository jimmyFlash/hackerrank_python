n = int(input())
arr = list(map(int, input().split()))
# limit the list items to that of the original input length
max_ = max(arr[:n])
while max(arr) == max_:
    arr.remove(max(arr))
print(max(arr))
