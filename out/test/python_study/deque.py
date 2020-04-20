# -*- coding: utf-8 -*- 

num = int(input())
command = [" " for _ in range(0, num)]
for i in range(0, num):
    command[i] = input()

# num = 15
# command = ["push_back 1","push_front 2","front","back","size","empty","pop_front","pop_back","pop_front","size","empty","pop_back","push_front 3","empty","front"]



arr = []

def push_front(x):
    arr.insert(0, x)


def push_back(x):
    arr.append(x)

def pop_front():
    if len(arr) == 0:
        print(-1)
    else:
        print(arr[0])
        del arr[0]

def pop_back():
    if len(arr) == 0:
        print(-1)
    else:
        # print(len(arr))
        print(arr[len(arr)-1])
        del arr[len(arr)-1]

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
    # print("i는"+ str(i)+"입니다")
    if "push_front" in command[i]:
        push_front(int(command[i].split(" ")[1]))

    elif "push_back" in command[i]:
        push_back(int(command[i].split(" ")[1]))
        

    elif "pop_front" in command[i]:
        pop_front()

    elif "pop_back" in command[i]:
        pop_back()

    elif "size" in command[i]:
        size()

    elif "empty" in command[i]:
        empty()
        
    elif "front" in command[i]:
        front()
    
    elif "back" in command[i]:
        back()