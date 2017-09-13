
import numpy as np

class NW(object):
    """
    NW（Needleman/Wunsch）算法基于最长公共子串算法。
    最长公共子串长度反映两个字符串的相似程度
    最长公共子串不需要连续出现，但一定是出现的顺序一致
    如abcd/afcd，最长子串为acd，长度为3
    """

    def __init__(self):
        pass
    
    def nw(self,a,b):
        len_a = len(a)
        len_b  =len(b)
        if min(len_a,len_b) == 0:
            return 0
        if a[len_a-1] == b[len_b-1]:
            return self.nw(a[:len_a-1],b[:len_b-1]) + 1
        else:
            return max(self.nw(a[:len_a-1],b[:len_b-1]),self.nw(a[:len_a],b[:len_b-1]),self.nw(a[:len_a-1],b[:len_b]))

    def nw_and_mat(self,a,b):
        len_a = len(a)
        len_b  =len(b)
        # print(self.nw_mat)
        if min(len_a,len_b) == 0:
            return 0
        if a[len_a-1] == b[len_b-1]:
            # if len_a == 7 and len_b == 11:
            #     print(self.nw_and_mat(a[:len_a-1],b[:len_b-1]) + 1)
            if self.nw_mat[len_a-1][len_b-1] == 0:
                self.nw_mat[len_a-1][len_b-1] = self.nw_and_mat(a[:len_a-1],b[:len_b-1]) + 1
            return self.nw_mat[len_a-1][len_b-1]
        else:
            if self.nw_mat[len_a-1][len_b-1] == 0:
                self.nw_mat[len_a-1][len_b-1] = max((self.nw_and_mat(a[:len_a-1],b[:len_b-1]),self.nw_and_mat(a[:len_a],b[:len_b-1]),self.nw_and_mat(a[:len_a-1],b[:len_b])))
            return self.nw_mat[len_a-1][len_b-1]

    def nw_and_print_diff(self,a,b):
        """
        调整a,b顺序，保证矩阵为宽矩阵
        """
        if len(a) > len(b):
            a,b = b,a
        self.nw_mat = np.mat(np.zeros(len(a)*len(b)).reshape(len(a),len(b))).tolist()
        print(self.nw_and_mat(a,b))
        print(self.nw_mat)
        self.print_diff(a,b)
    def print_diff(self,a,b):
        """
        nw算法编辑差异文本方法与ld算法大同小异，
        最长子串矩阵当前位置左边不为0且大于左上方，左移
        其他情况，向左上角移动

        """
        index_mat_a = len(a) - 1
        index_mat_b = len(b) - 1
        diff_a = ""
        diff_b = ""
        head_flag = 0
        while index_mat_a > 0 and index_mat_b > 0:
            if self.nw_mat[index_mat_a][index_mat_b-1] != 0 and self.nw_mat[index_mat_a][index_mat_b-1] > self.nw_mat[index_mat_a-1][index_mat_b-1]:
                diff_a = "_" + diff_a
                diff_b = b[index_mat_b] + diff_b
                index_mat_a = index_mat_a
                index_mat_b = index_mat_b - 1
            else:
                diff_a = a[index_mat_a] + diff_a
                diff_b = b[index_mat_b] + diff_b
                index_mat_a = index_mat_a - 1
                index_mat_b = index_mat_b - 1
        # print(index_mat_a,index_mat_b)
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

if __name__ == '__main__':
    nw_object = NW()
    # print(nw_object.nw("GGATCGA","GAATTCAGTTA"))
    nw_object.nw_and_print_diff("AAAAA","112256")