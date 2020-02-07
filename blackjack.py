N, M = list(map(int, input().split()))
arr = list(map(int, input().split(' ')))
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
                    if M-(arr[i]+arr[j]+arr[k]) < answer and M-(arr[i]+arr[j]+arr[k]) >= 0 :
                        answer = M-(arr[i]+arr[j]+arr[k])                
                    elif M-answer==0:
                        break

print(M-answer)
                 