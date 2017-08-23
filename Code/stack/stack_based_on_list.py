# -*- coding: utf-8 -*-
"""
Created on 2017/03/17 15:43

@author: lguduy

# Data Structure and Algorithms in Python
## Chapter 5
### Stack and Queue
#### Stack

基于list实现栈
"""

class StackUnderFlow(ValueError):
    """定义栈底溢出类"""
    pass


class SStack(object):
    """基于list实现stack"""
    def __init__(self):
        self._elems = list()

    def is_empty(self):
        """栈是否为空"""
        return len(self._elems) == 0

    def push(self, elem):
        """元素入栈"""
        self._elems.append(elem)

    def pop(self):
        """元素出栈"""
        if self.is_empty():
            raise StackUnderFlow("pop() error") # 异常处理

        elem = self._elems.pop()
        return elem

    def peek(self):
        """返回栈顶元素"""
        if self.is_empty():
            raise StackUnderFlow("peek() error") # 异常处理

        elem = self._elems[-1]
        return elem


# Test
if __name__ == '__main__':
    stack = SStack()
    print stack.is_empty()
    stack.push(1)
    stack.push(2)
    print stack.peek()
    print stack.pop()
    print stack.is_empty()
    print stack.pop()
    print stack.is_empty()
