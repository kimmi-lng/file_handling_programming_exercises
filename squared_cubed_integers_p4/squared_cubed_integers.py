class SortIntegers:
    def __init__(self, integers = "integers.txt", double = "double.txt", triple = "triple.txt"):
        self.integers = integers
        self.double = double
        self.triple = triple
    
    def read_integers(self):
        with open(self.integers, "r") as file:
            content = [line.rstrip('\n') for line in file.readlines()]
        return content
    
    def sort_integers(self):
        content = self.read_integers()
        with open(self.double, "w") as double_file, open(self.triple, "w") as triple_file:
            for line in content:
                numbers = int(line)
                if numbers % 2 == 0:
                    double_file.write(f"{numbers ** 2}\n")
                else:
                    triple_file.write(f"{numbers ** 3}\n")
    