class SortIntegers:
    def __init__(self, integers = "integers.txt", double = "double.txt", triple = "triple.txt"):
        self.integers = integers
        self.double = double
        self.triple = triple
    
    def read_integers(self):
        with open(self.integers, "r") as file:
            content = [line.rstrip('\n') for line in file.readlines()]
        return content
    