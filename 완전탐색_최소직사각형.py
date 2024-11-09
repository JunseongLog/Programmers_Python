# 프로그래머스_완전탐색_최소직사각형
def solution(sizes):
    answer = 0
    w = []
    h = []
    
    for i in range(len(sizes)):
        w.append(max(sizes[i]))
        h.append(min(sizes[i]))
    
    answer = max(w) * max(h)
    return answer