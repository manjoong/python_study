
# num = int(input())

# command = [" " for _ in range(0, num)]

# for i in range(0, num):
#     command[i] = input()

num = 9
command = ["push 5", "push 4", "top", "pop", "size", "empty", "top", "pop", "pop"]

arr = []

def push(x):
    arr.append(x)

def pop():
    if len(arr) == 0:
        print(-1)
    else:
        print(arr[0])
        arr.pop(0)

def size():
    print(len(arr))

def empty():
    if len(arr)>0:
        print 0
    else:
        print 1

def top():
    print(arr[0])

    
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



    
    

    
