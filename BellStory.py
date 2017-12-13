# Add time wiht time.sleep(5) later so the user has time to read m8 
import turtle
import time 
def greeting():
    print("Hello..")
    response=input("Do you want to play? (yes/no): ")
    return response

def second_choice():
    time.sleep(2)
    print("Good your a turtle named mixtape and you make fire shapes that are bought by other turtles")
    response=input("Will your first mixtape me a square mixtape (yes) or a circle mixtape (no)?")
    return response

def deny():
    time.sleep(1)
    print("GTFO don't even come back to this computer you scrub")
    
def opened():
    time.sleep(1)
    print("Your square only makes 10,000 shells due to every other turtle being able to make fire squares")
     
    m = turtle.Turtle()
    m.speed(0)
    for i in range(4):
        m.forward(100)
        m.right(90)

def not_opened():
    time.sleep(1)
    print("You forge the most fire circle ever created and make 100,000 shells")
     
    m = turtle.Turtle()
    m.speed(0)
    m.circle(30)
      
def record_deal():
    time.sleep(1)
    print("You are a good fire shape artist and turtle record notices and offers you 900,000,000 shells to make the most fire shape mixer ever!")
    response=input("Will you accept this fire offer??? (Y/N)")
    return response
def rip():
    print("You say no to the most fire offer ever and work on your own shapes and stay an okay fire shape maker but fall off due to all the seacane you do")
    time.sleep(1)
    print("SIMI END.. You got the worst possible ending you scrub I hope you feel bad for ruining that turtles life with your bad decision making!")
    response=input("You find your self simping in a ally way while your number 1 competitor is walking down the ally way and is responsible for your tapes failing. Do you shell up with him and turtle fight him or leave it alone and keep to yourself... simping (Y/N)")
    return response

def end():
    time.sleep(1)
    print("You become the most fire shape maker in all of the pond and you become the number 1 fire shape maker..... you see your archrival and you bump shoulders... ehe then disrespects your fire shapes and YOU GET INTO A SHELL FIGHT!")
def thug_life():
    time.sleep(1)
    print("You shell him up so bad he goes away for ever and quits the shell game and you come back and create a new genre called gangster shape fire which takes off and you become the under ground fire shape maker. You also adopt a new name... Yurtle The Turtle. THUG_LIFE ending ")
def cat():
    time.sleep(1)
    print("You let him walk by and you life flashed by you and you die of all shellcain you did back in the day.")

x = greeting()
if x=="yes":


     
    y = second_choice()
    if y=="yes":
        opened()
    else:
        
        not_opened()

    if x=="yes":

        y = record_deal()
    if y=="yes":
    
        end()
        



    else:

        if x=="yes":
            y = rip()
    if y=="yes":
        thug_life()
    else:
            cat()


        
   
         
else:
        deny()



    

 
