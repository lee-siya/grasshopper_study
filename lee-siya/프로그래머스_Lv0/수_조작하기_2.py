# https://school.programmers.co.kr/learn/courses/30/lessons/181925

'''
정수 배열 numLog 가 주어집니다.
처음에 numLog[0] 에서 부터 시작해 "w", "a", "s", "d" 로 이루어진 문자열을 입력받아 순서대로 다음과 같은 조작을 했다고 합시다.

- "w" : 수에 1 을 더한다.
- "s" : 수에 1 을 뺀다.
- "d" : 수에 10 을 더한다.
- "a" : 수에 10 을 뺀다.

그리고 매번 조작을 할 때마다 결괏값을 기록한 정수 배열이 numLog 입니다.
즉, numLog[i] 는 numLog[0] 로부터 총 i 번의 조작을 가한 결과가 저장되어 있습니다.

주어진 정수 배열 numLog 에 대한 조작을 위해 입력받은 문자열을 return 하는 solution 함수를 완성해 주세요.
'''

def solution(numLog):

    answer = ''
    # numLog[0]부터 시작해서 그 다음 값의 차이를 판단하고 (+1, -1, +10, -10) 문제에 조건과 맞는 문자열을 answer 에 이어붙여주는 for, if 문 만들기
    index = 0
    for _ in range(len(numLog)-1):
        
        judge = numLog[index]
        judge2 = numLog[index+1]
        
        if judge2 - judge == 1:
            answer += "w"
            index += 1
            
        elif judge2 - judge == -1:
            answer += "s"
            index += 1
            
        elif judge2 - judge == 10:
            answer += "d"
            index += 1
            
        elif judge2 - judge == -10:
            answer += "a"  
            index += 1
        
    return answer


# 예시 값
numLog = [0,1,0,10,0,1,0,10,0,-1,-2,-1]
print(solution(numLog))
