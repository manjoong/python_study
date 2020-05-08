


need = list(map(int, input().split(" ")))
count = need[0]
can_weight = need[1]

weight = []
values = []

for i in range(0, count):
    temp = input().split(" ")
    weight.append(int(temp[0]))
    values.append(int(temp[1]))

dp = []
dp = [values[0]]

for i in range(1, count):
    if weight[]

print(weight)
print(values)


# "4 7"
# "6 13"
# "4 8"
# "3 6"
# "5 12"