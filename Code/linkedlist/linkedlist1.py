# -*- coding: utf-8 -*-
"""
Created on 2017/03/02 10:52

@author: lguduy

# Data Structure and Algorithms in Python
## Chapter 3
### Linked List 链表

单链表的简单变形
引入表尾指针，感觉并没有带来便利
"""

from linkedlist import LNode
from linkedlist import LinkedListUnderflow
from linkedlist import LList


class LList1(LList):
    """单链表简单变形
    引入表尾指针
    继承自单链表类
    """
    def __init__(self):
        """初始化方法"""
        # 调用 LList 的初始化方法
        super(LList1, self).__init__()
        self._rear = None    # 初始化尾节点引用域（表尾指针）

    def pre_insert(self, elem):
        """重新定义首端插入
        表尾指针也要修改
        """
        if self._head is None:    # 空表
            self._head = LNode(elem)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)

    def last_insert(self, elem):
        """重新定义尾端插入元素"""
        if self._head is None:
            self._head = LNode(elem)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

    def last_pop(self):
        """重新定义尾端删除"""
        # 空表
        if self._head is None:
            raise LinkedListUnderflow("last_pop error")
        # 一个元素
        elif self._head == self._rear:
            e = self._head.elem
            self._head = None
        # 一般情况
        else:
            pre = self.find_node(self.length()-2)
            e = pre.next.elem
            pre.next = None
            self._rear = pre

        return e


# Test
if __name__ == "__main__":
    # 建立空链表对象
    llist = LList1()
    # 是否为空
    print llist.is_empty()
    # 首端插入
    for i in xrange(10):
        llist.pre_insert(i)
    print llist.is_empty()
    # 输出所有元素
    llist.printall()
    # 首端删除
    print "首端删除的元素：{}".format(llist.pre_pop())
    # 链表长度
    print "链表长度：{}".format(llist.length())
    # 按下标索引
    print "下标为0的元素值：{}".format(llist.find_index(0))
    # 按元素索引
    print "元素0的下标：{}".format(llist.find_value(0))
    # 尾端插入
    llist.last_insert(9)
    llist.printall()
    # 尾端删除
    print "尾端删除的元素：{}".format(llist.last_pop())
    # insert
    llist.insert(0, 9)
    print "下标为0的元素值：{}".format(llist.find_index(0))
    llist.insert(10, 9)
    print "下标为10的元素值：{}".format(llist.find_index(10))
    llist.insert(5, 9)
    print "下标为5的元素值：{}".format(llist.find_index(5))
    llist.printall()
    # pop
    print "定点删除"
    print llist.pop(0)
    print llist.pop(4)
    print llist.pop(9)
    # clear
    print llist.is_empty()
    llist.clear()
    print llist.is_empty()
    llist1 = LList1()
    llist1.pre_insert(1)
    print llist1.last_pop()
    llist1.last_pop()
