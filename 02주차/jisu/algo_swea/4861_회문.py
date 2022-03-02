def reverse(row): # 문자열 뒤집기 함수
    # 리스트 초기화
    r_row = []
    # 거꾸로 불러오며 리스트에 더하기
    for i in range(len(row)-1, -1, -1):
        r_row.append(row[i])
    # 뒤집힌 리스트 반환
    return r_row

def palindrome(): # 회문 함수
    for i in range(n):
        # 가로 검사
        for j in range(n-m+1):
            tmp = words[i][j:j+m]
            # 회문검사
            if tmp == reverse(tmp):
                return tmp
        # 세로 검사
        for j in range(n-m+1):
            tmp = []  # 세로문자열을 위한 빈리스트
            for k in range(m):
                tmp.append(words[j+k][i])  # k값이 증가하며 세로값 추가
            if tmp == reverse(tmp):
                return tmp
    return []  # 팰린드롬이 없으면 빈리스트 반환

T = int(input()) # 함수적용
for tc in range(1, T+1):
    n, m = map(int, input().split())
    words = [list(input()) for _ in range(n)]
    # 원하는 형식으로 출력하기 위해 join 사용
    ans = palindrome()
    print(f"#{tc} {''.join(ans)}")
