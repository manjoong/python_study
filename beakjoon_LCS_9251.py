

string_1 = input()
string_2 = input()
dp = [0 for _ in range(0, min(len(string_1), len(string_2)))]

temp = 0
max_value =0



for i in range(0, len(string_1)):
    for j in range(0, len(string_2)):
        temp = dp[j]
        if max_value < temp:
            max_value == temp
        if string_1[i] == string_2[j]:
            dp[j] = max_value + 1
    max_value = 0
    temp = 0

print(dp)


# for i in range(0, len(string_1)):
#     for j in range(0, len(string_2)):



# "ACAYKP"
# "CAPCAK"