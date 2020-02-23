
push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

num = 1
command = ["back"]

arr = []

def push_front(x):
    arr.append(x)


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