#[9, 7, 7, 5, 5, 4] --> [9, 7, 5]

def remove_oddnum(first_list):
    # new_list = set(first_list)
    # new_list_1 = []
    # for i in new_list:
    #     if i%2 !=0:
    #         new_list_1.append(i)
    # return new_list_1
    #---------------------- other method

    # new_list = []
    # for i in first_list:
    #     if i%2 !=0:
    #         new_list.append(i)
    # new_list = list(set(new_list))
    # return new_list
    '''Other method'''
    new_list = []
    for i in first_list:
        if i not in new_list and:
            


a = remove_oddnum([9, 7, 7, 5, 5, 4])
print(a)