import math

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def newNode(data):
    return Node(data)

def constructPerfectBT(depth, value):
    if depth == 0:
        return None

    root = newNode(value[0])
    value[0] -= 1
    root.right = constructPerfectBT(depth - 1, value)
    root.left = constructPerfectBT(depth - 1, value)

    return root


def findParent(root, target, parent=None):
    if root is None:
        return None

    if root.data == target:
        return parent

    leftResult = findParent(root.left, target, root)
    if leftResult is not None:
        return leftResult

    rightResult = findParent(root.right, target, root)
    if rightResult is not None:
        return rightResult

    return None  # Return None instead of -1

def solution(h, q):
    depth = h
    value = [pow(2, depth) - 1]
    root = constructPerfectBT(depth, value)

    p = []
    for node in q:
        targetNodeValue = node
        parentNode = findParent(root, targetNodeValue)
        p.append(parentNode.data if parentNode is not None else -1)
    return p
