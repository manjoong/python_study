n = int(input())
dp = [0 for _ in range(0, n)]
q = []

arr = list(map(int, input().split(" ")))
dp[0] = 1
max_value=0
temp=0


for i in range(0, n):
  for j in range(0, i):
    if arr[i]>arr[j]:
      temp = dp[j]
      # dp[i] = dp[j]+1
      if temp > max_value:
        max_value = temp
        dp[i] = max_value+1
  
  if max_value == 0:
    dp[i] = 1
  max_value = 0
      
# for i in range(0, n):
#   print(dp[i])
print(max(dp))
# print(max(dp))


# 6
# 10 20 10 30 20 50
