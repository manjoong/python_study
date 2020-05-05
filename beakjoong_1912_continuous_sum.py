
n = int(input())
string = input()
array = []
# dp = [0 for _ in range(0, n)]


for i in range(0, n):
  array.append(int(string.split(" ")[i]))

# array = list(map(int, array))
# dp[0] = array[0]
dp = array[0]
max_v = array[0]
temp = array[0]

# for i in range(1, n):
#   dp[i] = max(array[i], array[i]+dp[i-1])

for i in range(1, n):
  dp = max(array[i], array[i]+dp)
  temp = dp
  if max_v < temp:
    max_v = temp
    

print(max_v)
