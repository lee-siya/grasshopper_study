# https://school.programmers.co.kr/learn/courses/30/lessons/181914

'''
음이 아닌 정수를 9로 나눈 나머지는 그 정수의 각 자리 숫자의 합을 9로 나눈 나머지와 같은 것이 알려져 있습니다.
이 사실을 이용하여 음이 아닌 정수가 문자열 number 로 주어질 때,
이 정수를 9 로 나눈 나머지를 return 하는 solution 함수를 작성해주세요.
'''

def solution(number):
    
    sum_number= 0
    
    for num in number:
        sum_number += int(num)
    answer = sum_number % 9
    
    return answer

# map 활용
def solution(number):
    return sum(map(int, number)) % 9

# 예시 값
number = "123"
print(solution(number))

number = "78720646226947352489"
print(solution(number))
