
def solution(n):
    answer = []
    arr=[" " for _ in range(0, n+1)]
    arr[1] = "0"
    if n > 1:
        for i in range(2, n+1):
            arr_reverse = ""
            for j in range(0, len(arr[i-1])):
                if arr[i-1][j] == "0":
                    arr_reverse = "1" + arr_reverse
                elif arr[i-1][j] == "1":
                    arr_reverse = "0" + arr_reverse

            arr[i] = arr[i-1] +"0" + arr_reverse
        answer = [int(i) for i in arr[-1]]
    else:
        answer = [int(i) for i in arr[-1]]
    
    
    return answer
