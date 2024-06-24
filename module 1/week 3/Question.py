from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass

class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)
        self._grade = grade

    def describe(self):
        print(f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self._grade}")

class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self._subject = subject

    def describe(self):
        print(f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self._subject}")

class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name, yob)
        self._specialist = specialist

    def describe(self):
        print(f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self._specialist}")

class Ward:
    def __init__(self, name: str):
        self._name = name
        self._list_people = list()

    def add_person(self, person: Person):
        self._list_people.append(person)

    def describe(self):
        print(f"Ward Name: {self._name}")
        for p in self._list_people:
            p.describe()

    def count_doctor(self):
        return sum(isinstance(person, Doctor) for person in self._list_people)

# Tạo các đối tượng và thêm vào Ward
student1 = Student(name="studentA", yob=2010, grade="7")
teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")

ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)

# Kiểm tra số lượng bác sĩ và mô tả ward
assert ward1.count_doctor() == 2
ward1.describe()
print(f"Number of doctors: {ward1.count_doctor()}")
class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def is_empty(self):
        return len(self.__stack) == 0

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack is full")
        self.__stack.append(value)

    def top(self):
        if self.is_empty():
            return None
        return self.__stack[-1]

# Tạo đối tượng stack và kiểm tra
stack1 = MyStack(capacity=5)
stack1.push(1)
assert stack1.is_full() == False  # stack chưa đầy
stack1.push(2)
print(stack1.top())  # in giá trị top element hiện tại của stack
class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue is full")
        self.__queue.append(value)

# Tạo đối tượng queue và kiểm tra
queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
assert queue1.is_full() == False  # queue chưa đầy
queue1.enqueue(2)
print(queue1.is_full())  # in trạng thái đầy của queue
class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_empty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.__queue.pop(0)

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue is full")
        self.__queue.append(value)

    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.__queue[0]

# Tạo đối tượng queue và kiểm tra
queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
assert queue1.is_full() == False  # queue chưa đầy
queue1.enqueue(2)
print(queue1.front())  # in giá trị phần tử đầu tiên của queue