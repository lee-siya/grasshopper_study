# https://school.programmers.co.kr/learn/courses/30/lessons/181915
'''
문자열 my_string 과 정수 배열 index_list 가 매개변수로 주어집니다.
my_string 의 index_list 의 원소들에 해당하는 인덱스의 글자들을 순서대로 이어 붙인 문자열을
return 하는 solution 함수를 작성해 주세요.
'''

def solution(my_string , index_list):
    answer = ''
    for index in index_list:
        answer +=(my_string[index])
    return answer

# 예시 값

my_string = "cvsgiorszzzmrpaqpe"
index_list = [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]
print(solution(my_string, index_list))

my_string = "zpiaz"
index_list = [1, 2, 0, 0, 3]
print(solution(my_string, index_list))