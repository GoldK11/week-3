from datahandler import *


while True:
    
    a=input('Enter the file name: ')
    if a=='no':
        break
    b=input('Enter the class name: ')
    d = DataHandler(a,b)



    d.GetEvaluation(70)

    print()
    print('가장 성적이 높은 학생은 {}이고 {} 점이다.'.
          format(d.whohigh(),d.highscore()))

    print('가장 성적이 낮은 학생은 {}이고 {} 점이다.'.
          format(d.wholow(),d.lowscore()))
    print()
    

