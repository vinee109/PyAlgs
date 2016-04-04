"""
TODO: description of list.py
"""
__author__ = "Vineet Jain"

from exceptions import RemoveFromEmpty

class ListNode:
    """
    Implementation of a generic node in a linked list
    """
    def __init__(self, x, prev=None, nxt=None):
        """
        ListNode Constructor
        :param x: the value contained by this node
        :param prev: reference to the node directly before this node
        :param nxt: reference to the next node after this nodes
        :return:
        """
        self.val = x
        self.prev = prev
        self.nxt = nxt


class SLinkedlist:
    """
    Implementation of a Singly Linked List
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insertEnd(self, x):
        """
        Inserts an item to the end of the linked list
        :param x: the item we want to insert
        """
        if self.tail:
            self.tail.next = ListNode(x)
        else:
            self.head = ListNode(x)
            self.tail = self.head
        self.size += 1

