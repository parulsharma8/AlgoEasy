from typing import Any
class Node:
    v: int
    left: Any
    right: Any

    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)


def DFS(root):
    if root:
        print(root.v)
        DFS(root.left)
        DFS(root.right)

DFS(root)