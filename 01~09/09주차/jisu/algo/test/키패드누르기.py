def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12

    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            left = i  # 왼손 엄지의 위치 바꿈
        elif i in [3, 6, 9]:
            answer += 'R'
            right = i  # 오른손 엄지의 위치 바꿈
        else:
            i = 11 if i == 0 else i

            absL = abs(i-left)
            absR = abs(i-right)
            # 3을 나눈 몫과 나머지를 더하면 거리가 나옴
            if sum(divmod(absL, 3)) < sum(divmod(absR, 3)):
                answer += 'L'
                left = i
            elif sum(divmod(absL, 3)) > sum(divmod(absR, 3)):
                answer += 'R'
                right = i
            else:
                if hand == 'right':
                    answer += 'R'
                    right = i
                else:
                    answer += 'L'
                    left = i

    return answer
