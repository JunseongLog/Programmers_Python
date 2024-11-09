# 프로그래머스_완전탐색_카펫
def solution(brown, yellow):
    answer = []
    x_yellow = 0
    y_yellow = 0
    for i in range(1, yellow+1):
        if yellow % i == 0:
            x_yellow = yellow // i
            y_yellow = i
            if (2*x_yellow + 2*y_yellow + 4) == brown:
                answer.append(x_yellow+2)
                answer.append(y_yellow+2)
                # 브레이크 안하면 x,y 바뀌 값이 반복문으로 또 들어옴
                break
    
    return answer