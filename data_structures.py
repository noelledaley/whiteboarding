class LinkedList(object):
    """A sequence of Nodes."""

    def __init__(self):
        self.head = None


class Node(object):
    """A basic unit of a LinkedList or Tree."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "<Node data: %s>" % self.data
