# -*- coding: utf-8 -*-
"""
Created on 2017/03/11 21:20

@author: lguduy

# Data Structure and Algorithms in Python
## Chapter 3
### 表的应用
#### Josephus 问题

"""

# 基于顺序表
def Josephus(n, k, m):
    """
    parameters:
    -----------
    n: 共n个人
    k: 从第k个人开始报数
    m: 报m的人退出
    """
    people = range(1, n+1)  # 编号从1到n
    num = n    # 人数
    i = k-1    # 初始下标
    while num > 0:    # 当num == 0,游戏结束
        i = (i + m -1) % num    # 更新出局人的下标
        print "编号：{} 出局\n".format(people.pop(i)) # 弹出出局人编号
        num -= 1


if __name__ == '__main__':
    Josephus(5, 2, 7)
