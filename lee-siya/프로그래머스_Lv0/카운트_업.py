# https://school.programmers.co.kr/learn/courses/30/lessons/181920

'''
정수 start_num 와 end_num 가 주어질 때,
start_num 부터 end_num 까지의 숫자를 차례로 담은 리스트를 return 하도록 solution 함수를 완성해 주세요.
'''

def solution(start_num, end_num):
    result = []
    for num in range(start_num, end_num + 1):
        result.append(num)
    answer = result
    return answer

# 예시 값
start_num = 3
end_num = 10
print(solution(start_num, end_num))