def del_space(strs):
    """
    删除字符串中的空格
    :param strs:
    :return:
    """
    res = strs.replace(' ', '')
    print(res)



if __name__ == '__main__':
    example = '234. Palindrome Linked List'
    del_space(example)

