def solution(board, moves):
    bucket = []
    answer = []
    for move in moves:  # 크레인 이동 1건씩 실행
        for i in range(len(board)):  # board의 윗행부터 검사
            # board의 숫자가 0보다 크면
            if board[i][move-1] > 0:  # 인덱스보정 -1
                # 인형을 bucket에 담고
                bucket.append(board[i][move-1])
                board[i][move-1] = 0  # 그 자리를 0으로 바꾼다.
                # bucket 가장 위에 있는 2개가 숫자가 같다면
                if bucket[-1:] == bucket[-2:-1]:
                    answer += bucket[-1:]  # 사라진 인형을 answer 리스트에 추가
                    bucket = bucket[:-2]  # 위의 두 인형을 지운다.
                break
    return len(answer)*2
