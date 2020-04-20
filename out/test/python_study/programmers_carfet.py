
# 문제가 개편 되었습니다. 이로 인해 함수 구성이 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
def solution(brown, red):
    answer = []
    sum =brown + red
    # print(sum)
    y = 1
    while y * y <= sum : #이부분 생각해내기!
        if sum % y ==0:
            x = int(sum/y)
            if x >= y:
                if (x-2)*(y-2) == red:
                    answer.append(x)
                    answer.append(y)
        y =  y+1
        
    return answer
