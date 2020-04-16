
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
    while(people):
        # heap(people)
        if len(people) ==1:
            count=count + 1
            break
        else:
            if people[0] > int(limit/2):
                count = count + len(people)
                print("굿")
                people = []
                break
            else:      
                if people[len(people)-2] + people[len(people)-1] <= limit:
                    if len(people)%2 == 0:
                        count = count + int(len(people)/2)
                        people = []
                    else:
                        print(int(count/2))
                        count = count + int(len(people)/2) + 1
                        people = []
                    break
                
                
                if people[0] + people[1] > limit :
                    count = count + len(people)
                    people = []
                    break


                if people[0] + people[1] <= limit:         
                    for i in range(1, len(people)):
                        if people[0] + people[i] <= limit:
                            # print(people[0], people[i])
                            continue
                        else:
                            del people[i-1]
                            del people[0]
                            count = count + 1
                            break
                
#                 if people[0] + people[1] <= limit:         
#                     for i in range(len(people)-1, 0, -1):
#                         # print(people[0], people[i])

#                         if people[0] + people[i] <= limit:
#                             # print(people[0], people[i])

#                             people.pop(i)
#                             people.pop(0)
#                             count = count + 1
#                             break

            
                
        # n = n+1
        
    
    
    answer = count
    return answer
