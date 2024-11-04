# 프로그래머스-스택/큐-포로세스
def solution(priorities, location):
    # enumerate를 이용해서 튜플형태로 인덱스와 값을 같이 저장함.
    queue = [(i, p) for i, p in enumerate(priorities)]
    
    # 리스트가 빌때까지 반복
    cnt = 0
    while queue:
        value = queue.pop(0)
        
        if any(value[1] < q[1] for q in queue):
            queue.append(value)
        else:
            cnt += 1
            if value[0] == location:
                    break

    return cnt