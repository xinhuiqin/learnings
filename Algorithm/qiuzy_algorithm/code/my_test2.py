def del_space(strs):
    """
    删除字符串中的空格
    :param strs:
    :return:
    """
    res = strs.replace(' ', '')
    print(res)



if __name__ == '__main__':
    example = '145. Binary Tree Postorder Traversal'
    del_space(example)

