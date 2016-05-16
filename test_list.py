import unittest
from linkedlist import ListNode
from linkedlist import SLinkedList
from linkedlist import DLinkedList
from test_utils import expected_str

__author__ = "Vineet Jain"


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


class TestLinkedList(unittest.TestCase):
    """
    Testing insertend, removeEnd and isEmpty methods
    """
    def runTestIsEmpty(self, lst):
        self.assertTrue(lst.isEmpty(), expected_str(True, False))
        lst.insertEnd(1)
        self.assertFalse(lst.isEmpty(), expected_str(False, True))
        lst.insertEnd(2)
        self.assertFalse(lst.isEmpty(), expected_str(False, True))
        lst.removeEnd()
        lst.removeEnd()
        self.assertTrue(lst.isEmpty(), expected_str(True, False))

    def runTestInsertEnd(self, lst):
        lst.insertEnd(1)
        self.assertEqual(1, lst.size, expected_str(1, lst.size))
        self.assertEqual("[ 1 ]", str(lst), expected_str("[ 1 ]", str(lst)))
        lst.insertEnd(2)
        self.assertEqual(2, lst.size, expected_str(2, lst.size))
        self.assertEqual("[ 1 2 ]",
                         str(lst),
                         expected_str("[ 1 2 ]", str(lst)))
        lst.insertEnd(3)
        self.assertEqual(3, lst.size, expected_str(3, lst.size))
        self.assertEqual("[ 1 2 3 ]",
                         str(lst),
                         expected_str("[ 1 2 3 ]", str(lst)))

    def runTestRemoveEnd(self, lst):
        lst.insertEnd(1)
        lst.insertEnd(2)
        lst.insertEnd(3)

        self.assertEqual(3, lst.size, expected_str(3, lst.size))
        self.assertEqual("[ 1 2 3 ]",
                         str(lst),
                         expected_str("[ 1 2 3 ]", str(lst)))
        self.assertEqual(lst.removeEnd(), 3)
        self.assertEqual(2, lst.size, expected_str(2, lst.size))
        self.assertEqual("[ 1 2 ]",
                         str(lst),
                         expected_str("[ 1 2 ]", str(lst)))
        self.assertEqual(lst.removeEnd(), 2)
        self.assertEqual(1, lst.size, expected_str(1, lst.size))
        self.assertEqual("[ 1 ]", str(lst), expected_str("[ 1 ]", str(lst)))
        self.assertEqual(lst.removeEnd(), 1)
        self.assertEqual(0, lst.size, expected_str(0, lst.size))
        self.assertEqual("[ ]", str(lst), expected_str("[ ]", str(lst)))


class TestSLinkedList(TestLinkedList):

    def setUp(self):
        self.lst = SLinkedList()

    def testIsEmpty(self):
        self.runTestIsEmpty(self.lst)

    def testInsertEnd(self):
        self.runTestInsertEnd(self.lst)

    def testRemovEnd(self):
        self.runTestRemoveEnd(self.lst)


class TestDLinkedList(TestLinkedList):

    def setUp(self):
        self.lst = DLinkedList()

    def testIsEmpty(self):
        self.runTestIsEmpty(self.lst)

    def testInsertEnd(self):
        self.runTestInsertEnd(self.lst)

    def testRemoveEnd(self):
        self.runTestRemoveEnd(self.lst)


if __name__ == '__main__':
    unittest.main()
