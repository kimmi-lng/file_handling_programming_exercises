class SortIntegers:
    def __init__(self, 
             integers = "squared_cubed_integers_p4/integers.txt", 
             double = "squared_cubed_integers_p4/double.txt", 
             triple = "squared_cubed_integers_p4/triple.txt"):
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
                if line.strip():
                    numbers = int(line)
                    if numbers % 2 == 0:
                        double_file.write(f"{numbers ** 2}\n")
                    else:
                        triple_file.write(f"{numbers ** 3}\n")
    