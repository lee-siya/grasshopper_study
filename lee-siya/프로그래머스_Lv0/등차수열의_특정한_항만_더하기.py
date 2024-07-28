'''
두 정수 a, d 와 길이가 n 인 boolean 배열 included 가 주어집니다.
첫째항이 a, 공차가 d 인 등차수열에서 included[i] 가 i + 1 항을 의미할 때,
이 등차수열의 1항부터 n 항까지 included 가 true인 항들만 더한 값을 return 하는 solution 함수를 작성해주세요'''

def solution(a, d, included):
    # a, d 로 만들어지는 등차수열 리스트를 만들어두고
    my_list = []
    value = a
    for _ in range(len(included)):
        my_list.append(value)
        value += d
        
    # included 의 값이 True 일 때 결과 리스트에 추가
    result = []
    for value, True_find in zip(my_list, included):
        if True_find == True:
            result.append(value)
    
    # sum 을 써서 answer로 return 하기.
    answer = sum(result)
    return answer

# 문제 예시 값
included = [True, False, False, True, True]
a = 3
d = 4
my_list = []
value = a
print(solution(a,d,included))

'''처음엔 included 에서 false에 해당하는 인덱스 값을 얻고
   등차수열 리스트에서 제거하고 합을 구하는 것을 생각했는데
   enumerate() 함수와 del my_list[], for 문을 썼다가 
   삭제를 한번하면 인덱스가 앞으로 땡겨지는걸 생각하지 못함 그래서 수정함'''