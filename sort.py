num = input()
arr = []
for i in range(0, int(num)):
    a = input()
    arr.append(int(a))
    
arr.sort()

for i in range(0, int(num)):
    print(int(arr[i]))

