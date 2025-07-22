from linked_list.linked_list import LinkedList


ll = LinkedList(value=10)

ll.append(value=20)
ll.append(value=30)
ll.append(value=40)

ll.print_list()

print(f"Popped Node: {ll.pop()}")
print(f"Popped Node: {ll.pop()}")

ll.print_list()

print(f"List Length: {ll.length}")

ll.prepend(value=50)

ll.print_list()

print(f"List Length: {ll.length}")

first_node = ll.pop_first()

print(f"First Node Popped: {first_node.value if first_node else None}")

ll.print_list()

search_node = ll.get_value(1)

print(f"Search node: {search_node.value if search_node else None}")

ll.set_value(1, "test")

updated_node = ll.get_value(1)

print(f"Updated node: {updated_node.value if search_node else None}")

ll.print_list()
