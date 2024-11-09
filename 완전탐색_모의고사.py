# 프로그래머스_완전탐색_모의고사
def solution(answers):
    answer = []
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    cnt_list = [0] * 3
    
    idx1 = 0
    idx2 = 0
    idx3 = 0
    
    for value in answers:
        
        if value == person1[idx1]:
            cnt_list[0] += 1
        
        if value == person2[idx2]:
            cnt_list[1] += 1
            
        if value == person3[idx3]:
            cnt_list[2] += 1
            
        idx1 += 1
        idx2 += 1
        idx3 += 1
        
        if idx1 >= len(person1):
            idx1 = 0
        if idx2 >= len(person2):
            idx2 = 0
        if idx3 >= len(person3):
            idx3 = 0
            
    
    for i in range(3):
        if max(cnt_list) == cnt_list[i]:
            answer.append(i+1)
        
    
    return answer