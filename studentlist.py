################ Function Definitions ################

# Shows the user what options they have
def displayMenu():

  # This option will involve you adding a student and a collection for their grades to a dictionary!
  print("1. Add a Student")

  # This option will involve you removing a pair from a dictionary!
  print("2. Remove a Student")

  # This option will require you to grab a student from a dictionary and add a quiz grade to it's corresponding collection of grades!
  # You'll also need to use a pre-written function that ensures the user is entering a valid grade (a decimal number)
  print("3. Add Quiz Grade for Student")

  # This option will require you to use a loop to list all of the grades for an INDIVIDUAL student!
  print("4. List a Student's Quiz Grades")

  # This option will have you write a function that takes in a student's grade as a number and return the letter grade equivalent!
  print("5. Get Student's Letter Grade")

  print("6. Quit")

# Prompts the user to enter a numeric grade
# This function works, and ensures the user entered a valid float for the grade
# It's not important HOW this function works, but how to USE this function
def getNumberGradeFromUser():

  val = None

  while(val == None):
    try:
      test = float(input("Enter a Grade: "))
      val = test
    except:
      val = None
  
  return val

def getOption():
  
  val = None

  while(val == None):
    try:
      test = int(input("Select an option number: "))
      val = test
    except:
      val = None
  
  return val



################ Main Program ################

students={}
option=7
# Application Loop
while(int(option)!=6):

  # Prompt the user to select an option
  print()
  displayMenu()
  option=getOption()
  if option==1:
    name=input("Enter a student name: ")
    students[name]=[]
    print(f"{name} added!")
  elif option==2:
    key=input("Enter a student name: ")
    if key in students:
      students.pop(key)
      print(f"{key} removed!")
    else:
      print(f"{key} not in dictionary!!")
  elif option==3:
    key=input("Enter a student name: ")
    if key in students:
      grade=getNumberGradeFromUser() 
      students[key].append(grade) #need to add abilitiy for more grades
      print(f"Added {grade} to {name}'s quizzes")
    else:
      print(f"{key} not in dictionary!!")
  elif option==4:
    key=input("Enter a student name: ")
    if key in students:
      print(f"{key}'s quizzes")
      quizzes = students[key]
      for quiz in quizzes:
        print(f"{quiz}\n")
    else:
      print(f"{key} not in dictionary!!")
  elif option==5:
    key=input("Enter a student name: ")
    if key in students:
      quiz_ave=sum(students[key])/len(students[key])
      if quiz_ave >= 90:
        letter='A'
      elif quiz_ave >= 80:
        letter='A'
      elif quiz_ave >= 70:
        letter='C'
      elif quiz_ave >= 60:
        letter='D'
      elif quiz_ave >= 50:
        letter='E'
      else:
        letter='F'
      print(f"{key}'s current grade is a {letter}")
    else:
      print(f"{key} not in dictionary!!")
  else:
    print("Done")
  

  



