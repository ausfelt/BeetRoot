class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class UnorderedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __getitem__(self, index):
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        current = self.head
        for i in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, item):
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        current = self.head
        for i in range(index):
            current = current.next
        current.data = item

    def __delitem__(self, index):
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for i in range(index - 1):
            current = current.next
        current.next = current.next.next

    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def index(self, item):
        current = self.head
        index = 0
        while current:
            if current.data == item:
                return index
            current = current.next
            index += 1
        raise ValueError("Item not found in list")

    def pop(self, index=None):
        if index is None:
            index = len(self) - 1
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        if index == 0:
            data = self.head.data
            self.head = self.head.next
            return data
        current = self.head
        for i in range(index - 1):
            current = current.next
        data = current.next.data
        current.next = current.next.next
        return data

    def insert(self, index, item):
        new_node = Node(item)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for i in range(index - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def slice(self, start, stop):
        if start < 0 or start >= len(self):
            raise ValueError("Invalid start index")
        if stop <= start or stop > len(self):
            raise ValueError("Invalid stop index")
        new_list = UnorderedList()
        current = self.head
        for i in range(stop):
            if i >= start:
                new_list.append(current.data)
            current = current.next
        return new_list
