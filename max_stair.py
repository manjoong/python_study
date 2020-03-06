n = int(input())

arr = [0 for _ in range(0, n)]

arr[0] = int(input())
arr[1] = arr[0]+ int(input())

duplicate=0

for i in range(2, n):

    new = int(input())

    if duplicate != 1:
        arr[i] = max([(arr[i-1]+new), (arr[i-2]+new)])
    else:
        arr[i] = arr[i-2]+new
        duplicate=0

    if arr[i] == arr[i-1]+new:
        duplicate=1

    

print(arr[n-1])


