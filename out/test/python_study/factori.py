
answer = 9
def facto(n):
    if n == 0:
        return 1

    if n == 1:
        return 1
    else: 
        return (n * facto(n-1))


print(facto(answer))