class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


# Assumption 1: The parent should also be the same to be unival tree
def countUniValTree(root):
    if root == None:
        return 0, True

    leftUniVal = countUniValTree(root.left)
    rightUniVal = countUniValTree(root.right)

    if root.left != None:
        if root.val == root.left.val and leftUniVal[1] and rightUniVal[1]:
            return 1 + leftUniVal[0] + rightUniVal[0], True
        return leftUniVal[0] + rightUniVal[0], False
    elif root.right != None:
        if root.val == root.right.val and leftUniVal[1] and rightUniVal[1]:
            return 1 + leftUniVal[0] + rightUniVal[0], True
        return leftUniVal[0] + rightUniVal[0], False
    else:
        return 1, True


# Testing
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

root = Node(0)
root.left = Node(1)
root.right = Node(0)
root.right.left = Node(1)
root.right.right = Node(0)
root.right.left.left = Node(1)
root.right.left.right = Node(1)

print(countUniValTree(root)[0])  # 5
