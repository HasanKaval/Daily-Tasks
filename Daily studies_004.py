# We have a loud talking parrot. We are in trouble if the parrot is talking and the hour is before 6 or after 21.
# Define a function taking two parameters (talking and hour) to return True if we are in trouble. 

def parrot_trouble(talking, hour) :
    if (hour < 6 or hour > 21) and talking == True :
        return True
    else :
        return False
print(parrot_trouble(True, 5))
