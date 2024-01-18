import random

def power(base, exp):
    ret_val = 1
    for _ in range(exp):
        ret_val *= base
    return ret_val


#time complexity O(n)

def multiply(n1, n2):
    ret_val = 0
    for _ in range(n2):
        ret_val += n1
    return ret_val

#time complexity O(n)
'''
def insert (lis, value, index):
    i = len(lis) - 1
    while i > index:
        lis[i] = lis[i-1]
    lis[index] = value
'''

def random_num_insert(lis, value, index):
    i = len(lis) - 1
    while i > index:
        lis[i] = lis[i-1]
        i -= 1
    lis[index] = value

list1 = [4,7,9,12]
print(list1)
random_num_insert(list1, random.randint(1,6), 2)
print(list1)
 