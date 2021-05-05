class Group:
    number_of_group = 0

    def __init__(self, name, *students):
        self.students = list(students)
        self.name = name
        print(f'{self.students} study in gruop {self.name}')

        Group.number_of_group += 1

    def add_student(self, student):
        self.students.append(student)

    def info_group(self):
        print(f'Group: {self.name}\nStudents: {self.students}')

    def group_num():
        print(f'Number of groups: {Group.number_of_group}')

    group_num = staticmethod(group_num)

    def __del__(self):
        print(f'Group {self.name} delet')

        Group.number_of_group -= 1

programming_group = Group('PTN2-W21', 'Nikita', 'Oleg', 'Igor')
programming_group.info_group()
programming_group.add_student('Artem')
programming_group.info_group()
Group.group_num()
del programming_group
Group.group_num()
