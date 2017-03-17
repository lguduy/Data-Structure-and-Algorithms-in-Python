# -*- coding: utf-8 -*-
"""
Created on 2017/02/27 21:12

@author: lguduy

# Data Structure and Algorithms in Python
## Chapter 3
### LinkedList 链表
#### 双向链表

1. 基于单链接节点类实现双链接节点类
2. 基于单链表类(带表尾指针)实现双向链表类
"""

from linkedlist import LNode
from linkedlist import LinkedListUnderflow
from linkedlist1 import LList1


class DLNode(LNode):
    """定义双向链接节点类"""
    def __init__(self, elem, next_=None, pre=None):
        """基于单链接节点类实现双链接节点类"""
        # 调用基类初始化方法
        super(DLNode, self).__init__(elem, next_)
        self.pre = pre    # 指向前一个节点的指针


class DLList(LList1):
    """双向链表"""
    def __init__(self):
        """初始化方法"""
        # 调用基类的初始化方法
        super(DLList, self).__init__()  # 表头和表尾指针

    def pre_insert(self, elem):
        """重新定义首端插入"""
        if self._head is None:
            self._head = DLNode(elem)
            self._rear = self._head
        else:
            p = DLNode(elem, self._head)
            self._head.pre = p
            self._head = p

    def last_insert(self, elem):
        """重新定义尾端插入"""
        if self._head is None:
            self._head = DLNode(elem)
            self._rear = self._head
        else:
            p = DLNode(elem, pre=self._rear)
            self._rear.next = p
            self._rear = p

    def pre_pop(self):
        """重新定义首端删除"""
        # 空表
        if self._head is None:
            raise LinkedListUnderflow("pre_pop error")
        # 表中只有一个元素
        elif self._head == self._rear:
            e = self._head.elem
            self._head = None
        # 一般情况
        else:
            e = self._head.elem
            self._head = self._head.next
            self._head.pre = None
        return e

    def last_pop(self):
        """重新定义尾端删除"""
        # 空表
        if self._head is None:
            raise LinkedListUnderflow("last_pop error")
        # 表中只有一个元素
        elif self._head == self._rear:
            e = self._head.elem
            self._head = None
        # 一般情况
        else:
            e = self._rear.elem
            self._rear = self._rear.pre
            self._rear.next = None
        return e

    def reverse(self):
        """双向链表反转"""
        if self._head is None:
            return
        # 两两交换节点中的元素
        p, q = self._head, self._rear   # 控制循环的变量
        while True:
            p.elem, q.elem = q.elem, p.elem
            if p.next == q or p == q:   # 跳出循环
                break
            p, q = p.next, q.pre    # 改变循环条件


# Test
if __name__ == '__main__':
    dllist = DLList()
    for i in xrange(10):
        dllist.pre_insert(i)
    dllist.printall()
    print "\n"
    # reverse
    dllist.reverse()
    dllist.printall()
