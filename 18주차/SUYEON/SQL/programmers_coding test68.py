# 로그인 성공?
def solution(id_pw, db):
    if db_pw := dict(db).get(id_pw[0]):
        return "login" if db_pw == id_pw[1] else "wrong pw"
    return "fail"

def solution(id_pw, db):
    answer = ''
    a, b = id_pw[0], id_pw[1]
    for pk, pw in db:
        if pk == a and pw == b:
            return "login"
    for pk, pw in db:
        if pk == a:
            return "wrong pw"

    return "fail"