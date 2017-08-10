from normal_dist import *
import openpyxl

# 반 성적 가져와서
# 연관된 모든 연산
# 이 연산한 결과를 caching
# NorDist 객체를 상속할 것인가? inheritance: IS_A-X
# 합성할서인가? HAS-X
# class member 0 ,instance member x

class DataHandler:
    evaluator = NormDist()

    #class method
    @classmethod
    def get_raw_data(cls,filename):
        wb = openpyxl.load_workbook(filename)
        ws = wb.active
        dic = {}
        g = ws.rows
        for name, score in g:
            dic[name.value] = score.value

        return dic
    
    
    def __init__(self,filename,clsname):
        #엑셀파일에서 데이터를 받아서
        #
        self.rawdata = DataHandler.get_raw_data(filename) 
        self.clsname = clsname
        self.cache = {}
        #cache의 역할: 가져온 데이터, 필요할 때 마다 연산된 데이터(결과값)를 저장

    # cache 이용법
    def get_scores(self):
        if 'scores' not in self.cache:
            self.cache['scores'] = \
                                 list(self.rawdata.values())
        return self.cache['scores']                        

    #연산
    def get_avrg(self):
        if 'average' not in self.cache:
            avrg=self.evaluator.average(self.get_scores())
            self.cache['average']=avrg
        return self.cache['average']

    def get_variance(self):
        if 'variance' not in self.cache:
            var=self.evaluator.variance(self.get_scores(),self.get_avrg())
            self.cache['variance']=var
        return self.cache['variance']

    def get_std_dev(self):
        if 'std_dev' not in self.cache:
            stdev=self.evaluator.standard_deviation(self.get_variance())
            self.cache['std_dev']=stdev
        return self.cache['std_dev']

    def whohigh(self):
        if 'whohigh' not in self.cache:
            who=reduce(lambda a,b: a if self.rawdata.get(a)>self.rawdata.get(b) else b, self.rawdata.keys())
            self.cache['whohigh'] = who
        return self.cache['whohigh']

    def wholow(self):
        if 'wholow' not in self.cache:
            who=reduce(lambda a,b: b if self.rawdata.get(a)>self.rawdata.get(b) else a, self.rawdata.keys())
            self.cache['wholow'] = who
        return self.cache['wholow']        

    def highscore(self):
        if 'highscore' not in self.cache:
            high=self.rawdata[self.whohigh()]
            self.cache['highscore']=high
        return self.cache['highscore'] 
    
    def lowscore(self):
        if 'lowscore' not in self.cache:
            low=self.rawdata[self.wholow()]
            self.cache['lowscore']=low
        return self.cache['lowscore']
    
    def __str__(self):
        return '{} : {}'.format(self.rawdata,self.clsname)




    def GetEvaluation(self, total_avrg):
        print('*' * 50)
        print("%s 반 성적 분석 결과" % self.clsname)
        print(
        "{0}반의 평균은 {1}점이고 분산은 {2}이며,따라서 표준편차는{3}이다".format(
            self.clsname,
            self.get_avrg(),
            self.get_variance(),
            self.get_std_dev()))
        print('*' * 50)
        print("%s 반 종합 평가" % self.clsname)
        print('*' * 50)
        self.evaluateClass(total_avrg)

    def evaluateClass(self, total_avrg):
        avrg = self.get_avrg()
        std_dev = self.get_std_dev()
        
        if avrg <total_avrg and std_dev >20:
            print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")
        elif avrg > total_avrg and std_dev >20:
            print("성적은 평균이상이지만 학생들 실력 차이가 크다. 주의 요망!")
        elif avrg < total_avrg and std_dev <20:
            print("학생들간 실력차는 나지 않으나 성적이 너무 저조하다. 주의 요망!")
        elif avrg > total_avrg and std_dev <20:
            print("성적도 평균 이상이고 학생들의 실력차도 크지 않다.")
            



