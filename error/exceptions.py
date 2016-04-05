"""
TODO: insert description
"""
__author__ = "Vineet Jain"

class RemoveFromEmpty(Exception):
    def __init__(self, message):
        super(RemoveFromEmpty, self).__init__(message)
