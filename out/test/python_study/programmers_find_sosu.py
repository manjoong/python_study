import itertools

def prime(n):
    if n == 1 or n ==0:
        return False
    else:
        if n == 2:
            return True
        else:
            for i in range(2, n//2+1):
                if n%i ==0:
                    return False
            return True
        
def solution(numbers):
    answer = 0
    arr = [i for i in numbers] #문자열을 끊어서 각각의 배열로
    # print(arr)
    
    combine = [] #각각의 배열을 조합한 조합으로
    for i in range(len(arr)):
        combine.extend(itertools.permutations(arr, i+1))
    # print(combine)
    
    int_combine = [] #조합형식을 다시 스트링으로  그리고 숫자로
    for i in range(len(combine)):
        int_combine.append(int(''.join(combine[i])))
    # print(int_combine)
    
    uni_combine = [] #중복을 지우기 위해 집합으로 집합을 다시 리스트로
    uni_combine = list(set(int_combine))
    # print(uni_combine)
    
    result_combine = list(map(prime, uni_combine)) #마지막으로 소수인지 함수 돌린다.
    # print(result_combine)
    answer = sum(result_combine)
    # print(answer)
    
    
    
    
    return answer