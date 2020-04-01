def solution(array, commands):
    answer = ""
    new_array=[]
    result = []
    n = 0
    # print(commands)
    for (i,j,k) in commands:
        new_array = array[i-1:j]
        # print(new_array)
        new_array.sort()
        # print(new_array)
        print(new_array[k-1])
        result.append(new_array[k-1])
        # result[n] = new_array[k-1]
        # n = n+1
        # print(array)
        print(answer)

    return result
