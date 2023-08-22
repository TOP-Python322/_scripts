class Test:
    pass

try:
    for elem in Test():
        print(elem)
except TypeError as exc:
    print(exc)



class TestIter:
    def __iter__(self):
        return 'abc'.__iter__()

try:
    for elem in TestIter():
        print(elem)
except TypeError as exc:
    print(exc)



class TestAutoIter:
    def __iter__(self):
        yield self

try:
    for elem in TestAutoIter():
        print(elem)
except TypeError as exc:
    print(exc)



class TestNext:
    def __next__(self):
        return 1
    
try:
    for elem in TestNext():
        print(elem)
except TypeError as exc:
    print(exc)


