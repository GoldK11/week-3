# 정규 분포 관련 함수 라이브러리
# 함수 세 개 (평균,분산,표준편차)

import math
from functools import reduce



class NormDist:

    '''
    def __init__(self,avrg,variance,standard_deviation):
        self.avrg=avrg
        self.variance=variance
        self.standard_deviation
    method만 가져다 쓸거라 member 가 필요없기 때문에 이거 안만들어도 된다
    '''
    
    def average(self,score):
        n=len(score)
        average=reduce(lambda a,b: a+b,score)/n
        return average

    def variance(self,score,average):
        n=len(score)
        variance = reduce(lambda a,b: a+(b-average)**2,score,0)/n
        return variance

    def standard_deviation(self,variance):
        standard_deviation = round(math.sqrt(variance),1)
        return standard_deviation 
'''
if __name__ == '__main__':
    score = [1,2,3,4,5]
    nd = NormDist()
    av = nd.average
    va = nd.variance
    sd = nd.standard_deviation
    print(av(score))
'''
