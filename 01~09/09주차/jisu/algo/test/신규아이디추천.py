def solution(new_id):
    answer = ''
    # 1. 소문자 적용
    new_id = new_id.lower()

    # 2. 숫자, 빼기(-), 밑줄(_), 마침표(.)만 추가하기
    for char in new_id:
        if char.isalpha() or char.isdigit() or char in ['-', '_', '.']:
            answer += char

    # 3. 마침표 2개인 경우 1개로 대체
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4. 마침표 맨앞 맨뒤 제거
    if answer[0] == '.':  # answer 길이가 1보다 작으면 그냥 . 두기
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]

    # 5. 빈문자열엔 a 넣기
    if answer == '':
        answer = 'a'

    # 6. 15자 넘어가면 뒤에 자르기
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7. 3자 미만이면 맨 뒷글자 넣어주기
    while len(answer) < 3:
        answer += answer[-1]

    return answer
