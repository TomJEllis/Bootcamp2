
class Students:
   def __init__(self, name, completed_courses, program):
      self.name = name
      self.completed_courses = completed_courses
      self.program = program

   def get_name(self):
      return self.name
   
   def get_completed_courses(self):
      return self.completed_courses

   def get_program(self):
      return self.program
   
   def set_name(self, name):
      self.name = name
   
   def set_completed_courses(self, completed_courses):
      self.completed_courses = completed_courses

   def set_program(self, program):
      self.program = program

class Program:
   def __init__(self, name, num_courses):
      self.name = name
      self.num_courses = num_courses

   def get_name(self):
      return self.name
   
   def get_num_courses(self):
      return self.num_courses
   
   def set_name(self, name):
      self.name = name

   def set_num_courses(self, num_courses):
      self.num_courses = num_courses

def has_student_finished(students, programs):
   student_name = input("Enter a student name: ")
   for student in students:
      if student.get_name() == student_name:
         for program  in programs:
            if student.get_program() == program.get_name():
               if student.get_completed_courses() >= program.get_num_courses():
                  print(f"{student.get_name()} has completed the program: {program.get_name()}")
               elif (program.get_num_courses() - student.get_completed_courses()) <= 4:
                  print(f"{student.get_name()} will complete the program: {program.get_name()} this semester")
               else:
                  print(f"{student.get_name()} requires futher semesters to complete the program: {program.get_name()}")


if __name__ == "__main__":
   students = []
   students.append(Students("Tom",22,"Computer Science"))
   students.append(Students("Tim",24,"Computer Science"))
   students.append(Students("Tam",12,"Software Engineering"))

   programs = []
   programs.append(Program("Computer Science", 24))
   programs.append(Program("Software Engineering", 32))

   has_student_finished(students, programs)
  