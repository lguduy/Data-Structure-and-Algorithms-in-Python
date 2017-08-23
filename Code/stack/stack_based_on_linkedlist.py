# -*- coding: utf-8 -*-
"""
Created on 2017/02/27 21:12

@author: lguduy

# Data Structure and Algorithms in Python
## Chapter 5
### Stack and Queue
#### Stack

基于链接表技术和节点类实现栈
"""

# 添加自己的搜索目录，在程序运行后失效
import sys
sys.path.append('/home/liangyu/Python/Data-Structure-and-Algorithms-in-Python')

from Code.linkedlist.linkedlist import LNode
from stack_based_on_list import StackUnderFlow


class LStack(object):
    """基于链接表技术和节点类实现栈"""
    def __init__(self):
        self._peek = None

    def is_empty(self):
        return self._peek == None

    def push(self, elem):
        self._peek = LNode(elem, self._peek)

    def peek(self):
        if self.is_empty():
            raise StackUnderFlow("peek() error")

        return self._peek.elem

    def pop(self):
        if self.is_empty():
            raise StackUnderFlow("pop() error")

        elem = self._peek.elem
        self._peek = self._peek.next
        return elem


# Test
if __name__ == '__main__':
    stack = LStack()
    print stack.is_empty()
    stack.push(1)
    stack.push(2)
    print stack.peek()
    print stack.pop()
    print stack.is_empty()
    print stack.pop()
    print stack.is_empty()
