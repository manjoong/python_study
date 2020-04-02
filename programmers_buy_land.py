
def solution(land):
   #두번째 행부터 시작해서 위에서 가장 큰 값을 골라 더하는 알고리즘
   for i in range(1,len(land)):
        for j in range(4):
            #k = [n for n in land[i-1]] 처음시도했던 새로운 list만들기
            #del k[j]
            #바로 위 행에서 자신과 같은 열을 제외한 열중 가장 큰값을 구한다.
            k=land[i-1][0:j]+land[i-1][j+1:]
            print(k)
            land[i][j]+=max(k)
   #마지막 행의 최대값을 배출
   return max(land[-1])
