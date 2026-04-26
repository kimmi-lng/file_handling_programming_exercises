class StudentsGwa:
    def __init__(self, names_gwa_file = "student_names_with_gwa.txt"):
        self.names_gwa_file = names_gwa_file
    
    def read_file(self):
        with open(self.names_gwa_file, "r") as file:
            content = [line.rstrip('\n') for line in file.readlines()]
        return content
    
    def find_top_student(self):
        highest_gwa = -1
        top_student = ""

        content = self.read_file()

        for line in content:
            name, gwa = line.strip().split(",")
            gwa = float(gwa)

            if gwa > highest_gwa:
                highest_gwa = gwa
                top_student = name

        return top_student, highest_gwa