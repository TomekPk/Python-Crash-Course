def show_magicians(name):
    for i in name:
        print(i)


def make_great(name,second_list):
    '''
    Function remove items from name list, print removed item and append to new_list.
    Pass new_list name to second_list positional argument and create new_list = [] manually
    :param name:
    :param second_list: pass name of created empty list, of instance new_list = []
    :return:
    '''
    while name:
        remove_item = name.pop()
        print("Adding to new list: " + remove_item)
        remove_item = "Great " + remove_item
        second_list.append(remove_item)

new_list = []