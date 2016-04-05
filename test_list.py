__author__ = "Vineet Jain"

import unittest
from list import SLinkedList

class TestSinglyLinkedList(unittest.TestCase):

  def test_basic(self):
      slist = SLinkedList()
      self.assertTrue(slist.isEmpty())

if __name__ == '__main__':
    unittest.main()
