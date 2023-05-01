# Prints a line of equal signs
print("=========================")
print("Welcome to the UMBC")
print("Car Customization Form!")
print("=========================")
#blank
print()
#ask for the model option
print("(For multiple choice problems, please enter the letter of the slection you are looking for)")
print("~ Make & Model ~")
print("1. What Model of Car are you ordering?")
print("  a. Lightening Speedster")
print("  b. Eco Leaf")
print("  c. Harp Chord")
print("  d. Chevron Jolt")
#model stores the model option
model=input("Pleaes enter 'a' -'d': ")
print()
# 2 door model updgrade?
print("2. Would you like to upgrade from the 4-door option to the 2-door optoin?")
#doors stores door choice
doors=input("Please enter 'yes' or 'no': ")
print()
print("~Exterior~")
#Get color from user any choice
print("3. What color would you like your car to be?")
#color is the name of the color provided by user
color=input("You may enter the name of any color you'd like: ")
print()
#weather package upgrade choice
print("4. Would you like the deluxe weather packages?")
#weather stores weather pkg upgrade choice
weather=input("Please enter 'yes' or 'no': ")
print("~Interior~")
#engin choice
print("5.  Which Engine would you like your car to have?")
print("  a. I-4 Entry Engine")
print("  b. V-6 Performance Engine")
print("  c. Eco Diesel Engine")
#engine stores the letter designation choice
engine=input("Pleaes enter 'a' -'c': ")
print()
# choosing heated seats
print("6. Would you like heated seats?")
#seats stores the choice of heated seats
seats=input("Please enter 'yes' or 'no': ")
print()
#print out the car option choices
print("=========================")
print("~Summary~")
print("Model Option: ",model)
print("Upgrade to 2-Door: ",doors)
print("Desired Color: ",color)
print("Upgrade to Deluxe Weather: ",weather)
print("Engine Option: ",engine)
print("Upgrade to Heated Seats: ",seats)