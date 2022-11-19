'''
모든 판매원은 판매이익 10% 나머지 자신
10%가 1원 미만이면 그냥 그사람 다줌
1200원 판매 (개당 100원)
-> 나:1080, 추천인:120 (10%)
-> 추천인:108, 추천인의 추천인:12 (10%)
-> 추천인의 추천인: 11, 센터: 1 (10%)

enroll: 판매원이름 (민호=center는 제외)
referral: 추천 판매원이름
seller: 판매량 판매원이름
amount: 판매수량
return enroll 이름순으로 이익금 총합 

풀이
me_idx = enroll.index(s) index 함수로 찾아서 할 때는 테스트10~13 시간초과 발생 -> dictionary로 만들어서 해결
'''
answer = []
enroll_dict = {}

def cal_tax(referral, a, me_idx):
    global answer, enroll_dict
    
    # 세금은 수익의 10%
    # 세금이 1원 미만이면 내지 않는다 
    tax = a//10 if a//10 >= 1 else 0
    save = a-tax

    answer[me_idx] += save
    recommender = referral[me_idx]

    # center에 납부 후 종료
    if recommender == "-":
        return
    
    if tax == 0:
        return
    
    recommend_idx = enroll_dict[recommender]
    cal_tax(referral, tax, recommend_idx)
    
def solution(enroll, referral, seller, amount):
    global answer, enroll_dict
    answer = []
    i = 0
    
    for name in enroll:
        enroll_dict[name] = i
        answer.append(0)
        i += 1
    
    for s, a in zip(seller, amount):        
        me_idx = enroll_dict[s]
        cal_tax(referral, a*100, me_idx)
    
    return answer
