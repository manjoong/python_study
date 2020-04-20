
# num = int(input())

# command = [" " for _ in range(0, num)]

# for i in range(0, num):
#     command[i] = input()

num = 1
command = ["back"]

arr = []

def push(x):
    arr.append(x)

def pop():
    if len(arr) == 0:
        print(-1)
    else:
        print(arr[0])
        del arr[0]

def size():
    print(len(arr))

def empty():
    if len(arr)>0:
        print(0)
    else:
        print(1)

def front():
    if len(arr) == 0:
        print(-1)
    else:
        print(arr[0])

def back():
    if len(arr) == 0:
        print(-1)
    else:
        print(arr[len(arr)-1])



    
for i in range(0, num): 
    if "push" in command[i]:
        push(int(command[i].split(" ")[1]))
        

    elif "pop" in command[i]:
        pop()

    elif "size" in command[i]:
        size()

    elif "empty" in command[i]:
        empty()
        
    elif "front" in command[i]:
        front()
    
    elif "back" in command[i]:
        back()