q = list(map(int, input().split()))
N = q[0]
M = q[1]
arr = []
for i in range(0, N):
    arr.append(int(input()))
answer = M
for i in range(0, N):
    for j in range(0, N):
        if j == i:
            j = j+1
        else:
            for k in range(0, N):
                if k == i or k == j:
                    k = k+1
                else:
                    print("i: " + str(i) + " j: " + str(j) + " k: " + str(k))
                    if M-(arr[i]+arr[j]+arr[k]) < answer and M-(arr[i]+arr[j]+arr[k]) >= 0 :
                        answer = M-(arr[i]+arr[j]+arr[k])
                        print(answer)                  
                    elif M-answer==0:
                        break

print(M+answer)
                 