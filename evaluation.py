'''
위클리 챌린지 > 2주차_상호평가
https://programmers.co.kr/learn/courses/30/lessons/83201
i행 j열의 값은 i번 학생이 평가한 j번 학생의 과제 점수
각 학생들이 받은 점수의 평균을 구하여, 기준에 따라 학점을 부여
만약, 학생들이 자기 자신을 평가한 점수가 유일한 최고점 또는 유일한 최저점이라면 그 점수는 제외하고 평균
학생들의 점수가 담긴 정수형 2차원 배열 scores가 매개변수로 주어집니다. 
이때, 학생들의 학점을 구하여 하나의 문자열로 만들어서 return 
90점 이상    A
80점 이상 90점 미만   B
70점 이상 80점 미만   C
50점 이상 70점 미만   D
50점 미만    F
'''
def solution(scores):
    answer = ''
    studentIdx = 0
    studentCnt = len(scores)
    studentScore = []

    while studentIdx < studentCnt:
        for score in scores:
            studentScore.append(score[studentIdx])

        if studentScore.index(min(studentScore)) == studentIdx or studentScore.index(max(studentScore)) == studentIdx:
            sameScore = [i for i, value in enumerate(studentScore) if value == studentScore[studentIdx]]

            if len(sameScore) == 1:
                studentScore.pop(studentIdx)

        avgScore = sum(studentScore)/len(studentScore)
        answer += getScore(avgScore)    
        studentIdx += 1
        studentScore = []

    return answer

def getScore(score):
    if score >= 90:
        scoreRet = 'A'
    elif score >= 80 and score < 90:
        scoreRet = 'B'
    elif score >= 70 and score < 80:
        scoreRet = 'C'
    elif score >= 50 and score < 70:
        scoreRet = 'D'
    else:
        scoreRet = 'F'

    return scoreRet
  

 
