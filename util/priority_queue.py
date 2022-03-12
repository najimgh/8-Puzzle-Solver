import heapq
"""
Using heapq to build a priority queue as
the heapq already has functionalities similar to a priority queue.
"""

class PriorityQueue:
    """
    PriorityQueue class will be used in Informed Search algorithms.
    """

    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        """
        Pushing the tuple (priority, item) onto self.elements list.
        """
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        """
        Popping the element with the minimum priority value (i.e Highest priority).
        We specify the index to be 1 because we are getting from the tuple (priority, item).
        Therefore, we are popping the item.
        """
        if self.elements:
            return heapq.heappop(self.elements)[1]
        else:
            print("No more elements to get in Priority Queue")

    def __str__(self):
        return str(self.elements)