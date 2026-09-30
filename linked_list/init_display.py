class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def init_list(count: int) -> Node | None:
    if count <= 0:
        return None

    head = Node()
    current = head

    for _ in range(count - 1):
        current.next = Node()
        current = current.next

    return head


def print_list(head: Node | None = None) -> None:
    elements = []
    current = head

    while current:
        elements.append(current)
        current = current.next

    print(*elements)


list_head = init_list(5)
print_list(list_head)
