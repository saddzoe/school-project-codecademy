# school-project-codecademy
# This is class project from codecademy

class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
    self.attendance = {}

  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)
  
  def get_average():
    return self.grades / len(self.grades)
    

class Grade:
  minimum_passing = 65
  def __init__(self, score):
    self.score = score

  def is_passing(self, score):
    if self.score > minimum_passing:
      return "You are passing."
    else:
      return "Your are failing."




roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

pieter.add_grade(Grade(100))
