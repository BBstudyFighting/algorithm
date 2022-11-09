# 옷가게 할인 받기
def solution(price):
    if price>=500000:
        price = price *0.8
    elif price>=300000:
        price = price *0.9
    elif price>=100000:
        price = price * 0.95
    return int(price)

def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)
        
# 문자열안에 문자열
def solution(str1, str2):
    return 1 if str2 in str1 else 2

def solution(str1, str2):
    if str1.count(str2):
        return 1
    else:
        return 2
