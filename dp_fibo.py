



n = int(input())
arr = [0 for _ in range(0, n)]

for i in range(0, n):
    arr[i] = int(input())



zero_arr = [0 for _ in range(0, max(arr)+1)]
one_arr = [0 for _ in range(0, max(arr)+1)]

zero_arr[0] = 1
one_arr[0] = 0

for i in range(1, max(arr)+1):
    zero_arr[i] = one_arr[i-1]
    one_arr[i] = one_arr[i-1] + zero_arr[i-1]




for i in range(0, n):
    print(str(zero_arr[arr[i]]) + " " + str(one_arr[arr[i]]))
