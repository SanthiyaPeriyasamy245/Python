 

 import random

guessing_number=random.randint(1,100)

while(True):
    try:
        n=(int)(input("enter your guess"))
        if n<guessing_number:
            print("too low")
        elif n>guessing_number:
            print("too high")
        else:
            print("congratulations you won !")
            break
    except ValueError:
        
        print('Please enter a valid number')    
    
   
   
