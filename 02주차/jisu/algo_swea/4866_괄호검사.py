# 문제소개
# 입력된 문자열의 괄호를 검사하는 프로그램 만들기
# 문자열 안에 모든 () {} 이 제대로 입력됐으면 1, 아니면 0을 출력

# 풀이접근
# 글자를 리스트로 만들어 for 문으로 하나씩 검사하기
# 문자열 중 시작괄호 ( or { 이 나오면 스택리스트에 추가해줌
# 최근에 추가된 시작괄호와 쌍이 맞는 끝괄호 있는지 pop으로 검사 (stack 특성 활용)

# 괄호 검사 함수 정의
def check(string):
    # 스택리스트 초기화
    stack = []
    for char in string:  # sting 하니씩 검사
        if char == '(' or char == '{':
            stack.append(char)  # 시작괄호가 있다면 스택에 추가
        elif char == ')' or char == '}':
            if not stack:  # 시작괄호가 없다면 0 반환
                return 0
            # pop으로 마지막 리스트를 꺼내 쌍이 맞지 않으면 0 반환
            elif char == ')' and stack.pop() != '(':
                return 0
            elif char == '}' and stack.pop() != '{':
                return 0

    # (( 와 같이 시작괄호가 두개가 스택에 있는 경우도 있기 때문에
    # 만약 stack 안에 시작 괄호가 남아있다면 0 반환
    if stack:
        return 0
    return 1


T = int(input())
for tc in range(1, 1+T):
    string = list(input())
    print(f'#{tc} {check(string)}')
