import json
from files import Grades

if __name__ == "__main__":


        file = Grades('/home/cleveland/python_training/grades.json')

        file.add_student("Chauncy")

        file.create_new_assignment("Puzzlemania")

        file.enter_new_scores("Alice A", "Puzzlemania", "42")

        file.update_scores("Billy Bob Big Foot", "Burr Bush Assignment", "66")

        file.save('/home/cleveland/python_training/grades.json')
