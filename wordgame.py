### Setup Section ###

# We'll learn about how this line of code works later in the course - for now just know it loads the colored text
from colorama import Fore, Back, Style

# Function that prints out a letter with a colorful background
def printColorfulLetter(letter, isLetterInWord, isLetterInCorrectPlace = False):

  # If it's not in the word, display it with a red background
  if(not isLetterInWord):
    print(Back.RED + Fore.WHITE + f" {letter} ", end="")

  # If it's in the word...
  else:

    # ...and it's also in the right place, display it with a green background
    if(isLetterInCorrectPlace):
      print(Back.LIGHTGREEN_EX + Fore.WHITE + f" {letter} ", end="")  

    # ...but in the wrong place, display it with a yellow background
    else:
      print(Back.LIGHTYELLOW_EX + Fore.BLACK + f" {letter} ", end="")


def printGuessAccuracy(guess, actual):
  secret=actual
  # Loop through each index/position 
  for index in range(6):

    # Grab the letter from the guess
    letter = guess[index]

    # Check if the letter at this index of the user's guess is in the secret word AT ALL or not
    if (letter in secret):

      # If the letter is in the secret word, is it also AT THE CURRENT INDEX in the secret word?
      if(letter == secret[index]):

        # Then print it out with a green background
        printColorfulLetter(letter, True, True)

      # If it's not at the current index, we know by this point in the code that it's still used in the secret word somewhere...
      else:
        printColorfulLetter(letter, True, False)

        # ...so we'll print it out with a yellow background

    # ...but if the letter is not in the word at all...
    else:
      printColorfulLetter(letter, False, False)
      # ...print it out with a red background
      
    # Don't worry about the line of code below, it works. It just handles the transition between colors
    print(Style.RESET_ALL + " ", end="")

### Main Program ###
secretWord=("pigeon")
win=False
trys=0

def getSixLetterInput():
  guess = ""
  while(len(guess)!=6):
    guess = input("Enter a six letter guess: ")
  return guess
# TO-DO: Write the logic of the game here!

guess=getSixLetterInput()
if guess==secretWord:
  print("You Win!")
else:
  while (not win) and (trys<5):
    trys+=1
    printGuessAccuracy(guess, secretWord)
    if guess==secretWord:
      print("\nYou Win!")
      win=True
    elif (trys <5):
      print()
      guess=getSixLetterInput()
    else:
      print("\nYou lose.")
  
  
  