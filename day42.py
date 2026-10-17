def matrix_addition(a, b):
    final_list = []
    for i in range(len(a)):
        new_list = []
        listA = a[i]
        listB = b[i]
        for j in range(len(listA)):
            addition = listA[j] + listB[j]
            new_list.append(addition)
        final_list.append(new_list)
    return final_list
