n = int(input())
first_num = int(input())


arr_origin = [0 for _ in range(0, n)]

arr_origin[0] = first_num

for i in range(1, n):
    arr_new = list(map(int, input().split(' ')))
    
    
    for i in range(1, len(arr_new)):
        arr_origin[i] = max([(arr_new[i]+arr_origin[i-1]),(arr_new[i]+arr_origin[i])])  <--욥분...
    arr_origin[0] = arr_origin[0] + arr_new[0]

print(max[arr_origin])
