import random
from random import randint
import math

class HillMax(object):
    def __init__(self):
        pass
    def hill_max(self,lst,step):
        assert(step > 1,"step must > 1")
        start = 0
        len_lst = len(lst)
        m = lst[start]
        while start < len_lst - 1:
            loc = lst[start + 1:start + 1 + step]
            mm = max(loc)
            ## 如果当前值最大，则返回
            if m >= mm:
                return m 
            else:
                ## 如果不是就跳过本批次
                # mm_pos = [p for p,v in enumerate(loc) if v == mm]
                start += step
                m = mm
    def sim_annealing_max(self,lst,step):
        assert(step > 1,"step must > 1")
        start = 0
        len_lst = len(lst)
        m = lst[start]
        times = 1.0
        while start < len_lst - 1:
            loc = lst[start + 1:start + 1 + step]
            mm = max(loc)
            ## 如果当前值大于等于mm,则以一定的概率跳过
            # 1 - math.exp(mm-m) 越大，越应该跳过
            # 次数越多，越应该跳过
            if m >= mm:
                if start >= len_lst - 1 or  random.uniform(0,1) < (1 - math.exp(mm-m))*times:
                    return m
                else:
                    start += step
                    times += 1
                    print("times : ", times)
            else:
                ## 如果不是就跳过本批次
                # mm_pos = [p for p,v in enumerate(loc) if v == mm]
                start += step
                m = mm
    
if __name__ == '__main__':
    lst = [randint(1, 100) for i in range(20)]
    hill_object = HillMax()
    print(lst)
    print(max(lst))
    print(hill_object.hill_max(lst,4))
    print(hill_object.sim_annealing_max(lst,4))
