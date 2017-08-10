#함수 하나도 안 쓴 최악의 비구조적 프로그램을 만들어보자

import math
from openpyxl import *
from functools import reduce

# 1. 파일에서 데이터 읽어와서 자료구조 생성

wb = load_workbook('class_1.xlsx')
ws = wb.active

raw_data = {}

g = ws.rows

for c1,c2 in g:
    raw_data.update({c1.value:c2.value})
print(raw_data)

#딕셔너리에서 점수만 가져와 점수 리스트 만들기
scores=[]

for score in raw_data.values():
    scores.append(score)

print(scores)

# 평균 구하기
sum_score=reduce(lambda a,b: a+b,scores)
n=len(scores)
avrg=sum_score/n

print('평균:', avrg)    

#분산 구하기 : (s - avrg)**2 다 더함 / n
variance = reduce(lambda a,b: a+(b-avrg)**2,scores,0)/n
'''
map쓰는 방법도 있음
variance= reduce(lamgda a,b a+b,
                    map(
                        lambda x:
                        (x-avrg)**2,scores
                        ))/n
'''

print('분산:', variance)


# 표준편차 구하기
standard_deviation = round(math.sqrt(variance),1)
print('표준편차:',standard_deviation)

