# n = int(input())
countzero = 0
countone = 0

def fibo(x):
    if x == 0:
        global countzero += 1
        return 0
    elif x == 1:
        countone += 1
        return 1
    else:
        return fibo(x-1) + fibo(x-2)


print(fibo(4))    
