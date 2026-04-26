class ExtractNumbers:
    def __init__(self, reads_txt_file = "numbers.txt"):
        self.reads_txt_file = reads_txt_file

    def read_file(self):
        with open(self.reads_txt_file, "r") as file:
            content = [line.rstrip('\n') for line in file.readlines()]
        return content

    def find_even_odd(self):
        content = self.read_file()
        with open("even.txt", "w") as even_numbs_file, open("odd.txt", "w") as odd_numbs_file:
            for line in content:
                    numbers = int(line)
                    if numbers % 2 == 0:
                        even_numbs_file.write(f"{numbers}\n")
                    else:
                        odd_numbs_file.write(f"{numbers}\n")
