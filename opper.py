
class Student:

 def __init__(self,name,age):
     print("I am  alive")
     self.name = name
     self.age  = age

 def about_me(self):
        print(f"name:{self.name}")

nazar = Student("Nazar",16)
nazar.about_me()


class Course:

    def __init__(self,name,instructor,duration):
       self.name = name
       self.instructor = instructor
       self.duration = duration

    def course_info(self):
        print(f"name:{self.name},instructora:{self.instructor},duration:{self.duration}")

    def is_long_course(self):
        if self.duration > 40:
            return "true"
        else:
            return "false"


course1 = Course("Python для початківців", "Олексій Іванов", 45)
course2 = Course("Математика для аналітиків", "Наталія Петрова", 35)
course3 = Course("Англійська для IT", "Марія Сидоренко", 50)


courses = [course1, course2, course3]
for course in courses:
    print(course.course_info())
    print(f"Довготривалий: {course.is_long_course()}")
    print("-" * 40)














