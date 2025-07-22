import unittest

from io import StringIO
from unittest.mock import patch

from linked_list.linked_list import LinkedList


class LinkedListUnitTests(unittest.TestCase):
    def test_linked_list_initialization(self):
        ll: LinkedList = LinkedList(3)

        self.assertEqual(ll.head.value, 3)
        self.assertEqual(ll.tail.value, 3)
        self.assertEqual(ll.length, 1)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_list(self, mock_stdout):
        linked_list = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)

        linked_list.print_list()

        expected_output = '1\n2\n3\n'
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_add_to_empty_list(self):
        ll: LinkedList = LinkedList(1)

        ll.append(2)

        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 2)
        self.assertEqual(ll.length, 2)

    def test_add_multiple_elements(self):
        ll: LinkedList = LinkedList(1)

        ll.append(2)

        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 2)
        self.assertEqual(ll.length, 2)

        ll.append(3)

        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 3)
        self.assertEqual(ll.length, 3)

    def test_add_to_empty_list_with_tail(self):
        ll: LinkedList = LinkedList(1)

        ll.empty_list()

        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)
        self.assertEqual(ll.length, 0)

        ll.append(2)

        self.assertEqual(ll.head.value, 2)
        self.assertEqual(ll.tail.value, 2)
        self.assertEqual(ll.length, 1)

    def test_pop_from_empty_list(self):
        ll: LinkedList = LinkedList(1)

        ll.empty_list()

        self.assertEqual(ll.head, None)
        self.assertEqual(ll.tail, None)
        self.assertEqual(ll.length, 0)

        none_pop = ll.pop()
        self.assertIsNone(none_pop)

    def test_pop_from_single_element_list(self):
        ll: LinkedList = LinkedList(1)

        popped_node = ll.pop()

        self.assertEqual(popped_node.value, 1)
        self.assertEqual(ll.head, None)
        self.assertEqual(ll.tail, None)
        self.assertEqual(ll.length, 0)

    def test_pop_from_multiple_elements_list(self):
        ll: LinkedList = LinkedList(1)

        ll.append(2)
        ll.append(3)

        popped_node = ll.pop()
        self.assertEqual(popped_node.value, 3)
        self.assertEqual(ll.tail.value, 2)
        self.assertEqual(ll.length, 2)

        popped_node = ll.pop()
        self.assertEqual(popped_node.value, 2)
        self.assertEqual(ll.tail.value, 1)
        self.assertEqual(ll.length, 1)

    def test_prepend_to_empty_list(self):
        ll: LinkedList = LinkedList(1)

        ll.empty_list()

        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)
        self.assertEqual(ll.length, 0)

        ll.prepend(2)

        self.assertEqual(ll.head.value, 2)
        self.assertEqual(ll.tail.value, 2)
        self.assertEqual(ll.length, 1)

    def test_prepend_to_non_empty_list(self):
        ll: LinkedList = LinkedList(1)

        ll.append(2)
        ll.append(3)

        ll.prepend(0)

        self.assertEqual(ll.head.value, 0)
        self.assertEqual(ll.tail.value, 3)
        self.assertEqual(ll.length, 4)

        current = ll.head
        values = []
        while current:
            values.append(current.value)
            current = current.next

        self.assertEqual(values, [0, 1, 2, 3])

    def test_pop_first_from_empty_list(self):
        ll: LinkedList = LinkedList(1)

        ll.empty_list()

        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)
        self.assertEqual(ll.length, 0)

        first_node = ll.pop_first()
        self.assertIsNone(first_node)

    def test_pop_first_from_single_element_list(self):
        ll: LinkedList = LinkedList(1)

        first_node = ll.pop_first()

        self.assertEqual(first_node.value, 1)
        self.assertIsNone(first_node.next)
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)
        self.assertEqual(ll.length, 0)

    def test_pop_first_from_multiple_elements_list(self):
        ll: LinkedList = LinkedList(1)

        ll.append(2)
        ll.append(3)

        first_node = ll.pop_first()
        self.assertEqual(first_node.value, 1)
        self.assertEqual(ll.head.value, 2)
        self.assertEqual(ll.tail.value, 3)
        self.assertEqual(ll.length, 2)

        first_node = ll.pop_first()
        self.assertEqual(first_node.value, 2)
        self.assertEqual(ll.head.value, 3)
        self.assertEqual(ll.tail.value, 3)
        self.assertEqual(ll.length, 1)

        first_node = ll.pop_first()
        self.assertEqual(first_node.value, 3)
        self.assertIsNone(first_node.next)
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)
        self.assertEqual(ll.length, 0)
    
    def test_get_value_from_empty_list(self):
        ll: LinkedList = LinkedList(1)

        ll.empty_list()

        node = ll.get_value(0)
        self.assertIsNone(node)
    
    def test_get_value_from_single_element_list(self):
        ll: LinkedList = LinkedList(1)

        node = ll.get_value(0)

        self.assertEqual(node.value, 1)
        self.assertIsNone(node.next)

    def test_get_value_with_negative_index(self):
        ll: LinkedList = LinkedList(1)

        node = ll.get_value(-1)
        self.assertIsNone(node)

    def test_get_value_with_index_greater_then_length(self):
        ll: LinkedList = LinkedList(1)

        node = ll.get_value(3)
        self.assertIsNone(node)
    
    def test_get_value_from_multiple_elements_list(self):
        ll: LinkedList = LinkedList(1)

        ll.append(2)
        ll.append(3)

        node = ll.get_value(2)
        self.assertEqual(node.value, 3)
    
    def test_set_value_to_empty_list(self):
        ll: LinkedList = LinkedList(1)

        ll.empty_list()

        node = ll.set_value(1, "test")
        self.assertFalse(node)
    
    def test_set_value_to_index_greater_then_length(self):
        ll: LinkedList = LinkedList(1)

        result = ll.set_value(3, "test")
        self.assertFalse(result)
    
    def test_set_value_to_list(self):
        ll: LinkedList = LinkedList(1)

        result = ll.set_value(0, "test")
        self.assertTrue(result)

        node = ll.get_value(0)
        self.assertEqual(node.value, "test")
        self.assertIsNone(node.next)
        self.assertEqual(ll.length, 1)
    
    def test_set_value_from_multiple_elements_list(self):
        ll: LinkedList = LinkedList(1)

        ll.append(2)
        ll.append(3)

        result = ll.set_value(2, 4)
        self.assertTrue(result)

        node = ll.get_value(2)
        self.assertEqual(node.value, 4)


if __name__ == '__main__':
    unittest.main()
