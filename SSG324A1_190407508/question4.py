def remove_elements(list):
    new_list = []
    for i in range(len(list)):
        if i not in [0, 4, 5]:
            new_list.append(list[i])
    return new_list
    # return [list[i] for i in range(len(list)) if i not in [0, 4, 5]]



list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(remove_elements(list))