def get_even_list (l):
    result_list = []
    for i in range (len(l)):
        if l[i] % 2 == 0:
            result_list.append(l[i])
    return result_list

# a = [1,2,3,4,5,6,7,8,9]
# a = get_even_list(a)
# print(a)