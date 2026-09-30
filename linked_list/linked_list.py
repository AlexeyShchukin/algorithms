class Node:
    """Класс для представления узла связанного списка"""
    def __init__(self, data):
        self.data = data  # Данные, хранящиеся в узле
        self.next = None  # Ссылка на следующий узел


class LinkedList:
    """Класс для представления односвязного списка"""
    def __init__(self):
        self.head = None  # Указатель на первый узел списка (голова)

    def append(self, data):
        """Добавление нового узла в конец списка"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        """Отображение всех элементов списка"""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def remove(self, data):
        """Удаление узла с определенными данными"""
        current = self.head

        # Если нужно удалить голову
        if current and current.data == data:
            self.head = current.next
            return

        # Поиск узла для удаления
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        # Если узел не найден
        if current is None:
            print("Элемент не найден")
            return

        # Удаление узла
        prev.next = current.next

    def search(self, data):
        """Поиск элемента в списке"""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False


# Пример использования
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    print("Связанный список после добавления элементов:")
    linked_list.display()

    print("\nПоиск элемента 20:", linked_list.search(20))
    print("Поиск элемента 40:", linked_list.search(40))

    linked_list.remove(20)
    print("\nСвязанный список после удаления элемента 20:")
    linked_list.display()