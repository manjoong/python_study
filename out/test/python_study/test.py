def solution(inputString):
    answer = 0
    string_arr = [i for i in inputString]#일단 문자열을 배열로 변환
    check_right = [0 for _ in range(0, 4) ]
    kind_open_bracket = ["(", "{", "[", "<"]
    kind_close_bracket = [")", "}", "]",">" ]
    print(string_arr) 
    
    for i in range(0, len(string_arr)):
        if string_arr[i] in kind_open_bracket:
            check_right[kind_open_bracket.index(string_arr[i])] = check_right[kind_open_bracket.index(string_arr[i])] +1
        if sum(check_right) < 0:
            return -1
        print(check_right)
        
    
    for i in range(0, len(string_arr)):
        if string_arr[i] in kind_close_bracket:
            check_right[kind_close_bracket.index(string_arr[i])] = check_right[kind_close_bracket.index(string_arr[i])] -1
            answer = answer + 1
        if sum(check_right) < 0:
            return -1    
        
        print(check_right)

    
    # print(check_right)
    return answer


    [["doc1", "t1", "t2", "t3"], ["doc2", "t0", "t2", "t3"], ["doc3", "t1", "t6", "t7"], ["doc4", "t1", "t2", "t4"], ["doc5", "t6", "t100", "t8"], ["doc6", "t1", "t2", "t4"], ["doc7", "t1", "t2", "t4"], ["doc8", "t1", "t2", "t4"], ["doc9", "t1", "t2", "t4"], ["doc10", "t1", "t2", "t4"], ["doc11", "t1", "t2", "t4"], ["doc12", "t1", "t2", "t4"]]



    ["doc1", "doc2", "doc4", "doc6", "doc7", "doc8", "doc9", "doc10", "doc11", "doc12", "doc3"]