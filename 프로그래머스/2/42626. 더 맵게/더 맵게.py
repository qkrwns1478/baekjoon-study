from heapq import heappush, heappop, heapify

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while len(scoville):
        try:
            a = heappop(scoville)
            if a >= K:
                return answer
            b = heappop(scoville)
            answer += 1
            c = a + 2 * b
            heappush(scoville, c)
        except:
            break
    if scoville and heappop(scoville) >= K:
        return answer
    return -1