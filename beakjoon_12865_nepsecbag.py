need = list(map(int, input().split(" ")))
count = need[0]
can_weight = need[1]

weight = []
values = []

for i in range(0, count):
    temp = input().split(" ")
    weight.append(int(temp[0]))
    values.append(int(temp[1]))

dp = [ [0 for _ in range(0, can_weight)] for _ in range(0, count)]

# for i in range(1, count):
#     if sum_weight > can_weight:


print(weight)
print(values)
print(dp)


# "4 7"
# "6 13"
# "4 8"
# "3 6"
# "5 12"