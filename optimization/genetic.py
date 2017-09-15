"""
写在前面的话：
跟着简书学了遗传算法，代码码了一遍。请跳转以下链接
http://www.jianshu.com/p/80dc0f4247ab

遗传算法是一种优化算法，
通过模仿基因遗传定律而开发出的优化方案


to do list:
1.优化代码结构
2.给出多点交叉方案
3.给出其他selection方案
"""

from numpy import random
import numpy as np
import matplotlib.pyplot as plt
from math import pi,sin
import copy


class Genetic(object):
    def __init__(self,popsize,chrosize,xrangemin,xrangemax):
        self.popsize =popsize
        self.chrosize =chrosize
        self.xrangemin =xrangemin
        self.xrangemax =xrangemax
        self.crossrate =1
        self.mutationrate =0.01

    def initialpop(self):
        pop = random.randint(0,2,size = (self.popsize,self.chrosize))
        return pop

    def get_declist(self,chroms):
        step = (self.xrangemax - self.xrangemin)/float(2**self.chrosize-1)
        self.chroms_declist = []
        def chromtodec(chrom):
            m = 1
            r = 0
            for i in range(self.chrosize):
                r = r + m*chrom[i]
                m = m*2
            return r
        for i in range(self.popsize):
            chrom_dec = self.xrangemin + step*chromtodec(chroms[i])
            self.chroms_declist.append(chrom_dec)
        return self.chroms_declist
    def fun(self,x1):
        return x1*sin(10*pi*x1) + 2.0
    def get_fitness(self,x):
        fitness = []
        for x1 in x:
            fitness.append(self.fun(x1))
        return fitness
    def selection(self,popsel,fitvalue):
        new_fitvalue = []
        totalfit = sum(fitvalue)
        accumulator = 0.0
        for val in fitvalue:
            new_val = (val*1.0/totalfit)
            accumulator += new_val
            new_fitvalue.append(accumulator)
        ms = []
        for i in range(self.popsize):
            ms.append(random.random())
        ms.sort()
        fitin = 0 
        newin = 0
        newpop = popsel
        while newin < self.popsize:
            if(ms[newin] < new_fitvalue[fitin]):
                newpop[newin] = popsel[fitin]
                newin = newin + 1
                # fitin = 0
            else:
                fitin = fitin + 1
        pop = newpop 
        return pop
    #单点交叉遗传
    def crossover(self,pop):
        for i in range(self.popsize -1):
            if(random.random() < self.crossrate):
                singpoint = random.randint(0,self.chrosize)
                temp1 = []
                temp2 = []
                temp1.extend(pop[i][0:singpoint])
                temp1.extend(pop[i+1][singpoint:self.chrosize])
                temp2.extend(pop[i+1][0:singpoint])
                temp2.extend(pop[i][singpoint:self.chrosize])
                pop[i] = temp1
                pop[i+1] = temp2
        return pop
    #变异遗传
    def mutation(self,pop):
        for i in range(self.popsize):
            for i in range(2):
                if random.random() < self.mutationrate:
                    mpoint = random.randint(0,self.chrosize - 1)
                    if(pop[i][mpoint] == 1):
                        pop[i][mpoint] == 0
                    else:
                        pop[i][mpoint] == 1
        return pop
    #精英生存
    def elitism(self,pop,pop_best,next_fit_values,next_best_fit,fit_best):
        #输入参数为上一代最优个体，变异之后的种群，
        #上一代的最优适应度，本代最优适应度。这些变量是在主函数中生成的。
        if next_best_fit-fit_best <0:  
            #满足精英策略后，找到最差个体的索引，进行替换。         
            pop_worst =next_fit_values.index(min(next_fit_values))
            pop[pop_worst] = pop_best
        return pop



if __name__ == '__main__':
    genemic_object = Genetic(10,10,-1,2)
    generation = 1000
    best_fit_value_list = []
    #生成随机序列
    pop = genemic_object.initialpop()
    for i in range(generation):
        #序列解码
        dec_list = genemic_object.get_declist(pop)
        #适应度计算
        fit_values = genemic_object.get_fitness(dec_list)
        
        best_fit_value = max(fit_values)
        print(best_fit_value)
        #保存每一代的最高适应度
        best_fit_value_list.append(best_fit_value)
        pop_best = pop[fit_values.index(best_fit_value)]
        pop_best_deep_copy = copy.deepcopy(pop_best)
        ## 下一代个体选择
        #选择后代
        pop_selected = genemic_object.selection(pop,fit_values)
        #交叉突变
        pop_crossovered = genemic_object.crossover(pop_selected)
        #基因突变
        pop_mutationed = genemic_object.mutation(pop_crossovered)
        ## 下一代适应性检测
        next_dec_list = genemic_object.get_declist(pop_mutationed)
        next_fit_values = genemic_object.get_fitness(next_dec_list)
        next_best_fit_value = max(next_fit_values)
        # 比较本代和下代最优个体适应度
        pop = genemic_object.elitism(pop_mutationed,pop_best_deep_copy,next_fit_values,next_best_fit_value,best_fit_value)
    t = [x for x in range(generation)]
    s = best_fit_value_list
    plt.plot(t,s)
    plt.show()

    


