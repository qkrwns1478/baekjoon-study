from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    pp = deque(people)

    while pp:
        p = pp.pop()
        if pp and p + pp[0] <= limit:
            pp.popleft()
            answer += 1
        else:
            answer += 1
    
    return answer