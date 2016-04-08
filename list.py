"""
TODO: description of list.py
"""
__author__ = "Vineet Jain"


class ListNode:
    """
    Implementation of a generic node in a linked list
    """
    def __init__(self, x, prev=None, next=None):
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
        return "{}".format(self.val)

    def __repr__(self):
        return str(self)


class LinkedList:
    """
    Interface of LinkedList
    """

    def isEmpty(self):
        raise NotImplementedError()



class SLinkedList(LinkedList):
    """
    Implementation of a Singly Linked List
    """
    def __init__(self):
        self.head = None
        self.tail = None
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
        if self.isEmpty():
            self.head = ListNode(x)
            self.tail = self.head
        else:
            self.tail.next = ListNode(x)
            self.tail = self.tail.next
        self.size += 1

    def removeEnd(self):
        """
        Removes the item at the end of the linked list
        :return: The item that was removed, None if the list is empty
        """
        if self.isEmpty():
            return None
        else:
            if self.size == 1:
                to_return = self.head.val
                self.head, self.tail = None, None
                self.size -= 1
                return to_return
            else:
                node = self.head
                while node.next.next != None:
                    node = node.next
                to_return = node.next.val
                node.next = None
                self.size -= 1
                return to_return


    def __str__(self):
        node = self.head
        strs = []
        while node:
            strs.append(str(node))
            node = node.next
        return " ".join(["["] + strs + ["]"])


    def __repr__(self):
        return str(self)
