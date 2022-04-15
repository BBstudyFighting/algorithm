# 각 유저별 처리결과 메일을 받은 횟수를 배열에 담는 함수 작성

from collections import defaultdict
# 디폴트 값을 지정해줄수 있는 defaultdict
# 키(id)의 개수를 세거나 리스트나 셋의 항목을 정리할 때 활용됨


def solution(id_list, report, k):
    answer = []
    report_accept = defaultdict(set)  # id가 신고받은 목록
    report_throw = defaultdict(set)  # id가 신고한 목록

    for r in report:
        throw, accept = r.split(' ')  # 신고한 사람, 받은사람
        report_accept[accept].add(throw)  # accept가 신고받은 목록에 throw 추가
        report_throw[throw].add(accept)  # throw가 신고한 목록에 accept 추가

    for _id in id_list:
        cnt = 0
        for r_throw in report_throw[_id]:  # _id가 신고한 아이디를 가져옴(r_throw)
            if len(report_accept[r_throw]) >= k:
                cnt += 1
        answer.append(cnt)
    return answer
