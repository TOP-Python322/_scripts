test_list1 = [1, 2, 3]
test_list2 = test_list1

test_list1[0] = 100
print(test_list1, test_list2, sep='\n')
print(id(test_list1), id(test_list2), sep='\n')
print(f'{test_list1 is test_list2 = }\n')
print(f'test_list1 is test_list2 = {test_list1 is test_list2}\n')

test_list1.append(4)
print(test_list1, id(test_list1), sep='\n')

test_list1 = test_list1 + [5]
print(test_list1, id(test_list1), sep='\n')


test_tuple1 = (1, '2', 3.4)
test_tuple2 = (5, )

print(type(test_tuple1))
print(id(test_tuple1))

# приведёт к TypeError
# test_tuple1[0] = 100

# приведёт к AttributeError
# test_tuple1.append(4)

test_tuple1 = test_tuple1 + test_tuple2
print(id(test_tuple1))
