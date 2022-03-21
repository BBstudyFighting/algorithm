'''
프로그래머스 완주하지 못한 선수 파이썬
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
'''


def solution(participant, completion):
    participant.sort() # 각각의 값을 정렬
    completion.sort()
    for p,c in zip(participant, completion): #zip함수로 묶기
        if p != c: # 참여자와 완주자가 다르면 참여자의 이름을 리턴해주기
            return p
    return participant.pop() # 그리고 for문을 돌리면서 참여자를 제외시키기
