

def sumoddeven(arr): #홀수의 합과 짝수의 합을 구하는 함수
    even_sum = 0
    odd_sum = 0
    for i in range(0, len(arr)):
        if i%2 ==0:
            even_sum += arr[i]
        else:
            odd_sum += arr[i]
    return(even_sum, odd_sum)



def countBalancingElements(arr):

    count = 0 #count = n
    result = 0 # 결괏값
    temp = '' #동시에 겹쳐나오는 수를 판별하기 위한 변수(조건이 참일때의 직전의 변수를 저장함)

    while count != len(arr):
        temp_arr = arr[:]
        if temp == temp_arr[count]: #동시에 여러수가 겹쳐 나올때의 수가 참이였으면 뒤에 나오는 같은 수는 무조건 참 이므로 else 밑 연산을 할 필요가 없음
            result += 1
        else:
            del temp_arr[count]   #실제로 수를 빼봄
            sum_arr=sumoddeven(temp_arr)
            if sum_arr[0] == sum_arr[1]: #균형잡힌 배열인지 확인
                print(arr[count])
                print(count)
                temp = arr[count]
                result += 1
            else:
                temp = ''

        count += 1

    # while count != len(arr):
    #     temp_arr = arr[:]
    #     if temp_arr[count] in duplicate_num_check:
    #         if duplicate
    #         result += 1
    #     else:
    #         del temp_arr[count]
    #         sum_arr=sumoddeven(temp_arr)
    #         if sum_arr[0] == sum_arr[1]:
    #             duplicate_num_check.append(arr[count])
    #             odd_even_check.append(count%2)
    #             result += 1

    #     count += 1
    return(result)