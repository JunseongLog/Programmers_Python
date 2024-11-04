# 프로그래머스 스택/큐 올바른 괄호

# 파이썬에는 스택자료형 대신 그냥 리스트 쓰면 됨
# append(), pop()으로 선입후출 구현이 가능함


def check_right_or_not(s):
    stack = []
    for value in s:
        if value == "(":
            stack.append("(")
        elif value == ")":
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    
    return True



