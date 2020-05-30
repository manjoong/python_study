need = list(map(int, input().split(" ")))
count = need[0]
can_weight = need[1]

W = []
V = []

for i in range(0, count):
    temp = input().split(" ")
    W.append(int(temp[0]))
    V.append(int(temp[1]))

dp = [ [0 for _ in range(0, can_weight)] for _ in range(0, count)]

# for i in range(1, count):
#     if sum_weight > can_weight:


print(W)
print(V)
print(dp)
#dp[i][s]는 배낭 크기가 s일 때, i개의 물건을 넣었을 때, 가능한 최대 가치를 의미합니다.


# "4 7"
# "6 13"
# "4 8"
# "3 6"
# "5 12"
# "도저히 모르겠다"
#이거 언제 마무리 하냐..