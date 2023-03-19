#1.처음에 하나씩 쪼개고 그다음 두개씩 세 개씩 쪼개는 형식으로 for문을 돌린다.
#2. 그중 길이가 제일 작은 값은 return한다.

def solution(s):
    result = []
    if len(s)==1 :   # 문자열 s가 1일 때 반환 값은 항상 1
        return 1
    for i in range(1, (len(s)//2)+1): #쪼갤 수 있는 최대 길이가 문자열 s의 반
        b = ''  #b문자열 안에는 쪼갰을 떄 나오는 문자열 저장
        cnt = 1  #문자열이 연속으로 반복되는지 체크
        tmp=s [:i]

    for j in range (i, len(s), i) : #i만큼 문자룰 계속 쪼갠다
        if tmp==s[j:i+j] :
            cnt+=1
        else:
            if cnt!=1:
                b = b + str(cnt)+tmp
            else:
                b = b + tmp
            tmp=s [j:j+i]
            cnt = 1
    if cnt!=1:    #tmp에 담은 문자를  b변수에 추가해주기 위해서 지정
        b = b + str(cnt) + tmp
    else:
        b = b + tmp

    result.append(len(b))
    return min(result) 

