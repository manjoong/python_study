n = int(input())
array = []


array = list(map(int, input().split(" ")))


dp = array[0]
max_v = array[0]
temp = array[0]



for i in range(1, n):
  dp = max(array[i], array[i]+dp)
  temp = dp
  if max_v < temp:
    max_v = temp
    

print(max_v)





