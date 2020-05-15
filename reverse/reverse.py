class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        """
        Uses recursion to reverse a linked list.

        If node value is None, return None -- there is no list.
        If next node is None, set node as head and return -- at end of list.


        """
        if node is None:
            return None
        if node.next_node is None:
            self.head = node
            return node

        print( "a", self.head.value, ":", node.value, node.next_node.value, node.next_node.next_node)

        nextNode = node.next_node
        
        reverse = self.reverse_list( nextNode, node)

        node.next_node.next_node = node
        node.next_node = reverse
        self.head = node.next_node

        print( "b", self.head.value, ":", node.value, node.next_node.value, node.next_node.next_node.value)
        return node.next_node


test = LinkedList()

test.add_to_head( 1)
test.add_to_head( 2)
test.add_to_head( 3)
test.add_to_head( 4)
test.add_to_head( 5)
test.reverse_list( test.head, None)
