# Using multiple variables in a For loop in Python

list1 = ['bobby', 'hadz', 'com']
list2 = [1, 2, 3]
list3 = ['a', 'b', 'c']

for item1, item2, item3 in zip(list1, list2, list3):
    # bobby 1 a
    # hadz 2 b
    # com 3 c
    print(item1, item2, item3)