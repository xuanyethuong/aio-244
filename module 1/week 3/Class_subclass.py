class Person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob
    def describe(self):
        return f"Name: {self.name}, Year of Birth: {self.yob}"

class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        return f"Student - {super().describe()}, Grade: {self.grade}"

class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        return f"Teacher - {super().describe()}, Subject: {self.subject}"

class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        return f"Doctor - {super().describe()}, Specialist: {self.specialist}"

class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def describe(self):
        print(f"Ward: {self.name}")
        for person in self.people:
            print(person.describe())

    def count_doctor(self):
        return sum(1 for person in self.people if isinstance(person, Doctor))

    def sort_age(self):
        self.people.sort(key=lambda person: person.yob)

    def compute_average(self):
        teachers = [person for person in self.people if isinstance(person, Teacher)]
        if not teachers:
            return 0
        return sum(teacher.yob for teacher in teachers) / len(teachers)

# Tạo ward object và thêm vào các đối tượng
ward = Ward("Greenfield")

student1 = Student("Alice", 2004, "10th Grade")
teacher1 = Teacher("Mr. Smith", 1980, "Math")
teacher2 = Teacher("Ms. Johnson", 1985, "Science")
doctor1 = Doctor("Dr. Adams", 1975, "Cardiology")
doctor2 = Doctor("Dr. Baker", 1980, "Neurology")

ward.add_person(student1)
ward.add_person(teacher1)
ward.add_person(teacher2)
ward.add_person(doctor1)
ward.add_person(doctor2)

ward.describe()
print(f"Number of doctors in the ward: {ward.count_doctor()}")

ward.sort_age()
ward.describe()

print(f"Average year of birth of teachers in the ward: {ward.compute_average()}")