import sys
from random import random
import pyBST

def cmp(a, b):
    return a - b

def random_list(N):
    return [int(random() * 10) for i in range(N)]

def test_instantiation(N):
    ls = []
    for i in range(N):
        ls.append(int(random() * 100))
    print(ls)

    bst = pyBST.pyBST(cmp)
    for i in ls:
        bst.insert(i)
    print([node.data for node in bst.in_order()])
    print([node.data for node in bst.pre_order()])
    print([node.data for node in bst.post_order()])

def make_bst(ls):
    bst = pyBST.pyBST(cmp)
    for i in ls:
        bst.insert(i)
    return bst

def sample_tests(num_tests = 5, mode = 0):
    """Provides a dictionary with test keys and matching BSTs."""
    sample = []
    tall_tree_test1 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    tall_tree_test2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    tall_tree_test3 = [20, 1, 19, 2, 18, 3, 17, 4, 16, 5, 15, 6, 14, 7, 13, 8, 12, 9, 11, 10]
    
    if mode == 0:
        sample.append(make_bst(tall_tree_test1))
        sample.append(make_bst(tall_tree_test2))
        sample.append(make_bst(tall_tree_test3))
        for i in range(num_tests - 3):
            sample.append(make_bst(random_list(100)))
    else:
        sample.append((tall_tree_test1, make_bst(tall_tree_test1)))
        sample.append((tall_tree_test2, make_bst(tall_tree_test2)))
        sample.append((tall_tree_test3, make_bst(tall_tree_test3)))
        for i in range(num_tests - 3):
            rand_test = random_list(100)
            sample.append((rand_test, make_bst(rand_test)))
    return sample


def test_height():
    test1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    test2 = [5, 3, 1, 2, 0, 4, 7, 8, 6, 9]
    
    bst1 = make_bst(test1)
    bst2 = make_bst(test2)

    if bst1.height() == 10:
        print('Passed test_height: test1')
    else:
        print('Failed test_height: test1')

    if bst2.height() == 4:
        print('Passed test_height: test2')
    else:
        print('Failed test_height: test2')

def test_size():
    ls = []
    count = 0
    for i in range(100):
        rand = int(random() * 100)
        if rand not in ls:
            count += 1
        ls.append(rand)
    bst = make_bst(ls)
    if bst.size() == count:
        print('Passed test_size')
    else:
        print('Failed test_size')
        print('Size: ' + str(bst.size()))
        print('Count: ' + str(count))

def test_find():
    test1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    test2 = [5, 3, 1, 2, 0, 4, 7, 8, 6, 9]

    bst1 = make_bst(test1)
    bst2 = make_bst(test2)

    for i in test1:
        if not bst1.find(i):
            print('Failed test_find: bst1 contains ' + str(i))
            return
    for i in test2:
        if not bst2.find(i):
            print('Failed test_find: bst2 contains ' + str(i))
            return

    test3 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    for i in test3:
        if bst1.find(i):
            print('Failed test_find: bst1 does not contain ' + str(i))
            return
    for i in test3:
        if bst2.find(i):
            print('Failed test_find: bst2 does not contain ' + str(i))
            return

    print('Passed test_find')

def test_min():
    test1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    test2 = [5, 3, 1, 2, 0, 4, 7, 8, 6, 9]
    test3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    test4 = [5, 3, 1, 2, 10, 4, 7, 8, 6, 9]

    bst1 = make_bst(test1)
    bst2 = make_bst(test2)
    bst3 = make_bst(test3)
    bst4 = make_bst(test4)

    if bst1.min() != 0:
        print('Failed test_min: test1')
        return
    if bst2.min() != 0:
        print('Failed test_min: test2')
        return
    if bst3.min() != 1:
        print('Failed test_min: test3')
        return
    if bst4.min() != 1:
        print('Failed test_min: test4')
        return
    print ('Passed test_min.')

def test_delete_min():
    tests = sample_tests()
    for test_bst in tests:
        min_val = test_bst.min()
        test_bst.delete_min()
        if test_bst.min() == min_val:
            print("Failed test_delete_min: min returns the same")
            print('Min: ' + str(test_bst.min()))
            print('Min_val: ' + str(min_val))
            return
        if test_bst.find(min_val):
            print("Failed test_delete_min: find returns the same")
            return
    print('Passed test_delete_min')

def test_remove():
    tests = sample_tests(5, 1)
    for test_bst in tests:
        i = 0
        while not test_bst[1].is_empty():
            test_bst[1].remove(i)
            i += 1
    print('Passed test_remove.')

def main(argv):
    test_instantiation(int(argv[0]))
    test_height()
    test_size()
    test_find()
    test_min()
    test_delete_min()
    test_remove()
    
if __name__ == '__main__':
    main(sys.argv[1:])