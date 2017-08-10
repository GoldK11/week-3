# 기능별,절차.특정 기준에 의한 함수로 만들자
# 함수 인터페이스 (signature) 
# 인터페이스와 구현부를 나누는 것 >>> 추상화 


import math
from openpyxl import *
from functools import reduce

def get_raw_data(filename):
    '''인터페이스 설명서
    get_raw_data(filename) > dict of rawdata
    : 엑셀에서 파일을 읽어와{'name':'score'...} 형태의 dict을 반환한다.
    '''
    wb = load_workbook(filename)
    ws = wb.active

    raw_data = {}

    g = ws.rows

    for c1,c2 in g:
        raw_data.update({c1.value:c2.value})    
    return raw_data

raw_data=get_raw_data('class_1.xlsx')

def average(score_list):
    n=len(score_list)
    avrg=reduce(lambda a,b: a+b,score_list)/n
    return avrg

def variance(score_list,average):
    n=len(score_list)
    variance = reduce(lambda a,b: a+(b-average)**2,score_list,0)/n
    return variance

def standard_deviation(variance):
    standard_deviation = round(math.sqrt(variance),1)
    return standard_deviation

def show(avrg,varc,devi):
    print('평균:{}, 분산:{}, 표준편차:{}'.format(avrg,varc,devi))

def evaluateClass(avrg, total_avrg, std_dev):
    '''
    evaluateClass(avrg, total_avrg, std_dev) -> None
    avrg : 반 성적 평균
    total_avrg : 학년 전체 성적 평균
    std_dev : 반의 표준 편차 
    '''
    if avrg <total_avrg and std_dev >20:
        print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")
    elif avrg > total_avrg and std_dev >20:
        print("성적은 평균이상이지만 학생들 실력 차이가 크다. 주의 요망!")
    elif avrg < total_avrg and std_dev <20:
        print("학생들간 실력차는 나지 않으나 성적이 너무 저조하다. 주의 요망!")
    elif avrg > total_avrg and std_dev <20:
        print("성적도 평균 이상이고 학생들의 실력차도 크지 않다.")


        




