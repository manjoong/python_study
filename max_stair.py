n = int(input())

arr = [0 for _ in range(0, n)]

arr[0] = int(input())
arr[1] = arr[0]+ int(input())

for i in range(2, n):
    new = int(input())
    arr[i] = max([(arr[i-1]+new), (arr[i-2]+new)])
    
for i in range(0, n):
    print(arr[i])