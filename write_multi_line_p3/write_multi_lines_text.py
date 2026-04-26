class AddTexts:
    def __init__(self, mylife = "mylife.txt"):
        self.mylife = mylife

    def ask_for_texts(self):
        self.texts = []
        while True:
            line = input("Enter line: ")
            self.texts.append(line)
            
            choice = input("Are there more lines y/n? ").lower()
            if choice == 'n':
                break

    def add_texts(self):
        with open(self.mylife, 'a') as file:
            for data in self.texts:
                file.write(data + "\n")   