class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class Deque:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_left(self, value):

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

        self.size += 1

    def push_right(self, value):

        new_node = Node(value)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

        self.size += 1

    def pop_left(self):

        if self.head is None:
            raise IndexError("Deque is empty")

        value = self.head.value

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None

        self.size -= 1
        return value

    def pop_right(self):

        if self.tail is None:
            raise IndexError("Deque is empty")

        value = self.tail.value

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None

        self.size -= 1
        return value

    def print_deque(self):

        current = self.head

        while current:
            print(current.value, end=" <-> ")
            current = current.next

        print("None")


def main():

    deque = Deque()

    deque.push_left("B")
    deque.push_left("A")
    deque.push_right("C")
    deque.push_right("D")

    print("Deque:")
    deque.print_deque()

    print(f"Pop Left: {deque.pop_left()}")
    print(f"Pop Right: {deque.pop_right()}")

    print("Deque after pops:")
    deque.print_deque()


if __name__ == "__main__":
    main()