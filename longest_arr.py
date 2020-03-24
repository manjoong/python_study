n = int(input())
dp = [0 for _ in range(0, n)]
q = []

arr = list(map(int, input().split(" ")))
dp[0] = 1
max_value=1


for i in range(0, n):
  for j in range(0, i):
    if arr[i]>arr[j]:
      if dp[j] > max_value:
        max_value = dp[j]
        dp[i] = max_value+1
      

print(max(dp))


# 6
# 10 20 10 30 20 50
