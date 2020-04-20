# n = int(input())

# quest= []
# for i in range(0, n):
#     quest.append(int(input()))

n =2
quest= [6, 12]
origin_quest = quest[:]




quest.sort(reverse=True)


arr = [0 for _ in range(0, quest[0]+1)]

for i in range(6, quest[0]+1):
    arr[1]=1
    arr[2]=1
    arr[3]=1
    arr[4]=2
    arr[5]=2
    arr[i] = arr[i-1] + arr[i-5]

for i in range(0, len(quest)):
    print(arr[origin_quest[i]])
