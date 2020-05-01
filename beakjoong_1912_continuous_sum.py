
n = int(input())
string = input()
array = []
dp = [0 for _ in range(0, n)]


for i in range(0, n):
  array.append(string.split(" ")[i])

array = list(map(int, array))
dp[0] = array[0]

for i in range(1, n):
  dp[i] = max(array[i], array[i]+dp[i-1])





print(max(dp))
