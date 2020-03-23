n = int(input())
arr = [0 for _ in range(0, n)]
q = []

q = list(map(int, input().split(" ")))
# for i in range(0, n):
#   q.append(int(input(" ")))

arr[0] = q[0]
if n>1:
  count = 1
else:
  count = 0
max = 0


for i in range(1, n):
  arr[i] = q[i]-q[i-1]
  # print("arr[i] : " + str(arr[i]))

  if max < arr[i] :
    max = arr[i]
    # print("max : " +str(max))
    count += 1

print(count)

#즐가하는 부분의 갯수를 말하는게 아니라
#수열 안에서 또 다른 수열(부분수열)을 만들껀데, 무조건 증가하는 증가 수열이여야 하며, 그런 증가 수열 중, 가장 길어야함.

# 6
# 10 20 10 30 20 50