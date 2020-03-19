
# n = int(input())

# arr=[ 0 for _ in range(0, n+1)]
# arr[0] = 0
# arr[1] = 1


# for i in range(2, n+1):
#     arr[i] = arr[i-1] + arr[i-2]


# for j in range(0, n+1):
#     print(arr[j])



n = int(input())
arr = [0 for _ in range(0, n)]

for i in range(0, n):
    arr[i] = int(input())

zero_count = 0
one_count = 0

def fibo(k):
    if k==0:
        global zero_count
        zero_count = zero_count + 1
        return(0)
    elif k==1:
        global one_count
        one_count = one_count + 1
        return(1)
    else:
        return(fibo(k-1)+fibo(k-2))

for i in range(0, n):
    fibo(arr[i])
    print(str(zero_count) + " " + str(one_count))
    zero_count = 0
    one_count = 0