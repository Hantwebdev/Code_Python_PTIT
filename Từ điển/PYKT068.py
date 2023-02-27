class Subject:
    def __init__(self, id, name, exam_forms):
        self.id = id
        self.name = name
        self.exam_forms = exam_forms   
    def __str__(self):
        return f'{self.id} {self.name} {self.exam_forms}'
if __name__ == '__main__':
    students = []
    for case in range(int(input())):
        students += [Subject(input(), input(), input())]
    students.sort(key= lambda ele: ele.id)
    print(*students, sep='\n')