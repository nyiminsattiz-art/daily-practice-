def count(s):
    count_dict = {}
    for i in s:
        if i not in count_dict:
            count_dict[i] = 1
        else:
            count_dict[i] += 1
    return count_dict
