import heapq

def heap_sort(nums):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    sorted_nums = []
    
    while heap:
        sorted_nums.append(heapq.heappop(heap))
    return sorted_nums

def solution(people, limit):
    
    # people.sort()
    people = heap_sort(people)
    print(people)
    count =0
    # print(people)
    # while(people):
    n=0
    light_people= 0
    heavy_people= len(people)-1
    
    while(light_people<heavy_people):
        
        if people[light_people] + people[heavy_people]<=limit:
            # print(light_people, heavy_people)
            heavy_people = heavy_people - 1
            light_people = light_people + 1
            count = count + 1
        else:
            # print(light_people, heavy_people)
            heavy_people = heavy_people - 1
            count = count + 1
            
    if light_people==heavy_people:
        count = count + 1
    
    answer = count
    return answer