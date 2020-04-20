
# num = int(input())

# command = [" " for _ in range(0, num)]

# for i in range(0, num):
#     command[i] = input()

num = 14
command = ["push 1", "push 2", "top", "size","empty","pop","pop","pop","size","empty","pop","push 3","empty","top"]

arr = []

def push(x):
    arr.append(x)

def pop():
    if len(arr) == 0:
        print(-1)
    else:
        print(arr[len(arr)-1])
        arr.pop()

def size():
    print(len(arr))

def empty():
    if len(arr)>0:
        print(0)
    else:
        print(1)

def top():
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
        
    elif "top" in command[i]:
        top()



    
    

    
