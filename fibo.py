
answer = 0
def fibo()

fibo(0) = 0
fibo(1) = 1


def fibo(a):
    if a == 0:
        return int(0)
    
    elif a == 1:
        return int(1)
    
    

    return(answer + fibo(a-1))

print(answer)