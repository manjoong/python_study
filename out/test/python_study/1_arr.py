# arr=list(map(int, input().split()))
arr = []
for i in range(0, 9):
    arr.append(int(input()))

origin_arr = arr[:]
arr.sort(reverse=True)

print(arr[0])

for i in range(0, 9):
    if int(arr[0]) == int(origin_arr[i]):
        print(i+1)
        break
        

    

