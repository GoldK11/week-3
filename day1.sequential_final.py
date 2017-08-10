from sequential_func import *

if __name__=='__main__':
    raw_data = get_raw_data('class_1.xlsx')
    scores = list(raw_data.values())
    avrg = average(scores)
    variance = variance(scores,avrg)
    std_deviation = standard_deviation(variance)

    print('평균:{}, 분산:{}, 표준편차:{}'.format(avrg,variance,std_deviation))
    print()
    evaluateClass(avrg, 50, std_deviation)


