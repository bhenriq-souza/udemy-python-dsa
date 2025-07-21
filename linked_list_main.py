from linked_list.linked_list import LinkedList


new_linked_list = LinkedList(value=10)

new_linked_list.append(value=20)
new_linked_list.append(value=30)
new_linked_list.append(value=40)

new_linked_list.print_list()

print(f"Popped Node: {new_linked_list.pop()}")
print(f"Popped Node: {new_linked_list.pop()}")

new_linked_list.print_list()

print(f"List Length: {new_linked_list.length}")

new_linked_list.prepend(value=50)

new_linked_list.print_list()

print(f"List Length: {new_linked_list.length}")