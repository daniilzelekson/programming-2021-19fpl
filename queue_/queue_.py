"""
Programming for linguists

Implementation of the data structure "Queue"
"""

from typing import Iterable


# pylint: disable=invalid-name
class Queue_:
    """
    Queue Data Structure
    """

    def __init__(self, data: Iterable = (), max_size_queue: int = float("inf")):
        self.max_size_queue = max_size_queue
        self.data = []
        for element in list(data):
            self.put(element)

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        if self.full():
            raise IndexError
        self.data.append(element)

    def get(self):
        """
        Remove and return an item from queue_
        """
        if self.empty():
            raise IndexError
        result = self.data[0]
        self.data = self.data[1:]
        return result

    def full(self):
        """
        Checks if the queue is full
        """
        return self.max_size_queue == len(self.data)

    def empty(self) -> bool:
        """
        Return whether queue_ is empty or not
        :return: True if queue_ does not contain any elements.
                 False if the queue_ contains elements
        """
        return self.data == []

    def size(self) -> int:
        """
        Return the number of elements in queue_
        :return: Number of elements in queue_
        """
        return len(self.data)

    def top(self):
        """
        Return the element on the top of queue_
        :return: the element that is on the top of queue_
        """
        if self.empty():
            raise IndexError
        return self.data[0]
