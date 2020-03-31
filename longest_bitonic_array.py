n = int(input())
arr = list(map(int, input().split(" ")))
arr = reverse_arr[:]
front_dp = [0 for _ in range(0, n)]
front_dp[0] = 1
back_dp = [0 for _ in range(0, n)]
back_dp[n-1] = 1
temp = 0
max_value = 0


for i in range(0, n):
    for j in range(0, i):
        if arr[i]> arr[j]:
            temp = front_dp[j]+1
            
            if temp > max_value:
                max_value = temp
        front_dp[i] = max_value
    if max_value == 0:
        front_dp[i] = 1
    temp = 0
    max_value = 0


for i in range(n, -1, 0):
    print(front_dp[i])


# for i in range(0, n):
#     for j in range(0, i):
#         if arr[i]> arr[j]:
#             temp = front_dp[j]+1
            
#             if temp > max_value:
#                 max_value = temp
#         front_dp[i] = max_value
#     if max_value == 0:
#         front_dp[i] = 1
#     temp = 0
#     max_value = 0


# 10
# 1 5 2 1 4 3 4 5 2 1
# 1 * 2 * * 3 4 5 2 1 
# 1   2     3 4 5 6 7  -> corect


# 1 2 2 1 3 3 4 5 2 1  if basetion is front
# 1 5 2 1 4 3 3 3 2 1 if basetion is back  -> if sum of front and back is right answer ? 
