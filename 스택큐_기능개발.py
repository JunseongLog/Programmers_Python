def solution(progresses, speeds):
    answer = []
    while progresses:
        cnt = 0

        while progresses and progresses[0] >= 100:
            # list.pop(0)을 하면 첫번째 값을 뺄 수 있음.
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1

        progresses = [progresses[i]+speeds[i] for i in range(len(progresses))]

        if cnt:
            answer.append(cnt)
    return answer