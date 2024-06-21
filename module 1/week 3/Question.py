# Câu 1:
from abc import ABC, abstractmethod
import torch
import torch.nn as nn
data = torch.Tensor([1, 2, 3])
softmax_function = nn.Softmax(dim=0)
output = softmax_function(data)
assert round(output[0].item(), 2) == 0.09
# Câu 2:


class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        sum_exp_x = torch.sum(exp_x)
        return exp_x / sum_exp_x


data = torch.Tensor([5, 2, 4])
my_softmax = MySoftmax()
output = my_softmax(data)
assert round(output[-1].item(), 2) == 0.26
print("Câu 2:", output)
# Câu 3:


class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        max_x = torch.max(x)
        exp_x = torch.exp(x - max_x)
        sum_exp_x = torch.sum(exp_x)
        return exp_x / sum_exp_x


data = torch.Tensor([1, 2, 300000000])
my_softmax = MySoftmax()
output = my_softmax(data)
assert round(output[0].item(), 2) == 0.0
print("Câu 3:", output)
# Câu 4:


class SoftmaxStable(nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, x):
        x_max = torch.max(x)  # Tìm giá trị lớn nhất trong tensor x
        # Trừ đi giá trị lớn nhất trước khi tính exponential
        x_exp = torch.exp(x - x_max)
        partition = torch.sum(x_exp)  # Tổng của các giá trị exponential
        return x_exp / partition  # Chia từng giá trị exponential cho tổng để tính softmax


data = torch.Tensor([1, 2, 3])
softmax_stable = SoftmaxStable()
output = softmax_stable(data)
assert round(output[-1].item(), 2) == 0.67
print("Câu 4:", output)
# Câu 5:


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
        super().__init__(name, yob)  # Khởi tạo các thuộc tính từ class cha (Person)
        self._grade = grade  # Khởi tạo thêm thuộc tính grade cho class Student

    def describe(self):
        # In ra thông tin của Student
        print(
            f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self._grade}")


# Tạo object Student và kiểm tra assert
student1 = Student(name="studentZ2023", yob=2011, grade="6")
assert student1._yob == 2011
student1.describe()
# Câu 6:


class Person(ABC):
    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass


class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)  # Khởi tạo các thuộc tính từ class cha (Person)
        self._subject = subject  # Khởi tạo thêm thuộc tính subject cho class Teacher

    def describe(self):
        # In ra thông tin của Teacher
        print(
            f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self._subject}")


# Tạo object Teacher và kiểm tra assert
teacher1 = Teacher(name="teacherZ2023", yob=1991, subject="History")
assert teacher1._yob == 1991
teacher1.describe()
# Câu 7:


class Person(ABC):
    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass


class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name, yob)  # Khởi tạo các thuộc tính từ class cha (Person)
        self._specialist = specialist  # Khởi tạo thêm thuộc tính specialist cho class Doctor

    def describe(self):
        # In ra thông tin của Doctor
        print(
            f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self._specialist}")


# Tạo object Doctor và kiểm tra assert
doctor1 = Doctor(name="doctorZ2023", yob=1981, specialist="Endocrinologists")
assert doctor1._yob == 1981
doctor1.describe()
# Câu 8:


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
        print(
            f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self._grade}")


class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self._subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self._subject}")


class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name, yob)
        self._specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self._specialist}")


class Ward:
    def __init__(self, name: str):
        self.__name = name
        self.__listPeople = list()

    def add_person(self, person: Person):
        self.__listPeople.append(person)

    def describe(self):
        print(f"Ward Name: {self.__name}")
        for p in self.__listPeople:
            p.describe()

    def count_doctor(self):
        count = 0
        for p in self.__listPeople:
            if isinstance(p, Doctor):
                count += 1
        return count


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
# Câu 9:


class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def push(self, value):
        if not self.is_full():
            self.__stack.append(value)
        else:
            raise OverflowError("Stack is full")


# Tạo đối tượng stack và kiểm tra
stack1 = MyStack(capacity=5)
stack1.push(1)
assert stack1.is_full() == False  # stack chưa đầy
stack1.push(2)
print(stack1.is_full())  # in kết quả kiểm tra stack đã đầy hay chưa
# Câu 10:


class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def is_empty(self):
        return len(self.__stack) == 0

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def push(self, value):
        if not self.is_full():
            self.__stack.append(value)
        else:
            raise OverflowError("Stack is full")

    def top(self):
        if not self.is_empty():
            return self.__stack[-1]
        else:
            return None


# Tạo đối tượng stack và kiểm tra
stack1 = MyStack(capacity=5)
stack1.push(1)
assert stack1.is_full() == False  # stack chưa đầy
stack1.push(2)
print(stack1.top())  # in giá trị top element hiện tại của stack
# Câu 11:


class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def enqueue(self, value):
        if not self.is_full():
            self.__queue.append(value)
        else:
            raise OverflowError("Queue is full")


# Tạo đối tượng queue và kiểm tra
queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
assert queue1.is_full() == False  # queue chưa đầy
queue1.enqueue(2)
print(queue1.is_full())  # in trạng thái đầy của queue
# Câu 12:


class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def isEmpty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def dequeue(self):
        if not self.isEmpty():
            return self.__queue.pop(0)
        else:
            raise IndexError("Queue is empty")

    def enqueue(self, value):
        if not self.is_full():
            self.__queue.append(value)
        else:
            raise OverflowError("Queue is full")

    def front(self):
        if not self.isEmpty():
            return self.__queue[0]
        else:
            raise IndexError("Queue is empty")


# Tạo đối tượng queue và kiểm tra
queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
assert queue1.is_full() == False  # queue chưa đầy
queue1.enqueue(2)
print(queue1.front())  # in giá trị phần tử đầu tiên của queue
