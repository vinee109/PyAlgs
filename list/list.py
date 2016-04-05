"""
TODO: description of list.py
"""
__author__ = "Vineet Jain"

from error.exceptions import RemoveFromEmpty

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
        self.next = next

    def __str__(self):
        return "{}".format(x)

    def __repr__(self):
        return str(self)


class LinkedList:
    """
    Interface of LinkedList
    """

    def isEmpty(self):
        raise NotImplementedError()



class SLinkedlist(LinkedList):
    """
    Implementation of a Singly Linked List
    """
    def __init__(self):
        self.dummy = ListNode(None)
        self.head = None
        self.tailprev = None
        self.size = 0

    def isEmpty(self):
        """
        Returns whether this linked list is empty or not
        :return: True if this Linked List is empty, False otherwise
        """
        return self.size == 0

    def insertEnd(self, x):
        """
        Inserts an item to the end of the linked list
        :param x: the item we want to insert
        """
        if not self.dummy.next:
            self.dummy.next = ListNode(x)
            self.head = self.dummy.next
            self.tailprev = self.dummy
        else:
            self.tailprev.next = ListNode(x)
            self.tailprev = self.tailprev.next
        self.size += 1

    def __str__(self):
        node = self.head
        strs = []
        while node:
            strs.append(str(node))
        return " ".join(["["] + strs + ["]"])


    def __repr__(self):
        return str(self)