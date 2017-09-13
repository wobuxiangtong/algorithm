"""
LD算法（Levenshtein Distance）又成为编辑距离算法（Edit Distance）。
它是以字符串A通过插入字符、删除字符、替换字符变成另一个字符串B
操作过程的次数表示两个字符串的差异。


to do list:
1.添加可视化高亮动态展示

"""
import numpy as np
class LD(object):
    def __init__(self):
        pass
    def ld(self,a,b):
        """
        统计编辑距离
        """
        len_a = len(a)
        len_b = len(b)
        if min(len_a,len_b) == 0:
            return max(len_a,len_b)
        if a[len_a-1] == b[len_b-1]:
            return self.ld(a[:len_a-1],b[:len_b-1])
        else:
            ld_tuple= self.ld(a[:len_a-1],b[:len_b-1]),self.ld(a[:len_a],b[:len_b-1]),self.ld(a[:len_a-1],b[:len_b])
            return min(ld_tuple) + 1

    def ld_and_mat(self,a,b):
        """
        统计编辑距离并生成编辑矩阵
        编辑矩阵的数值是对应文本的最小编辑距离

        利用动态规划，如果当前对应元素相等，
        编辑距离等于a[:a.length-1]和b[:b.length-1]对应的编辑距离
        如果当前对应元素不相等，则对应三种情况中的最小值+1
        """
        len_a = len(a)
        len_b = len(b)
        if min(len_a,len_b) == 0:
            if len_a > len_b:
                for i in range(len_a):
                    if self.ld_mat[i][0] == 0:
                        self.ld_mat[i][0] = i
            elif len_b > len_a:
                for i in range(len_b):
                    if self.ld_mat[0][i] == 0:
                        self.ld_mat[0][i] = i
            return max(len_a,len_b)
        if a[len_a-1] == b[len_b-1]:
            if self.ld_mat[len_a-1][len_b-1] == 0:
                self.ld_mat[len_a-1][len_b-1] = self.ld_and_mat(a[:len_a-1],b[:len_b-1])
        else:
            ld_tuple= self.ld_and_mat(a[:len_a-1],b[:len_b-1]),self.ld_and_mat(a[:len_a],b[:len_b-1]),self.ld_and_mat(a[:len_a-1],b[:len_b])
            if self.ld_mat[len_a-1][len_b-1] == 0:
                self.ld_mat[len_a-1][len_b-1] = min(ld_tuple) + 1
        return self.ld_mat[len_a-1][len_b-1]

    def print_diff(self,a,b): 
        """
        根据编辑矩阵生成差异文本

        编辑矩阵优先考虑左移，如果左边不为零且小于左上方
        当移动到第一行或者第一列时，特殊考虑
        """
        index_mat_a = len(a) - 1
        index_mat_b = len(b) - 1
        diff_a = ""
        diff_b = ""
        head_flag = 0
        while index_mat_a > 0 and index_mat_b > 0:
            if self.ld_mat[index_mat_a][index_mat_b-1] != 0 and self.ld_mat[index_mat_a][index_mat_b-1] <= self.ld_mat[index_mat_a-1][index_mat_b-1]:
                diff_a = "_" + diff_a
                diff_b = b[index_mat_b] + diff_b
                index_mat_a = index_mat_a
                index_mat_b = index_mat_b - 1
            else:
                diff_a = a[index_mat_a] + diff_a
                diff_b = b[index_mat_b] + diff_b
                index_mat_a = index_mat_a - 1
                index_mat_b = index_mat_b - 1
            """
            逻辑复杂且不严谨，直接观察矩阵规律，见方法注释
            # if self.ld_mat[index_mat_a-1][index_mat_b] == 0:
            #     diff_a = a[index_mat_a] + diff_a
            #     diff_b = b[index_mat_b] + diff_b
            #     index_mat_a = index_mat_a - 1
            #     index_mat_b = index_mat_b - 1
            # else:
            #     if self.ld_mat[index_mat_a][index_mat_b-1] !=0 :
            #         mat_tuple = (self.ld_mat[index_mat_a-1][index_mat_b-1],self.ld_mat[index_mat_a-1][index_mat_b],self.ld_mat[index_mat_a][index_mat_b-1])
            #         if mat_tuple.index(min(mat_tuple)) == 0:
            #             diff_a = a[index_mat_a] + diff_a
            #             diff_b = b[index_mat_b] + diff_b
            #             index_mat_a = index_mat_a - 1
            #             index_mat_b = index_mat_b - 1
            #         elif mat_tuple.index(min(mat_tuple)) == 1:
            #             diff_a = a[index_mat_a] + diff_a
            #             diff_b = "_" + diff_b
            #             index_mat_a = index_mat_a - 1
            #             index_mat_b = index_mat_b
            #         else:
            #             diff_a = "_" + diff_a
            #             diff_b = b[index_mat_b] + diff_b
            #             index_mat_a = index_mat_a
            #             index_mat_b = index_mat_b - 1
            #     else:
            #         mat_tuple = (self.ld_mat[index_mat_a-1][index_mat_b-1],self.ld_mat[index_mat_a-1][index_mat_b])
            #         if mat_tuple.index(min(mat_tuple)) == 0:
            #             diff_a = a[index_mat_a] + diff_a
            #             diff_b = b[index_mat_b] + diff_b
            #             index_mat_a = index_mat_a - 1
            #             index_mat_b = index_mat_b - 1
            #         elif mat_tuple.index(min(mat_tuple)) == 1:
            #             diff_a = a[index_mat_a] + diff_a
            #             diff_b = "_" + diff_b
            #             index_mat_a = index_mat_a - 1
            #             index_mat_b = index_mat_b
        """
        print(index_mat_a,index_mat_b)
        if index_mat_a == 0 and index_mat_b == 0:
                diff_b = b[index_mat_b] + diff_b
                diff_a = a[index_mat_a] + diff_a
        elif index_mat_a < index_mat_b:
            while index_mat_b >= 0:
                if head_flag == 0:
                    diff_a = a[index_mat_a] + diff_a
                    diff_b = b[index_mat_b] + diff_b
                    index_mat_a = index_mat_a
                    index_mat_b = index_mat_b - 1
                    head_flag = head_flag + 1
                else:
                    diff_a = "_" + diff_a
                    diff_b = b[index_mat_b] + diff_b
                    index_mat_a = index_mat_a
                    index_mat_b = index_mat_b - 1
        else :
            while index_mat_a >= 0:
                if head_flag ==0:
                    diff_a = a[index_mat_a] + diff_a
                    diff_b = b[index_mat_b] + diff_b
                    index_mat_a = index_mat_a - 1
                    index_mat_b = index_mat_b
                else:
                    diff_a = a[index_mat_a] + diff_a
                    diff_b = "_" + diff_b
                    index_mat_a = index_mat_a - 1
                    index_mat_b = index_mat_b
        print(diff_a,diff_b)

    def ld_and_print_diff(self,a,b):
        """
        调整a,b顺序，保证矩阵为宽矩阵
        """
        if len(a) > len(b):
            a,b = b,a
        self.ld_mat = np.mat(np.zeros(len(a)*len(b)).reshape(len(a),len(b))).tolist()
        print(self.ld_and_mat(a,b))
        print(self.ld_mat)
        self.print_diff(a,b)

if __name__ == '__main__':
    ld_object = LD()
    ld_object.ld_and_print_diff("AGGTC","AAAGGGTTTCC")
    ld_object.ld_and_print_diff("AAAA","112256")
    ld_object.ld_and_print_diff("GGATCGA","GAATTCAGTTA")
    ld_object.ld_and_print_diff("GAATTCAGTTA","GGATCGA")