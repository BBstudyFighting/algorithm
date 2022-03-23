'''
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 
어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.
'''
# 1번째 방법
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1): 
        #phone_book을 정렬하고 for문을 이용해 phone_book[i]과 phone_book[i+1] 값을 비교
        if len(phone_book[i]) < len(phone_book[i+1]):  # 첫번째 if문에서 i와 i+1의 길이를 비교한 것은 바로 아래의 if문에서 index가 out of range가 되는 것을 피하기 위함
            if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
                answer = False
                break
    return answer
  
  # 2번째 방법
  def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):  #startswith는 문자열이 특정문자로 시작하는지 여부를 알려준다, true나 false 를 반환
            return False
    return True
