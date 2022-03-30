def main(list_num):
    """
    g
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    if list_num[0] > list_num[-1]:
        return list_num[0]
    return list_num[-1]