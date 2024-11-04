# 프로그래머스-스택/큐-같은숫자는싫어
def solution(arr):
    # 스택 리스트를 만들고, 겹치는 거 빼고 나머지만 스택 리스트에 넣는다
    stack = []
    
    
    for i in range(len(arr)):
        if i == 0:
            stack.append(int(arr[i]))
            continue
        
        if stack[-1] != arr[i]:
            stack.append(int(arr[i]))

        
    return stack