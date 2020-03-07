n = int(input())

arr = [0 for _ in range(0, n)]

first = int(input())
arr[0] = first
second = int(input())
arr[1] = arr[0] + second
third = int(input())
arr[2] = max([first, second])+third
pre = third



for i in range(3, n):

    new = int(input())
    arr[i] = max([(new+pre+arr[i-3]),(new+arr[i-2])])
    pre = new



for i in range(0, n):
    print(arr[i])


