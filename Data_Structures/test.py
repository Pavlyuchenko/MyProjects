from Data_Struct import LinkedList, Stack
'''
llist = LinkedList()

llist.append("A")
llist.append("B")
llist.print_llist()'''


def find_it(seq):
    arr = []

    for i in seq:
        arr.append(i)

    numbers = {}

    for i in seq:
        if not i in numbers.keys():
            numbers[i] = 0
            for j in seq:
                if j == i:
                    numbers[i] += 1
    for i in numbers.values():
        if i % 2 == 1:
            for j, k in numbers.items():
                if i == k:
                    return j

    

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))