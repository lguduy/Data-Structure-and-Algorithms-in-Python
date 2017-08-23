# -*- coding: utf-8 -*-
"""
Created on 2017/02/27 21:12

@author: lguduy

# Data Structure and Algorithms in Python
## Chapter 3
### LinkedList 链表

实现最简单的单链表

插入排序？？？
"""


class LNode(object):
    """定义节点类"""
    def __init__(self, elem, next_=None):
        """初始化方法
        elem 是当前节点中存的元素
        next_ 是当前节点指向的下一个节点
        """
        self.elem = elem
        self.next = next_


class LinkedListUnderflow(ValueError):
    """定义异常类"""
    pass

class LList(object):
    """定义单链表类"""
    def __init__(self):
        """初始化方法"""
        self._head = None          # 表头指针

    def is_empty(self):
        """链表是否为空"""
        return self._head is None

    def clear(self):
        """清除链表所有元素"""
        self._head = None

    def pre_insert(self, elem):
        """首端插入
        注意：表头指针 _head 要更改
        """
        self._head = LNode(elem, self._head)

    def pre_pop(self):
        """首端删除
        返回删除的元素
        """
        if self._head is None:
            raise LinkedListUnderflow("pre_pop error")

        elem = self._head.elem
        self._head = self._head.next
        return elem

    def length(self):
        """获得链表长度"""
        if self._head is None:
            length = 0
        else:
            p = self._head  # 扫描指针
            i = 1
            while p.next is not None:
                p = p.next
                i += 1

            length = i
        return length   # 单一出口原则

    def find_node(self, k):
        """按下标查找相应节点
        内部方法
        k: 输入下标
        """
        length = self.length()
        if k > length-1 or k < 0:
            raise ValueError("index 值不合法")

        p = self._head
        idx = 0
        while idx < k:
            p = p.next
            idx += 1

        return p

    def find_index(self, k):
        """按下标查找元素，并返回元素值
        k: 输入下标
        """
        p = self.find_node(k)
        return p.elem

    def find_value(self, elem):
        """按值查找元素
        返回找到的第一个元素的下标
        返回-1表示未找到
        elem: 输入值
        """
        p = self._head
        idx = 0
        while p is not None and p.elem != elem:
            p = p.next
            idx += 1

        if p is not None:   # 代表 p.elem == elem
            res = idx
        else:
            res = -1

        return res

    def last_insert(self, elem):
        """尾端插入元素"""
        length = self.length()
        if length == 0:    # 空表
            self._head = LNode(elem)

        pre = self.find_node(length-1)  # 最后一个节点
        pre.next = LNode(elem)

    def last_pop(self):
        """尾端删除
        1. 空表：异常处理
        2. 只有一个元素：修改表头指针 _head
        """
        length = self.length()

        # 空表
        if length == 0:
            raise LinkedListUnderflow("last_pop erro")
        # 只有一个元素
        elif length == 1:
            e = self._head.elem
            self._head = None
        # 一般情况
        else:
            pre = self.find_node(length-2)
            e = pre.next.elem
            pre.next = None

        return e

    def insert(self, index, elem):
        """定点插入
        elem: 元素值
        index: 下标值
        1. 首端插入
        2. 尾端插入
        3. 一般位置插入"""
        length = self.length()
        # 参数检查
        if index < 0 or index > length:
            raise ValueError("insert 中 index {} 不合法".format(index))

        if index == 0:
            self._head = LNode(elem, self._head)
        elif index == length:
            pre = self.find_node(length-1)
            pre.next = LNode(elem)
        else:
            pre = self.find_node(index-1)     # 前面的一个节点
            new_node = LNode(elem, self.find_node(index))
            pre.next = new_node

    def pop(self, index):
        """定点删除"""
        length = self.length()
        # 参数检查
        if index < 0 or index > length-1:
            raise ValueError("pop 中 index {} 不合法".format(index))

        if length == 0:
            raise LinkedListUnderflow("pop error")
        elif length == 1:
            elem = self._head.elem
            self._head = None
        else:
            if index == 0:             # 首端删除
                elem = self._head.elem
                self._head = self._head.next
            elif index == length-1:    # 尾端删除
                pre = self.find_node(index-1)
                elem = pre.next.elem
                pre.next = None
            else:
                pre = self.find_node(index-1)
                p = pre.next
                elem = p.elem
                pre.next = p.next
                p = None

            return elem

    def reverse(self):
        """单链表反转
        把节点的链接反转
        """
        q = None
        while self._head is not None:
            p = self._head  # 扫描指针
            self._head = p.next
            p.next = q
            q = p
        self._head = q

    def sort(self):
        """插入排序（升序）"""
        # 空表或只有一个元素
        if self._head is None or self._head.next is None:
            return

        rem = self._head.next    # 扫描指针
        self._head.next = None    # 这一步？？？
        while rem is not None:
            p = self._head
            q = None
            while p.elem <= rem.elem and p is not None:
                q = p    # 要插入的位置的前一个位置
                p = p.next   # 确定元素要插入的位置

            if q is None:    # p = self._head, q = None, rem插入到表头
                self._head = rem
            else:
                q.next = rem    # rem插入到p和q之间

            a = rem
            rem = rem.next
            a.next = p

    def elems(self):
        """定义链表元素迭代器"""
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    def printall(self):
        """输出所有元素"""
        for elem in self.elems():
            print elem


# Test
if __name__ == "__main__":
    # 建立空链表对象
    llist = LList()
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

    for i in xrange(10):
        llist.pre_insert(i)
    llist.printall()
    print "\n"
    # reverse
    llist.reverse()
    llist.printall()
    llist.clear()

    # sort
    llist.pre_insert(10)
    llist.pre_insert(20)
    llist.pre_insert(30)
    llist.printall()
    print "\n"
    llist.sort()
    llist.printall()
