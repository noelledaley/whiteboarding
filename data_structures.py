class LinkedList(object):

    def __init__(self):
        self.head = None


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "<Node data: %s>" % self.data
