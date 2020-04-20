n = int(input())

dp=[]
arr=[]
for i in range(0, n):
    arr.append(int(input()))

dp.append(arr[0])
if n>=2:
    dp.append(arr[0] + arr[1])
    dp[1] = max(dp[1], dp[0])
if n >= 3:
    dp.append(max(arr[0], arr[1])+arr[2])
    dp[2] = max(dp[2], dp[1])
    for i in range(3, n):

        dp.append(max((arr[i]+arr[i-1]+dp[i-3]), (arr[i]+dp[i-2])))
        dp[i] = max(dp[i], dp[i-1])

print(max(dp))

#i don't know. i will see the answer