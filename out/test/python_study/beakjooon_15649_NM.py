import itertools

n=input()
arr = []
combi_arr = []
arr=[]
N=n.split(" ")[0]
M=int(n.split(" ")[1])

for i in range(1, int(N)+1):
    arr.append(str(i))

combi_arr.extend(itertools.permutations(arr, M))
arr = list(map(' '.join, combi_arr))


for i in range(0, len(arr)):
    print(arr[i])


    



