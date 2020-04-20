result = 0
def solution(numbers, target):
    # print(numbers, target)
    answer = 0
    dfs(numbers, target, 0)
    return result

def dfs(numbers, target, k):
    total = 0
    global result
    # print(result)
    if k == len(numbers):
        total = 0
        total =sum(numbers)
        if total == target:
            result = result + 1
            # print(result)
    else:
        numbers[k] = numbers[k] * 1 #이부분에서 k의역할
        dfs(numbers, target, k+1)
        
        numbers[k] = numbers[k] * -1
        dfs(numbers, target, k+1)
