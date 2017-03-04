# -*- coding: utf-8 -*-
"""
Created on 2017/03/04 11:15

@author: lguduy

# Data Structure and Algorithms in Python
## Chapter 3
### Linked List 链表

循环单链表
定义表尾指针，表尾指针所指的节点指向首节点实现循环
"""

from linkedlist import LNode
from linkedlist import LinkedListUnderflow


class LClist(object):
    """定义循环单链表类"""
    def __init__(self):
        """初始化方法"""
        self._rear = None    # 表尾指针

    def is_empty(self):
        """链表是否为空"""
        return self._rear is None

    def clear(self):
        """清除链表"""
        self._rear = None

    def pre_insert(self, elem):
        """首端插入"""
        if self._rear is None:
            self._rear = LNode(elem)
            # 只有一个元素时，还要把表尾指针指向自己
            self._rear.next = self._rear
        else:
            p = LNode(elem, self._rear.next)
            self._rear.next = p

    def last_insert(self, elem):
        """尾端插入"""
        if self._rear is None:
            self._rear = LNode(elem)
            # 只有一个元素时，还要把表尾指针指向自己
            self._rear.next = self._rear
        else:
            p = LNode(elem, self._rear.next)
            self._rear.next = p
            self._rear = p

    def pre_pop(self):
        """首端删除"""
        if self._rear is None:
            raise LinkedListUnderflow("pre_pop error")
        elif self._rear.next == self._rear:
            e = self._rear.elem
            self._rear = None
        else:
            p = self._rear.next
            e = p.elem
            self._rear.next = p.next
            p = None

        return e

    def last_pop(self):
        """尾端删除"""
        if self._rear is None:
            raise LinkedListUnderflow("last_pop error")
        elif self._rear == self._rear.next:
            e = self._rear.elem
            self._rear = None
        else:
            p = self._rear.next  # 首节点
            while p.next != self._rear:
                p = p.next

            e = self._rear.elem
            p.next = self._rear.next
            self._rear = p

        return e

    def elems(self):
        """定义链表元素迭代器"""
        if self.is_empty():
            return

        p = self._rear.next  # 首节点
        while p != self._rear:
            yield p.elem
            p = p.next
        yield p.elem

    def printall(self):
        """输出所有元素"""
        for elem in self.elems():
            print elem


# Test
if __name__ == '__main__':
    cllist = LClist()
    print cllist.is_empty()
    cllist.pre_insert(1)
    print cllist.is_empty()
    cllist.printall()
    cllist.last_insert(2)
    cllist.printall()
    print cllist.pre_pop()
    print cllist.last_pop()
    cllist.pre_pop()
