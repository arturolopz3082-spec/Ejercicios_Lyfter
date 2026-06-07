class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, value):

        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current_node, new_node):

        if new_node.value < current_node.value:

            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insert_recursive(
                    current_node.left,
                    new_node
                )

        else:

            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insert_recursive(
                    current_node.right,
                    new_node
                )

    def print_tree(self):

        if self.root is None:
            print("Tree is empty")
            return

        self._print_recursive(self.root)

    def _print_recursive(self, node):

        if node is None:
            return

        self._print_recursive(node.left)

        print(node.value)

        self._print_recursive(node.right)


def main():

    tree = BinaryTree()

    tree.insert(50)
    tree.insert(25)
    tree.insert(75)
    tree.insert(10)
    tree.insert(30)
    tree.insert(60)
    tree.insert(90)

    print("Binary Tree:")
    tree.print_tree()


if __name__ == "__main__":
    main()