
import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for i in range(len(scoville)):
        heapq.heappush(heap, scoville[i])
    # print(heap)
    while len(heap)>0:
        if heap[0] >= K:
            return answer
        a = heapq.heappop(heap)
        if len(heap) != 0: #a를 뺀 후 혹시 배열이 비게 될까봐
            b = heapq.heappop(heap)
            heapq.heappush(heap, a+(b*2))
        answer = answer + 1
    
    return -1
