class ListPrinter:
    def __init__(self,lst):
        self.lst = lst

    def print(self):
        for i,l in enumerate(self.lst):
            print(i,l)

    def printAtIndex(self,ndx):
        try:
            print(self.lst[ndx])
        except IndexError:
            raise IndexError('error in printAtIndex')

lp = ListPrinter([1,2,3])

try:
    lp.print()
    lp.printAtIndex(4)
except IndexError as e:
    print(e)