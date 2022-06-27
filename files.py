
# create a class that reads a JSON file, options of add student, create a new assignment, update scores, enter new scores, save contents
import json

class Grades(object):
    def __init__(self, json):
        self.grades = self.read(json)
        self.assignments = list(self.grades[list(self.grades.keys())[0]].keys())
        self.json = json
       

    def read(self, file):
        with open(file, "r") as read_file:
            location = json.load(read_file)
        return location


    def add_student(self, name):
        self.grades[str(name)] = {}
        for assignment in self.assignments:
            self.grades[str(name)][assignment] = None
    


    def create_new_assignment(self, assignment_name):
        self.assignments.append(assignment_name)
        for student in self.grades:
            self.grades[student][assignment_name] = None



    def enter_new_scores(self,student, assignment, new_score):
            self.grades[student][assignment] = new_score


    def update_scores(self, student, assignment, updated_score):
            self.grades[student][assignment] = updated_score

    
    def save(self,file_name):
        with open(file_name, "w") as out_file:
            json.dump(self.grades, out_file, indent=2)



if __name__ == "__main__":
    
    file = Grades('/home/cleveland/python_training/grades.json')


    option_dict = {
            'Add student': ['name'],
            'Create new assignment': ['title'],
            'Enter new scores': ['score'],
            'Update scores': ['updated score'],
            'Exit': None
        }
    option_menu = ['Add student', 'Create new assignment', 'Enter new scores', 'Update scores', 'Exit']
    option_string = ''
    for i, options in enumerate(option_menu):
            option_string += f'{i}. {options}\n'


    while True:

        action = input(f'Enter the number of the action you would like.\n{option_string}')

        if action == '0':
            file.add_student(input('Enter new student\'s name: '))

        elif action == '1':
            file.create_new_assignment(input('Enter new assignment name: '))

        elif action == '2':
            for student in file.grades:
                for assignment in file.assignments:
                    if file.grades[student][assignment] == None:
                        while True:

                            try:
                                x = float(input(f'\nEnter new score for {student} on {assignment}: '))
                                break
                            except ValueError:
                                print('Please enter a valid number.')

                        file.enter_new_scores(student, assignment, x )

        elif action == '3':
            file.update_scores(input('\nEnter student name: '), input('\nEnter assignment name: '), input('\nEnter updated score: '))

        elif action == '4':
            file.save('/home/cleveland/python_training/grades.json')
            break