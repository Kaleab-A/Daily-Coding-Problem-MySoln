class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Idea: To recursively go down the tree. And compare value of nodes with a target value.
# If a node is a leaf node, by default it is a unival tree.
# A tree is unival tree, it is left sub-tree (if any) and right sub-tree (if any) are both unival
#   and the value of node == value of leftChild == value of rightChild


# Returns 2 value, index 0: the number of unival under the tree. index 1: boolean if the root is
#        unival itself
def countUnival(root):
    if root.left == None and root.right == None:
        return [1, True]

    isLeftUniVal = True
    isRightUniVal = True
    allSameVal = (
        True  # Boolean representing is the left and right and root have same val
    )

    leftCount = 0
    rightCount = 0

    if root.left != None:
        leftCount, isLeftUniVal = countUnival(root.left)
        allSameVal = allSameVal and (root.val == root.left.val)

    if root.right != None:
        rightCount, isRightUniVal = countUnival(root.right)
        allSameVal = allSameVal and (root.val == root.right.val)

    if isLeftUniVal and isRightUniVal and allSameVal:
        return [leftCount + rightCount + 1, True]
    return [leftCount + rightCount, False]


#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1
# Constucting example tree
temp1 = Node(1)
temp2 = Node(1, temp1, temp1)
temp1 = Node(0)
temp2 = Node(0, temp2, temp1)
temp1 = Node(1)
root = Node(0, temp1, temp2)

print(countUnival(root)[0])
