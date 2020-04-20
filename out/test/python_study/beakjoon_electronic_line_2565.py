n = int(input())
first_pole = [0 for _ in range(0, n)]
second_pole = [0 for _ in range(0, n)]
dp = [0 for _ in range(0, n)]
count = 0

for i in range(0, n):
    string = str(input())
    first_pole[i] = int(string.split(" ")[0])
    second_pole[i] = int(string.split(" ")[1])

first_dic = {}
for i in first_pole:
    first_dic[i] = second_pole[first_pole.index(i)]


first_pole = []
second_pole = []
for key, value in first_dic.items():
    first_pole.append(key)
    second_pole.append(value)
    
temp =0
max_value = 0
dp[0] = 1
for i in range(0, len(second_pole)):
    for j in range(0, i):
        if second_pole[i] > second_pole[j]:
            temp = dp[j] + 1
            if max_value < temp:
                max_value = temp
                dp[i] = max_value
    if temp == 0:
        dp[i] = 1
    temp =0
    max_value = 0


print(len(second_pole)-max(dp))
    

# print(count)
# print(first_dic)
# print(first_pole)
# print(second_pole)



# "8"
# "1 8"
# "3 9"
# "2 2"
# "4 1"
# "6 4"
# "10 10"
# "9 7"
# "7 6"