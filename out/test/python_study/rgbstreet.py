n = int(input())
arr_origin = [0, 0, 0]

for i in range(0, n):
    arr_new = list(map(int, input().split(' ')))

    red = min([(arr_new[0]+arr_origin[1]), (arr_new[0]+arr_origin[2])])
    green = min([(arr_new[1]+arr_origin[0]), (arr_new[1]+arr_origin[2])])
    blue = min([(arr_new[2]+arr_origin[0]), (arr_new[2]+arr_origin[1])])

    arr_origin[0] = red
    arr_origin[1] = green
    arr_origin[2] = blue

print(min(arr_origin))

