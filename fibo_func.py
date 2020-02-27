n = int(input())
arr = [0 for _ in range(0, n+1)]
arr[1] = 1
arr_0 = 0
arr_1 = 1

for i in range(2, n+1):
    arr[i] = arr[i-1] + arr[i-2]

print(arr[n])    
