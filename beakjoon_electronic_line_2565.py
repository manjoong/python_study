n = int(input())
first_pole = [0 for _ in range(0, n)]
second_pole = [0 for _ in range(0, n)]
dp = [0 for _ in range(0, n)]

for i in range(0, n):
    string = str(input())
    first_pole[i] = int(string.split(" ")[0])
    second_pole[i] = int(string.split(" ")[1])

first_dic = {}
for i in first_pole:
    first_dic[i] = second_pole[first_pole.index(i)]

print(first_dic)




print(first_pole)
print(second_pole)


# "8"
# "1 8"
# "3 9"
# "2 2"
# "4 1"
# "6 4"
# "10 10"
# "9 7"
# "7 6"