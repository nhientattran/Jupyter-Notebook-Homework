def sum_pairs(ints, s):
    dic = {}
    for num in ints:
        if num not in dic:
            dic[s - num] = num
        else:
            return [(s - num), num]
    return None


