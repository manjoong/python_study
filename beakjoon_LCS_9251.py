

string_1 = input()
string_2 = input()
temp_string = ''
if len(string_2) > len(string_1):
    temp_string = string_1
    string_1 = string_2
    string_2 = temp_string


dp = [0 for _ in range(0, min(len(string_1), len(string_2)))]

temp = 0
max_value =0



for i in range(0, len(string_1)):
    for j in range(0, len(string_2)):
        temp = dp[j]
        if string_1[i] == string_2[j]:
            # print("j =", j)
            dp[j] = max_value + 1
            # print("dp[j] =", dp[j])
            # print(dp)        
        # print(temp)
        if max_value < temp:
            # print("i = ", i, "j = ", j, "max = ", max_value)
            max_value = temp

    max_value = 0
    temp = 0
# print(dp)
print(max(dp))


# for i in range(0, len(string_1)):
#     for j in range(0, len(string_2)):



# "ACAYKP"
# "CAPCAK"