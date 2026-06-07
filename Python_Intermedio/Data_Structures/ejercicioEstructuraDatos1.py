class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Stack:
  def __init__(self):
    self.head = None
    self.size = 0

  def push(self, value):
    new_node = Node(value)
    if self.head:
      new_node.next = self.head
    self.head = new_node
    self.size += 1

  def pop(self):
    if self.is_empty():
      raise IndexError("Stack is empty")
    popped_node = self.head
    self.head = self.head.next
    self.size -= 1
    return popped_node.value

  def peek(self):
    if self.is_empty():
      return "Stack is empty"
    return self.head.value

  def is_empty(self):
    return self.size == 0

  def stack_size(self):
    return self.size

  def traverse_and_print(self):
    current_node = self.head
    while current_node:
      print(current_node.value, end=" -> ")
      current_node = current_node.next
    print("None")

def main():
    myStack = Stack()
    myStack.push('A')
    myStack.push('B')
    myStack.push('C')

    print("LinkedList: ", end="")
    myStack.traverse_and_print()
    print("Peek: ", myStack.peek())
    print("Pop: ", myStack.pop())
    print("LinkedList after Pop: ", end="")
    myStack.traverse_and_print()
    print("isEmpty: ", myStack.is_empty())
    print("Size: ", myStack.stack_size())

if __name__ == '__main__':
    main()