print(r"""

   ___     _   _             _____       _____                __  __  U _____ u  _    
  / " \ U |"|u| |   ___     |"_  /u     |_ " _|     ___     U|' \/ '|u\| ___"|/U|"|u  
 | |"| | \| |\| |  |_"_|    U / //        | |      |_"_|    \| |\/| |/ |  _|"  \| |/  
/| |_| |\ | |_| |   | |     \/ /_        /| |\      | |      | |  | |  | |___   |_|   
U \__\_\u<<\___/  U/| |\u   /____|      u |_|U    U/| |\u    |_|  |_|  |_____|  (_)   
   \\// (__) )(.-,_|___|_,-._//<<,-     _// \\_.-,_|___|_,-.<<,-,,-.   <<   >>  |||_  
  (_(__)    (__)\_)-' '-(_/(__) (_/    (__) (__)\_)-' '-(_/  (./  \.) (__) (__)(__)_) 

""")
# Display the title and rules of your game to the user when the program begins

print("You wish to cross into the universe of voldor. You must answer 3 true (T) or false (F) questions.")

questions = ("The airspeed of a European Swallow is 10. ", "Bob's favorite color is blue no red. ", "A witch will float in water. ")
answers = ("T","F","F")
wrong=0
result =("You may cross","You may not cross")
for i in range(3):
  answer=input(questions[i])
  while(answer !=answers[i]):
    wrong+=1
    answer=input(questions[i])
if (wrong==0):
  print(f"You got them all correct. {result[0]}")
else:
  print(f"You got {wrong} out of {len(answers)} correct.  {result[1]}")

  
  

#To improve your portfolio, take it a step further and try to use visually appealing techniques #like ASCII Art to have your quiz show stand out!
#Store at least 3 questions in a tuple, and their corresponding answers in a separate tuple.
#Use a loop to display each question to the user from the questions tuple
#For each question, the user must enter T for True, or F for False. ** Use a loop** to enforce input validation, and re-prompt the user if they enter any other values.
#Keep track of how many questions the user has gotten right
#Finally, display the number of questions they got right out of the total number of questions