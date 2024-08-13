# https://school.programmers.co.kr/learn/courses/30/lessons/181917

'''
boolean 변수 x1, x2, x3, x4 가 매개변수로 주어질 때,
다음의 식의 true / false 를 return 하는 solution 함수를 작성해주세요.

(x1 ∨ x2) ∧ (x3 ∨ x4)
'''
def boolean_or(a, b):
    if a == True and b == True:
        result = True
    elif a == True and b == False:
        result = True
    elif a == False and b == True:
        result = True
    elif a == False and b == False:
        result = False
    return result
    
def solution(x1, x2, x3, x4):
    result1 = boolean_or(x1, x2)
    result2 = boolean_or(x3, x4)
    if result1 == True and result2 == False:
        answer = not boolean_or(result1, result2)
    elif result1 == False and result2 == True:
        answer = not boolean_or(result1, result2)
    else:
        answer = boolean_or(result1, result2)
    return answer


# 예시 값
x1 = False
x2 = True
x3 = True
x4 = True
print(solution(x1, x2, x3, x4))

x1 = True
x2 = False
x3 = False
x4 = False
print(solution(x1, x2, x3, x4))
