class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('name :', self.name)
        print('age :', self.age)


class Student(Person):

    def __init__(self, **kwargs):
        super().__init__(kwargs['name'], kwargs['age'])
        self.year_of_passing = kwargs['year_passing']
        self.student_id = kwargs['id']
        self.year_of_enrolled = kwargs['enroll_year']
        self.course_name = kwargs['course_name']

    def displayStudent(self):
        print('name :', self.name)
        print('age :', self.age)
        print('Student ID :', self.student_id)
        print('Course enrolled :', self.year_of_enrolled)
        print('Course Name : ', self.course_name)
        print('year of passing :', self.year_of_passing)


# obj_person = Person('Raj','21')
dis = {'name': 'Raj', 'age': '21', 'id': '1234', 'year_passing': '2022',
       'enroll_year': '2018', 'course_name': 'cse'}

obj = Student(**dis)
obj.displayStudent()
