# {"name":"john","age":30,"city":"New York","marks":90}
# {"name":"rita","age":25,"city":"Los Angeles","marks":85}
# {"name":"mike","age":28,"city":"Chicago","marks":92}
# {"name":"sara","age":22,"city":"Houston","marks":88}

class Student:
    def __init__(self, name, age, city, marks):
        self.name = name
        self.age = age
        self.city = city
        self.marks = marks

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")
        print(f"Marks: {self.marks}")

    def greetings(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old. from {self.city}. I scored {self.marks} marks.")    

student1=Student("john", 30, "New York", 90)
student2=Student("rita", 25, "Los Angeles", 85)


# student1.display_info()
greet_message = student1.greetings()
print(greet_message)
# print(student1.name)

students_list = []
students_list.append(student1)
students_list.append(student2)

for i in students_list:
   print(i.greetings())