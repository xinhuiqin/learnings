def preorder_iterate(root):
    """

    :param root: 待遍历的树的根结点
    :return:
    """
    # 栈使用列表模拟，用于记录暂时未访问的结点
    stack = []
    while root or stack:
        while root:
            # 先序遍历，先访问根结点
            print(root.val)
            # 因为右子结点再左子结点后面访问，所以要先记录
            stack.append(root.right)
            # 沿左分支下行，直到叶子结点
            root = root.left
        # 回溯,处理右子结点
        root = stack.pop()


def inorder_iterate(root):
    """
    中序遍历（迭代）

    :param root: 待遍历的树的根结点
    :return:
    """
    # 栈使用列表模拟，用于记录暂时未访问的结点
    stack = []
    while root or stack:
        while root:
            # 根结点在左子结点后面访问，所以先记录
            stack.append(root)
            # 沿左分支下行，直到叶子结点
            root = root.left
        # 回溯
        root = stack.pop()
        # 处理根结点
        print(root.val)
        # 处理右结点
        root = root.right


def postorder_iterate(root):
    """
    后序遍历（迭代）

    :param root: 待遍历的树的根结点
    :return:
    """

    # 栈使用列表模拟，用于记录暂时未访问的结点
    stack = []
    prev = None
    while root or stack:
        while root:  # 左分支下行，直到叶子结点
            # 因为是后续遍历，所以根结点先记录，入栈
            stack.append(root)
            # 找到下一个应该访问的结点
            root = root.left if root.left else root.right

        # 回溯
        root = stack.pop()
        print(root.val)
        # 当前结点是栈顶的左子结点，则遍历右子结点
        if stack and root[-1].left:
            root = stack[-1].right
        else:
            root = None



