class ReverseIterator:

    def __init__(self, lst):
        self.index = len(lst)
        self.lst = lst
        pass

    def __next__(self):
        if self.index == 0:  # stop to iterate
            raise StopIteration
        if self.index > 0:  # reason to continue
            self.index -= 1
        print(self.lst[self.index])
        return self


it = ReverseIterator([1, 2, 3, 4, 5])
next(it)
next(it)
next(it)
next(it)
next(it)
next(it)
