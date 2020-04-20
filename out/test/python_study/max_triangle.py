n = int(input())
first_num = int(input())


arr_origin = [0 for _ in range(0, n)]


arr_origin[0] = first_num

for j in range(1, n):
    arr_new = list(map(int, input().split(' ')))
    
    
    for i in range(len(arr_new)-1, 0, -1):
        arr_origin[i] = max([(arr_new[i]+arr_origin[i-1]),(arr_new[i]+arr_origin[i])])
    arr_origin[0] = arr_origin[0] + arr_new[0]


    # for k in range(0, len(arr_origin)):
    #     print(arr_origin[k])




print(max(arr_origin))


