
n = int(input())

arr=[ 0 for _ in range(0, n+1)]
arr[0] = 0
arr[1] = 1

def fibonacci(i):
    for i in range(2, n+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n]


print(fibonacci(n))

