def solution(stock, dates, supplies, k):
    answer = 0
    start = 0
    stk = []
    while stock < k:
        for i in range(start, len(dates)):
            if dates[i] <= stock:  # 만약 stock이 여유가 있어서 date[i]읠 날까지 가면 그날의 밀가루를 갖는셈
                stk.append(supplies[i])
                # print(stk)
            else:                #여유가 없으니 일단, start지점을 저장해 두고 stock을 채우잔 뜻
                start = i
                break
        answer = answer + 1
        stk.sort(reverse = True) #있는 것 중, 큰 걸 하는게 오래 버팀
        # print(stk)
        stock = stock + stk[0]
        stk.pop(0)
    
                
        
    return answer
