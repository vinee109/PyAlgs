__author__ = "Vineet Jain"

import unittest
from list import ListNode
from list import SLinkedList
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
        slist.insertEnd(1)
        slist.insertEnd(2)
        slist.insertEnd(3)
        expected = "[ 1 2 3 ]"
        actual = str(slist)
        self.assertEqual(expected, actual, expected_str(expected, actual))


if __name__ == '__main__':
    unittest.main()
