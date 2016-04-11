__author__ = "Vineet Jain"

import unittest
from linkedlist import ListNode
from linkedlist import SLinkedList
from test_utils import expected_str

class TestStringMethods(unittest.TestCase):
    """
    Testing the string methods
    """
    def testListNodeStr(self):
        node = ListNode("1")
        expected = "1"
        actual = str(node)
        self.assertEqual(expected, actual, expected_str(expected, actual))

    def testSLinkedListStr(self):
        slist = SLinkedList()
        expected, actual = "[ ]", str(slist)
        self.assertEqual(expected, actual, expected_str(expected, actual))
        slist.insertEnd(1)
        slist.insertEnd(2)
        slist.insertEnd(3)
        expected, actual = "[ 1 2 3 ]", str(slist)
        self.assertEqual(expected, actual, expected_str(expected, actual))


class TestSLinkedList(unittest.TestCase):
    """
    Testing insertend, removeEnd and isEmpty methods
    """
    def testIsEmpty(self):
        slist = SLinkedList()
        self.assertTrue(slist.isEmpty(), expected_str(True, False))
        slist.insertEnd(1)
        self.assertFalse(slist.isEmpty(), expected_str(False, True))
        slist.insertEnd(2)
        self.assertFalse(slist.isEmpty(), expected_str(False, True))
        slist.removeEnd()
        slist.removeEnd()
        self.assertTrue(slist.isEmpty(), expected_str(True, False))

    def testInsert(self):
        slist = SLinkedList()
        slist.insertEnd(1)
        self.assertEqual(1, slist.size, expected_str(1, slist.size))
        self.assertEqual("[ 1 ]", str(slist), expected_str("[ 1 ]", str(slist)))
        slist.insertEnd(2)
        self.assertEqual(2, slist.size, expected_str(2, slist.size))
        self.assertEqual("[ 1 2 ]",
                         str(slist),
                         expected_str("[ 1 2 ]", str(slist)))
        slist.insertEnd(3)
        self.assertEqual(3, slist.size, expected_str(3, slist.size))
        self.assertEqual("[ 1 2 3 ]",
                         str(slist),
                         expected_str("[ 1 2 3 ]", str(slist)))

    def testRemove(self):
        slist = SLinkedList()
        slist.insertEnd(1)
        slist.insertEnd(2)
        slist.insertEnd(3)

        self.assertEqual(3, slist.size, expected_str(3, slist.size))
        self.assertEqual("[ 1 2 3 ]",
                         str(slist),
                         expected_str("[ 1 2 3 ]", str(slist)))
        self.assertEqual(slist.removeEnd(), 3)
        self.assertEqual(2, slist.size, expected_str(2, slist.size))
        self.assertEqual("[ 1 2 ]",
                         str(slist),
                         expected_str("[ 1 2 ]", str(slist)))
        self.assertEqual(slist.removeEnd(), 2)
        self.assertEqual(1, slist.size, expected_str(1, slist.size))
        self.assertEqual("[ 1 ]", str(slist), expected_str("[ 1 ]", str(slist)))
        self.assertEqual(slist.removeEnd(), 1)
        self.assertEqual(0, slist.size, expected_str(0, slist.size))
        self.assertEqual("[ ]", str(slist), expected_str("[ ]", str(slist)))


if __name__ == '__main__':
    unittest.main()
