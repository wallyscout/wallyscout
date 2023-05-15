 #This function returns the entirety of "Dracula" as a string
def readBook():
  f = open("dracula.txt", "r")
  s = f.read().replace("-", " ")
  f.close()
  return ''.join(c for c in s if c.isalnum() or c == " ")

draculatext=readBook()
#draculatext=("the the the boys girls are ready to go the cows are ready too and they semell really bad let's go boys")
draculatext=draculatext.lower()
draculatext=draculatext.split()


word_count={}

num_four_letter=0

for word in draculatext:
  if word in word_count:
    #value=value+1
    word_count[word]+=1#=value
  else:
    word_count[word]=1

  if len(word)==4:
    num_four_letter+=1

largest = 0
most_frequent=''
# Find the largest value in the Tuple
for key in word_count:
  if(word_count[key] > largest):
    largest = word_count[key]
    most_frequent=word

frequent_words={}
for key in word_count:
  if word_count[key]>499:
    frequent_words[key]= word_count[key]

# Display the largest number found
print(f"'{most_frequent}' is the word that appears the most throughout the text, a total of {largest} times ")
print(f"There are {num_four_letter} words that are four letters long")
print("I noticed that these words show up 500 or more times:")
for key in frequent_words:
  print(f"{key} - {frequent_words[key]}")


  

  



