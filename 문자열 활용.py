s ='나는 빨리 집에 가고 싶다'
# print(s)

#

s1 ='나는 빨리 {} 가고 싶다. {} 공부를 해야 집에 {} 있다'
s2 ='하지만, 집에, 갈수'

s3 = s2.split(",")

print(s1.format(s3[1].strip(), s3[0].strip(),s3[2].strip()))



# ○ encode():문자열의인코딩버전변환기본은utf-8
# ○ find(substr):문자열내에포함되는서브문자열첫인덱스반환
# ○ format():{}로구분된치환필드에인자를문자열로치환
# ○ join():리스트의항목을문자구분으로문자열로치환
# ○ split(x):문자열을 x문자 구분으로 리스트로 치환
# ○ strip():문자열의앞뒤공백제거


# a_total = []
# a  = []
# for i in range(0,1):
#     # a  = []
#     a = [i, i+1, i+2]
#     # print(a)
#     a_total.append(a)
#     print(a_total)