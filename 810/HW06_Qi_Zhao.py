"""
this is a program intend to let usr to sort list

@author: Qi Zhao
"""

def insertion_sort(l):
    """ scan each item in a list and findout if the current position number is less than target """
    sorted_list = []
    for item_compare in l:
        for offset, sorted_number in enumerate(sorted_list.copy()):
            if item_compare <= sorted_number:
                sorted_list.insert(offset, item_compare)
                break
        else:
            sorted_list.append(item_compare)
    return sorted_list

def list_copy(l):
    # this is the function using list comprehension
    return [item for item in l]

def list_intersect(l1, l2):
    # this is a function return two list common item into a list
    return [item for item in l1 if item in l2]

def list_difference(l1, l2):
    # this is a function return two list difference item into a lisst
    return [item for item in l1 if item not in l2]

def remove_vowels(string):
    # this is a function return the string without the vowels
    return "".join([item for item in string if item.lower() not in ['a', 'e', 'i', 'o', 'u']])

def check_pwd(password):
    # pwd checker
    return len([item for item in password if item.isupper()]) > 0 and len([item for item in password if item.islower()]) > 0 and len([item for item in password if item.isdigit()]) > 0