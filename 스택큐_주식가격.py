def solution(prices):
    answer = []
    start = 1
    for value in prices:
        cnt = 0
        for i in range(start, len(prices)):
            cnt += 1
            if (value > prices[i]):
                answer.append(cnt)
                break
        # for문에서 else는 break되어서 나오지 않으면 실행됨
        else: 
            answer.append(cnt)
        start += 1
                   
    return answer