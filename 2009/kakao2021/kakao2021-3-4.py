# 지원서

# 지원자가 지원서에 입력한 4가지의 정보와 획득한 코딩테스트 점수를 하나의 문자열로 구성한 값의 배열 info,
# 개발팀이 궁금해하는 문의조건이 문자열 형태로 담긴 배열 query가 매개변수로 주어질 때,
# 각 문의조건에 해당하는 사람들의 숫자를 순서대로 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

# info 형식  "개발언어 직군 경력 소울푸드 점수"

# 풀이 설계
# 1. 사전을 설계한다
# 2. query 조건을 추가한 사전을 설계한다

# 효율성 어떻게 통과할 수 있을까?



ex1 = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
# [1,1,1,1,2,4]

import numpy as np

def solution(info, query):
    answer = []
    dic = dict()
    for i in ['cpp', 'java', 'python', '-']:
        for j in ['backend', 'frontend', '-']:
            for k in ['junior', 'senior', '-']:
                for l in ['chicken', 'pizza', '-']:
                    dic[i+j+k+l] = np.zeros(100001,)

    for i in info:
        a, b, c, d, e = i.split(' ')
        for j in [a, '-']:
            for k in [b, '-']:
                for l in [c, '-']:
                    for m in [d, '-']:
                        dic[j+k+l+m][int(e)] += 1

    for i in query:
        q = i.split(' ')
        q = [i for i in q if i!='and']
        answer.append(np.cumsum(dic[''.join(q[:-1])])[int(q[-1])])

    return answer

print(solution(*ex1))

# 더 느려짐


