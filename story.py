answer=input(
  "Your name is Bob, your favorit color is red, and meet with the old goat at the bridge of death. To cross \n he will ask you three questions to  which you must answer correctly or you will catupult into an abyss.\n At the bridge the old goat asks:\n What is your name?: \n")

if(answer=='Bob'):
  color=input("What is your favorite color? ")
  if(color=='red'):
    number=float(input("What is 7 + 6 - 3 + 3/2 ?  "))
    if(number==(7 + 6 - 3 + 3/2)):
      print("You can go on now")
    else:
      print("'Oooh, so sorry' you hear him say as you fly over the edge into the abyss")
  else:
    print("'Oooh, so sorry' you hear him say as you fly over the edge into the abyss")
else:
  print("'Oooh, so sorry' you hear him say as you fly over the edge into the abyss")
#ending


                      
             
