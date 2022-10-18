# 체육복
def solution(n, lost, reserve):
    reserve_student = set(reserve) - set(lost)
    
    lost_student = set(lost) - set(reserve)
    
    for student in reserve_student:
        if (student - 1) in lost_student:
            lost_student.remove(student - 1)
        elif (student + 1) in lost_student:
            lost_student.remove(student + 1)
            
    return n - len(lost_student)