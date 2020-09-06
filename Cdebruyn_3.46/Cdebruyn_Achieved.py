#Name: Time for Maths!
#Author: Connor de Bruyn
#Date: 28/2/18
#Ver: 1


########################################################################################################
##  IMPORTS/VARIABLES START HERE  ##  IMPORTS/VARIABLES START HERE  ##  IMPORTS/VARIABLES START HERE  ##
########################################################################################################

#Importing tkinter modules and a random module
from tkinter import *
import random
root = Tk()

#List of possible answers in the addition gamemode
listAddition1 = [1,2,3,4,5,6]

#Standard variables used all over code
roundinput = StringVar()
entry2 = object()
intGamemode = 1
intRound = 0
intLevel = 1
symbol = "+"
list_picked1 = []
list_picked2 = []
list_picked3 = []
user_picked = []
strAccept = "False"
intColour = 0
intScore = 0

##################################################################################################
##  CLASSES START HERE  ##  CLASSES START HERE  ##  CLASSES START HERE  ##  CLASSES START HERE  ##
##################################################################################################

#Shows the title screen with button to play
class Title_screen():
    
    def Page_one():
        global canvas, root
        print("User has entered main screen")
        Container.ConstantLayout()
        
        #Makes a title
        canvas.create_rectangle(150, 10, 850, 110, fill="white", outline="black")
        canvas.create_text(500, 60, text="Time for Maths!", font="Times 46 bold")
        
        #Creates a play button for them to press
        play_button = Button(root, text="Play", font="Times 40 bold", width=300, bg="red", command=pick)
        canvas.create_window(500,437, width=300, height=75, window=play_button)
        canvas.pack()
        canvas.update()
        
#This will be displayed on every page, this class will always be called up on startup for each page
class Container():  
    
    def ConstantLayout():
        global canvas, tkinter, root, entry2, entry
        #delete_entry()
        #Deletes everything from previous pages, so new pages dont have old widgets
        canvas.delete("all")
        
        
        #Creates Quit button
        quit_button = Button(root, text="Quit", font="Times 18 bold", width=100, bg="red", command=quit)
        canvas.create_window(52,577, width=100, height=50, window=quit_button)

#This will run the game with the gamemode, level and correct numbers in equations
class Game():

    def creategame():
        global strAccept, intColour
        print("User is now playing ze game")
        print(list_picked1)
        print(list_picked3)
        print(list_picked2)
        intColour = 0
        #4 rounds to ask questions
        if strAccept != "True":
            Game.loop()   
        elif strAccept == "True":
            print("User at results screen")
            end_screen.showscreen()

    #This will run the next equation in the loop, until the user puts in a suitable answer -> the next equation will show
    def loop():
        global strAccept
        if intRound == 0:
            Container.ConstantLayout()
            canvas.create_rectangle(100,50,900,350, fill="white", outline="black")
            canvas.create_rectangle(100,350,900,425, fill="grey", outline="black")
            canvas.create_text(500,200,text=(str(list_picked2[0]),symbol,str(list_picked3[0]),"=", "?"),font="Times 70 bold")
            Game.gameask()
            
        elif intRound == 1:
            Container.ConstantLayout()
            canvas.create_rectangle(100,50,900,350, fill="white", outline="black")
            canvas.create_rectangle(100,350,900,425, fill="grey", outline="black")
            canvas.create_text(500,200,text=(str(list_picked2[1]),symbol,str(list_picked3[1]),"=", "?"),font="Times 70 bold")
            Game.gameask()

        elif intRound == 2:
            Container.ConstantLayout()
            canvas.create_rectangle(100,50,900,350, fill="white", outline="black")
            canvas.create_rectangle(100,350,900,425, fill="grey", outline="black")
            canvas.create_text(500,200,text=(str(list_picked2[2]),symbol,str(list_picked3[2]),"=", "?"),font="Times 70 bold")
            Game.gameask()

        elif intRound == 3:
            Container.ConstantLayout()
            canvas.create_rectangle(100,50,900,350, fill="white", outline="black")
            canvas.create_rectangle(100,350,900,425, fill="grey", outline="black")
            canvas.create_text(500,200,text=(str(list_picked2[3]),symbol,str(list_picked3[3]),"=", "?"),font="Times 70 bold")
            Game.gameask()
            strAccept = "True"

    #Creates an entry box to type in for game
    def gameask():
        global entry2, roundinput
        entry2 = Entry(root, textvariable = roundinput, width=33, font="Times 13 bold")
        entry2.insert(15, "")
        entry2.pack()
        entry2.place(x=350, y=382)
        entry2.focus_set()
        button2 = Button(root, text = "Enter", width = 10, command = roundcheck)
        canvas.create_window(685, 395, height=25, width=60, window=button2)
            
    #Inputs the answer into user guessed list if the answer has a suitable value
    def nextround():
        global user_picked, intRound, entry2
        roundguess = roundinput.get()
        roundguess = int(roundguess)
        user_picked.append(roundguess)
        entry2.delete(0, "end")
        entry2.destroy()
        intRound += 1
        print(user_picked)
        Game.creategame()

    #Tally's up score and shows user when they reach the results screen
    def changescore():
        global round_score, intScore #if intscore < 3 then do one line with listpicked[intscore]
        if intScore == 0:
            if list_picked1[0] == user_picked[0]:
                round_score += 1
                intScore += 1
            else:
                intScore += 1
        elif intScore == 1:
            if list_picked1[1] == user_picked[1]:
                round_score += 1
                intScore += 1
            else:
                intScore += 1
        elif intScore == 2:
            if list_picked1[2] == user_picked[2]:
                round_score += 1
                intScore += 1
            else:
                intScore += 1
        elif intScore == 3:
            if list_picked1[3] == user_picked[3]:
                round_score += 1
                intScore += 1
            else:
                intScore += 1
        else:
            pass
        

#Shows the finishing results for the game, correct answers and what the user guessed            
class end_screen():

    #Shows a table with results
    def showscreen():
        Container.ConstantLayout()
        #Creating table look
        canvas.create_rectangle(150,50,850,100, fill="light grey", outline="black")
        canvas.create_rectangle(150,100,850,140, fill="grey", outline="black")
        canvas.create_rectangle(150,140,850,400, fill="white", outline="black")
        canvas.create_line(150,205,850,205, fill="black")
        canvas.create_line(150,270,850,270, fill="black")
        canvas.create_line(150,335,850,335, fill="black")
        canvas.create_line(500,100,500,400, fill="black")
        canvas.create_text(500,75, text="Results Table", font="Times 25 bold")
        canvas.create_text(490,120, text="Correct Answers                                 Your Answers", font = "Times 20 bold")
        #Creating correct answers
        canvas.create_text(325,177, text=(str(list_picked1[0])), font="Times 35 bold", fill="black")
        canvas.create_text(325,242, text=(str(list_picked1[1])), font="Times 35 bold", fill="black")
        canvas.create_text(325,307, text=(str(list_picked1[2])), font="Times 35 bold", fill="black")
        canvas.create_text(325,372, text=(str(list_picked1[3])), font="Times 35 bold", fill="black")

        #User answers
        canvas.create_text(675,177, text=(str(user_picked[0])), font="Times 35 bold", fill="black")
        canvas.create_text(675,242, text=(str(user_picked[1])), font="Times 35 bold", fill="black")
        canvas.create_text(675,307, text=(str(user_picked[2])), font="Times 35 bold", fill="black")
        canvas.create_text(675,372, text=(str(user_picked[3])), font="Times 35 bold", fill="black")

        game_button = Button(root, text="Continue", font="Times 32 bold", width=300, bg="red", command=Title_screen.Page_one)
        canvas.create_window(500,487, width=300, height=75, window=game_button)

##################################################################################################################    
## STANDARD DEFS START HERE ## STANDARD DEFS START HERE ## STANDARD DEFS START HERE ## STANDARD DEFS START HERE ##
##################################################################################################################

##Creates the window for the canvas to be made on all pages past this point
def open():
    global tkinter, canvas, root
    root.title("Time for Maths! by Connor de Bruyn")
    canvas = Canvas(root, width = 1000, height = 600, bg = "beige")
    Title_screen.Page_one()
    root.mainloop()
    
#Quits the program
def quit():
    root.destroy()

#Checks if the inputted data is usable, gives a visual error if unusable
def roundcheck():
    roundguess = roundinput.get()
    try:
        int(roundguess)
        if int(roundguess) < 0:
            canvas.create_rectangle(325,435,675,525, fill="white", outline="black")
            canvas.create_text(500,450, text="Sorry!", font="Times 15 bold")
            canvas.create_text(500, 485, text="You cannot have a number under 0.", font="Times 14 bold")
        elif int(roundguess) > 9999:
            canvas.create_rectangle(325,435,675,525, fill="white", outline="black")
            canvas.create_text(500,450, text="Sorry!", font="Times 15 bold")
            canvas.create_text(500, 485, text="You cannot have a number over 9999.", font="Times 14 bold")
        else:
            Game.nextround()
    except ValueError:
        canvas.create_rectangle(325,435,675,525, fill="white", outline="black")
        canvas.create_text(500,450, text="Sorry!", font="Times 15 bold")
        canvas.create_text(500, 485, text="You need to input an interger.", font="Times 14 bold")

#Gets numbers then runs game
def pick():
    numberpicker()
    Game.creategame()

#Number picking definition (picks a 4 random numbers appended to a list to be used in each gamemode/level)
def numberpicker():
    global list_picked1, list_picked2, list_picked3, strAccept, user_picked
    user_picked = []
    list_picked1 = []
    list_picked2 = []
    list_picked3 = []
    strAccept = "False"
    x = 0
    y = 0
    z = 0
    #Addition mode
    if intGamemode == 1:
        if intLevel == 1:#Level 1
            while x < 4:
                choice = random.choice(listAddition1)#listAddition(intLevel)?
                list_picked1.append(choice)
                choice = 0
                x += 1
                
            while z < 4:
                choice = random.randint(1, listAddition1[z])
                choice = (choice - 1)
                list_picked2.append(choice)
                choice = 0
                z += 1

            while y < 4:
                choice = list_picked1[y] - list_picked2[y]
                list_picked3.append(choice)
                choice = 0
                y += 1

        elif intLevel == 2:#Level 2
            while x < 4:
                choice = random.choice(listAddition2)
                list_picked1.append(choice)
                choice = 0
                x += 1
                
            while z < 4:
                choice = random.randint(1, listAddition2[z])
                choice = (choice - 1)
                list_picked2.append(choice)
                choice = 0
                z += 1

            while y < 4:
                choice = list_picked1[y] - list_picked2[y]
                list_picked3.append(choice)
                choice = 0
                y += 1

        elif intLevel == 3:#Level 3
            while x < 4:
                choice = random.choice(listAddition3)
                list_picked1.append(choice)
                choice = 0
                x += 1
                
            while z < 4:
                choice = random.randint(1, listAddition3[z])
                choice = (choice - 1)
                list_picked2.append(choice)
                choice = 0
                z += 1

            while y < 4:
                choice = list_picked1[y] - list_picked2[y]
                list_picked3.append(choice)
                choice = 0
                y += 1
        else:
            pass
               
#Runs the program
open()
