# We have a loud talking parrot. We are in trouble if the parrot is talking and the hour is before 6 or after 21.
# Define a function taking two parameters (talking and hour) to return True if we are in trouble. 

def parrot_trouble(talking, hour) :
    if (hour < 6 or hour > 21) and talking == True :
        return True
    else :
        return False
print(parrot_trouble(True, 5))
print()

#Define a function to take a word and return negative meaning.
#Given a word, return a new word where "not " has been added to the front.
#However, if the word already begins with "not", return the string unchanged.

def not_string(word):
    x = slice(0,3)
    if word[x] == "not" :
        return(word)
    else :
        return("not " + word)
print(not_string('not bad'))
print()


