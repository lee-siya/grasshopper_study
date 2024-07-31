# https://school.programmers.co.kr/learn/courses/30/lessons/181922

'''
정수 배열 arr 와 2차원 정수 배열 queries 이 주어집니다.
queries 의 원소는 각각 하나의 query 를 나타내며, [s, e, k] 꼴입니다.
각 query 마다 순서대로 s <= i <= e 인 모든 i 에 대해 i 가 k 의 배수이면 arr[i] 에 1을 더합니다.
위 규칙에 따라 queries 를 처리한 이후의 arr 를 return 하는 solution 함수를 완성해 주세요.
'''

def solution(arr,queries):
    
    for s,e,k in queries:
        for i in range(s,e+1): # 문제 조건 s <= i <= e
            if i % k == 0:
                arr[i] = arr[i] + 1 # arr[i] += 1 도 되는구나
    answer = arr
    return answer


# 예시 값
arr = [0,1,2,4,3]
queries = [[0,4,1],[0,3,2],[0,3,3]]
print(solution(arr,queries))