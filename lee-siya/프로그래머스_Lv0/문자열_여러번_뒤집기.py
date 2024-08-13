# https://school.programmers.co.kr/learn/courses/30/lessons/181913

'''
문자열 my_string 과 이차원 정수 배열 queries 가 매개변수로 주어집니다.
queries 의 원소는 [ s, e ] 형태로, my_string 의 인덱스 s 부터 인덱스 e 까지를 뒤집으라는 의미입니다.
my_string 에 queries 의 명령을 순서대로 처리한 후의 문자열을 return 하는 solution 함수를 작성해 주세요.
'''

def solution(my_string, queries):
    for s, e in queries:
        
        start = s
        end = e + 1
        
        extracted_text = my_string[start:end]
        reversed_string = extracted_text[::-1]
        my_string = my_string[:start] + reversed_string + my_string[end:]
        
    answer = my_string
    return answer

# [::-1] 를 바로 뒤에 붙여서 실행가능한 것을 알게됨
# my_string = my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]

# 예시 값

my_string = "rermgorpsam"
queries = [[2,3], [0,7], [5,9], [6,10]]
print(solution(my_string, queries))

