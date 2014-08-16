from linked_list import *
import unittest

class LinkedListTest(unittest.TestCase):
    def setUp(self):
        self.node1 = Node(1)
        self.node2 = Node(2)
        self.node3 = Node(3)
        self.node4 = Node(4, self.node1)
        self.node5 = Node(5, self.node3)
        self.mylist = LinkedList(0)

    def test_single_list(self):
        self.assertEqual(self.mylist.head.value, 0)
        self.assertEqual(self.mylist.head.next, None)
        self.assertEqual(self.mylist.__str__(), '0')
        self.assertEqual(self.mylist.head.__str__(), '0')

    def test_nodes(self):
        self.assertEqual(self.node1.value, 1)
        self.assertEqual(self.node1.next, None)
        self.assertEqual(self.node4.next, self.node1)
        self.assertEqual(self.node4.next.value, 1)
        self.assertEqual(self.node1.__str__(), '1')

    def test_length(self):
        self.assertEqual(self.mylist.length(), 1)
        self.mylist.addNode(1)
        self.mylist.addNode(2)
        self.mylist.addNode(3)
        self.assertEqual(self.mylist.length(), 4)
        self.mylist.addNodeAsNode(self.node1)
        self.mylist.addNodeAsNode(self.node4)
        self.assertEqual(self.mylist.length(), 6)

    def test_add_nodes_to_list(self):
        self.mylist.addNodeAsNode(self.node1)
        self.mylist.addNodeAsNode(self.node2)
        self.mylist.addNodeAsNode(self.node3)
        self.assertEqual(self.mylist.head.next, self.node1)
        self.assertEqual(self.mylist.head.next.next, self.node2)
        self.assertEqual(self.mylist.head.next.next.next, self.node3)
        self.assertEqual(self.mylist.head.next.next.next.value, 3)
        self.assertEqual(self.mylist.head.next.next.next.next, None)
        self.assertEqual(self.mylist.__str__(), '0, 1, 2, 3')

    def test_add_ints_to_list(self):
        self.mylist.addNode(1)
        self.mylist.addNode(2)
        self.mylist.addNode(3)
        self.assertEqual(self.mylist.head.next.value, 1)
        self.assertEqual(self.mylist.head.next.next.value, 2)
        self.assertEqual(self.mylist.head.next.next.next.value, 3)
        self.assertEqual(self.mylist.head.next.next.next.next, None)
        self.assertEqual(self.mylist.__str__(), '0, 1, 2, 3')

    def test_make_bad_node(self):
        self.assertEqual(Node('l').value, None)
        self.mylist.addNode('l')
        self.assertEqual(self.mylist.head.next, None)

    def test_cycles(self):
        self.mylist.addNodeAsNode(self.node1)
        self.mylist.addNodeAsNode(self.node2)
        self.mylist.addNodeAsNode(self.node3)
        self.mylist.addNodeAsNode(self.node4)
        self.assertEqual(self.mylist.head.next.next.next.next, self.node4)
        self.assertEqual(self.mylist.head.next.next.next.next.next, self.node1)
        self.assertEqual(self.mylist.__str__(), '0, 1, 2, 3, 4, 1')
        self.assertEqual(self.mylist.addNode(9), None)

    def test_add_node_before(self):
        self.mylist.addNodeAsNode(self.node1)
        self.mylist.addNodeAsNode(self.node2)
        self.mylist.addNodeAsNode(self.node3)
        self.mylist.addNodeAsNode(self.node4)
        self.mylist.addNodeBefore(9, self.node3)
        self.assertEqual(self.mylist.head.next.next.next.value, 9)
        self.assertEqual(self.mylist.__str__(), '0, 1, 2, 9, 3, 4, 1')
        self.assertEqual(self.mylist.addNodeBefore(10, self.node5), None)

    def test_add_node_after(self):
        self.mylist.addNodeAsNode(self.node1)
        self.mylist.addNodeAsNode(self.node2)
        self.mylist.addNodeAsNode(self.node3)
        self.mylist.addNodeAsNode(self.node4)
        self.mylist.addNodeAfter(9, self.node2)
        self.assertEqual(self.mylist.head.next.next.next.value, 9)
        self.assertEqual(self.mylist.__str__(), '0, 1, 2, 9, 3, 4, 1')
        self.assertEqual(self.mylist.addNodeAfter(10, self.node5), None)

    def test_remove_node(self):
        self.mylist.addNodeAsNode(self.node1)
        self.mylist.addNodeAsNode(self.node2)
        self.mylist.addNodeAsNode(self.node3)
        self.mylist.addNodeAsNode(self.node4)
        self.mylist.removeNode(self.node3)
        self.assertEqual(self.mylist.__str__(), '0, 1, 2, 4, 1')
        self.assertEqual(self.mylist.removeNode(self.node5), None)

    def test_remove_node_by_value(self):
        self.mylist.addNodeAsNode(self.node1)
        self.mylist.addNodeAsNode(self.node2)
        self.mylist.addNodeAsNode(self.node3)
        self.mylist.addNodeAsNode(self.node4)
        self.mylist.addNodeAfter(4, self.node2)
        self.mylist.removeNodesByValue(4)
        self.assertEqual(self.mylist.__str__(), '0, 1, 2, 3')

    def test_reverse_list(self):
        self.mylist.addNodeAsNode(self.node1)
        self.mylist.addNodeAsNode(self.node2)
        self.mylist.addNodeAsNode(self.node3)
        self.mylist.reverse()
        self.assertEqual(self.mylist.__str__(), '3, 2, 1, 0')
        self.assertEqual(self.mylist.head, self.node3)

        self.mylist.addNodeAsNode(self.node4)
        hold = self.mylist
        self.mylist.reverse()
        self.assertEqual(hold, self.mylist)

    def test_hasCycle(self):
        self.mylist.addNodeAsNode(self.node1)
        self.mylist.addNodeAsNode(self.node2)
        self.mylist.addNodeAsNode(self.node3)
        self.assertEqual(self.mylist.hasCycle(), False)
        self.mylist.addNodeAsNode(self.node4)
        self.assertEqual(self.mylist.hasCycle(), True)
        self.mylist.removeNode(self.node4)
        self.assertEqual(self.mylist.hasCycle(), False)

if __name__ == '__main__':
    unittest.main()
