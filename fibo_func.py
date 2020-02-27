# n = int(input())
# arr_0 = 0
# arr_1 = 0

def fibo(x):
    if x == 0:
        # arr_0 = arr_0 + 1
        return 0
    elif x == 1:
        # arr_1 = arr_1 + 1
        return 1
    else:
        return fibo(x-1) + fibo(x-2)


print(fibo(4))    
