class BTNode():
    __slots__ = "value", "left", "right"

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def postorder(tree):
    if tree:
        postorder(tree.left)
        postorder(tree.right)
        print(tree.value)


def createTree(inorder, preorder):
    if len(preorder) == 0:
        return None
    if len(preorder) == 1:
        return BTNode(preorder[0])

    root = preorder[0]
    inorder_left = inorder[:inorder.index(root)]
    inorder_right = inorder[inorder.index(root) + 1:]
    preorder_left = []
    preorder_right = []

    index = 1
    for index in range(1, len(preorder)):
        if preorder[index] in inorder_right:
            break
        preorder_left.append(preorder[index])

    if index != len(preorder) - 1 or preorder[index] in inorder_right:
        for index in range(index, len(preorder)):
            preorder_right.append(preorder[index])

    return BTNode(root, createTree(inorder_left, preorder_left), createTree(inorder_right, preorder_right))


def main():
    inorder = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12]
    preorder = [6, 3, 2, 1, 5, 4, 10, 8, 9, 11, 12]
    tree = createTree(inorder, preorder)
    postorder(tree)


if __name__ == '__main__':
    main()
