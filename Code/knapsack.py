# -*- coding: utf-8 -*-
"""
Created on 2017/02/27 21:12

@author: lguduy

# Data Structure and Algorithms in Python
## Chapter 5
### Stack and Queue
#### Stack

01背包问题

？？？还没有完全想清楚
"""
vlist = [5, 4, 3]
wlist = [20, 10, 12]
C = 10
number = len(vlist)  # 物品数量
res = [[-1 for i in xrange(C+1)] for j in xrange(number+1)]
for i in xrange(1, number+1):
    for j in xrange(C+1):
        if j > vlist[i-1]:
            res[i][j] = max(res[i-1][j], res[i-1][j-vlist[i-1]] + wlist[i-1])
