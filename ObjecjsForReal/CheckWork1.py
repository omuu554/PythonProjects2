from Work1 import Course

Name = input("Please enter a course Name: ")
id = int(input("Please enter a course id: "))
Max = int(input("Please enter a the max amount of students in the course: "))
Signed = int(input("Please enter a course amount of students in the course: "))
StudentsToAdd = int(input("Please enter a course amount of students in the course: "))

NewCourse = Course(id , Name , Max, Signed)

print(NewCourse)
NewCourse.AddStudents(StudentsToAdd)
print(NewCourse)
