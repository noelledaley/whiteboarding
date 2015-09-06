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


### Examples ###

animals = LinkedList()
dog = Node('dog')
cat = Node('cat')
bird = Node('bird')
cow = Node('cow')

animals.head = dog
dog.next = cat
cat.next = bird
bird.next = cow

cities = LinkedList()
berkeley = Node('berkeley')
oakland = Node('oakland')
seattle = Node('seattle')
portland = Node('portland')

cities.head = berkeley
berkeley.next = oakland
oakland.next = seattle
seattle.next = portland
portland.next = oakland
