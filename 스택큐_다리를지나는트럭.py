# 프로그래머스-스택/큐-다리를 지나는 트럭
def solution(bridge_length, weight, truck_weights):
    # 다리를 지나는 트럭을 넣어줄 리스트
    passing = []
    # 다리에 있는 트럭의 남은 시간을 넣어줄 리스트
    time_left = []
    # 전체 시간을 재줄 변수
    second_cnt = 0
    
    while True:
        # 남아있는 트럭과 지나가는 트럭이 없으면 반복문 종료
        if not passing and not truck_weights:
            # 1초를 더해주는 이유는 마지막에 다 내리고 난 시간도 포함해야 하기 때문
            second_cnt += 1
            break
        
        if truck_weights:    
            if (sum(passing) + truck_weights[0]) <= weight:
                truck = truck_weights.pop(0)
                passing.append(truck)
                time_left.append(int(bridge_length))
            
        #반복문 돌때마다 시간 1씩 증가        
        second_cnt += 1
        
        # time에 값이 있을 때
        if time_left:
            # 안에 있는 값에 1씩 다 빼주고
            for i in range(len(time_left)):
                time_left[i] -= 1
            # 첫번째 남은 시간이 0이되면 빼주기
            if (time_left[0] <= 0):
                passing.pop(0)
                time_left.pop(0)
                
    return second_cnt