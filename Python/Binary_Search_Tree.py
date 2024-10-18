class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root: Node, value: int) -> Node:
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def search(root: Node, value: int) -> bool:
    if root is None:
        return False
    if root.value == value:
        return True
    return search(root.left, value) if value < root.value else search(root.right, value)

def find_min(root: Node) -> Node:
    while root.left is not None:
        root = root.left
    return root

def delete(root: Node, value: int) -> Node:
    if root is None:
        return root
    if value < root.value:
        root.left = delete(root.left, value)
    elif value > root.value:
        root.right = delete(root.right, value)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        min_node = find_min(root.right)
        root.value = min_node.value
        root.right = delete(root.right, min_node.value)
    return root

def in_order(root: Node, result: list = None) -> list:
    if result is None:
        result = []
    if root is not None:
        in_order(root.left, result)
        result.append(root.value)
        in_order(root.right, result)
    return result

# Example usage
root = None
root = insert(root, 20)
root = insert(root, 10)
root = insert(root, 30)
root = insert(root, 25)

print("Searching for 25:", search(root, 25))  # Output: True

root = delete(root, 10)

print("In-order traversal after deletion:", in_order(root))  # Output: [20, 25, 30]
