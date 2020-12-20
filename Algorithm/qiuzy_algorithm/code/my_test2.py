def del_space(strs):
    """
    删除字符串中的空格
    :param strs:
    :return:
    """
    res = strs.replace(' ', '')
    print(res)



if __name__ == '__main__':
    example = '1046. Last Stone Weight'
    del_space(example)

