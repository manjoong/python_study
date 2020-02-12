
n = 10

f0 = 0
f1 = 1

if n > 1:
    for i in range(0, ((n//2))):
        f0 = f1+f0
        f1 = f1+f0


if n%2 == 0:
    print f0
else:
    print f1