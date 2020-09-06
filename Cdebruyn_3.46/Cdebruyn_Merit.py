#Name: Time for Maths!
#Author: Connor de Bruyn
#Date: 20/4/18
#Ver: 2


########################################################################################################
##  IMPORTS/VARIABLES START HERE  ##  IMPORTS/VARIABLES START HERE  ##  IMPORTS/VARIABLES START HERE  ##
########################################################################################################

#Importing tkinter modules and a random module
from tkinter import *
import random
root = Tk()

#List of possible answers in the addition gamemode
listAddition1 = [1,2,3,4,5,6]
listAddition2 = [9,10,11,12,13,14,15,17,18]
listAddition3 = [25,27,29,32,37,39,41,45,48,50,55]

#List of possible first numbers that are subtracted from in subtraction gamemode
listSubtraction1 = [3,4,5,6,7,8]
listSubtraction2 = [8,9,10,11,12,13,14,15,16,17]
listSubtraction3 = [19,20,23,25,26,28,29,31,34,37,43]

#List of all posible first numbers in the multiplication gamemode
listMultiplication1 = [1,2,3,4,5]
listMultiplication2 = [5,6,7,8,9,10,11,12]
listMultiplication3 = [13,14,15,16,17,18,19,20,25]

#List of possible first numbers that are divisable from in division gamemode
listDivision1 = [1,2,3,4,5]
listDivision2 = [5,6,7,8,9,10,11,12]
listDivision3 = [13,14,15,16,17,18,19,20,25]

#Standard variables used all over code
total_score = 0
round_score = 0
entry = object()
username = StringVar()
roundinput = StringVar()
entry2 = object()
name = ""
intGamemode = 0
intRound = 0
intLevel = 0
phrase = ""
phrase2 = ""
phrase3 = ""
symbol = ""
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

##Creates the window for the canvas to be made on all pages past this point
class Open_window():

    def __init__(self):
        global tkinter, canvas, root
        root.title("Time for Maths! by Connor de Bruyn")
        canvas = Canvas(root, width = 1000, height = 600, bg = "beige")
        Title_screen.Page_one()
        root.mainloop()

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
        play_button = Button(root, text="Play", font="Times 40 bold", width=300, bg="red", command=Instruction.Instruction_screen)
        canvas.create_window(500,437, width=300, height=75, window=play_button)

        
        canvas.update()

#Creates an instructions screen telling them how to play, also calls up an enter username before showing instructions
class Instruction():

    def Instruction_screen():
        print("User is at enter name screen")
        ask()

    def Instructions():
        global entry
        Container.ConstantLayout()
        #entry.insert(15, "")
        #slide_down_animation()
        canvas.create_text(500, 50, text=phrase, font="Times 25 bold")
        canvas.create_text(500, 100, text="a maths game were you will be shown ", font="Times 25 bold")
        canvas.create_text(500, 150, text="an equation and type in the answer. ", font="Times 25 bold")
        canvas.create_text(500, 200, text="There are 4 gamemodes with 3 levels ", font="Times 25 bold")
        canvas.create_text(500, 250, text="of difficulty, dependant on what you", font="Times 25 bold")
        canvas.create_text(500, 300, text="choose the game will get easier to  ", font="Times 25 bold")
        canvas.create_text(500, 350, text="tougher. Hope you enjoy!   ~Connor", font="Times 25 bold")
        cont_button = Button(root, text="Continue", font="Times 32 bold", width=300, bg="red", command=Gamemode.Gameselect)
        canvas.create_window(500,437, width=300, height=75, window=cont_button)

#Creates a screen where they choose a gamemode that takes them to a level screen
class Gamemode():

    def Gameselect():
        global intGamemode, symbol
        symbol = ""
        intGamemode = 0
        print("User is at Game select screen")
        Container.ConstantLayout()

        canvas.create_text(500, 50, text=phrase2, font="Times 30 bold")
        
        #Creating buttons to pick a gamemode
        add_button = Button(root, text="Addition", font="Times 32 bold", width=300, bg="red", command=Gamemode.addpick)
        canvas.create_window(250, 250, width=350, height=100, window=add_button)

        sub_button = Button(root, text="Subtraction", font="Times 32 bold", width=300, bg="blue", command=Gamemode.subpick)
        canvas.create_window(750, 250, width=350, height=100, window=sub_button)

        mul_button = Button(root, text="Multiplication", font="Times 32 bold", width=300, bg="green", command=Gamemode.mulpick)
        canvas.create_window(250, 400, width=350, height=100, window=mul_button)

        div_button = Button(root, text="Division", font="Times 32 bold", width=300, bg="yellow", command=Gamemode.divpick)
        canvas.create_window(750, 400, width=350, height=100, window=div_button)

#Changes the intGamemode which decides what variables to use in the maths game
    def addpick():
        global intGamemode, symbol
        print("addition mode selected")
        intGamemode = 1
        symbol = "+"
        Level.addlevelselect()

    def subpick():
        global intGamemode, symbol
        print("subtraction mode selected")
        intGamemode = 2
        symbol = "-"
        Level.sublevelselect()

    def mulpick():
        global intGamemode, symbol
        print("multiplication mode selected")
        intGamemode = 3
        symbol = "x"
        Level.mullevelselect()

    def divpick():
        global intGamemode, symbol
        print("division mode selected")
        intGamemode = 4
        symbol = "/"
        Level.divlevelselect()
        
#User gets to a screen to pick a level, that level is saved under intLevel
class Level():
    
    def addlevelselect():
        global intLevel
        intLevel = 0
        print("User is at level select screen")
        Container.ConstantLayout()
        canvas.create_text(500, 50, text=phrase3, font="Times 30 bold")

        #Creating level buttons
        level1 = Button(root, text="Level 1", font="Times 32 bold", width=300, bg="red", command=Level.lev1pick)
        canvas.create_window(500, 200, width=350, height=75, window=level1)

        level2 = Button(root, text="Level 2", font="Times 32 bold", width=300, bg="red", command=Level.lev2pick)
        canvas.create_window(500, 300, width=350, height=75, window=level2)

        level3 = Button(root, text="Level 3", font="Times 32 bold", width=300, bg="red", command=Level.lev3pick)
        canvas.create_window(500, 400, width=350, height=75, window=level3)

    def sublevelselect():
        global intLevel
        intLevel = 0
        print("User is at level select screen")
        Container.ConstantLayout()
        canvas.create_text(500, 50, text=phrase3, font="Times 30 bold")

        #Creating level buttons
        level1 = Button(root, text="Level 1", font="Times 32 bold", width=300, bg="blue", command=Level.lev1pick)
        canvas.create_window(500, 200, width=350, height=75, window=level1)

        level2 = Button(root, text="Level 2", font="Times 32 bold", width=300, bg="blue", command=Level.lev2pick)
        canvas.create_window(500, 300, width=350, height=75, window=level2)

        level3 = Button(root, text="Level 3", font="Times 32 bold", width=300, bg="blue", command=Level.lev3pick)
        canvas.create_window(500, 400, width=350, height=75, window=level3)

    def mullevelselect():
        global intLevel
        intLevel = 0
        print("User is at level select screen")
        Container.ConstantLayout()
        canvas.create_text(500, 50, text=phrase3, font="Times 30 bold")

        #Creating level buttons
        level1 = Button(root, text="Level 1", font="Times 32 bold", width=300, bg="green", command=Level.lev1pick)
        canvas.create_window(500, 200, width=350, height=75, window=level1)

        level2 = Button(root, text="Level 2", font="Times 32 bold", width=300, bg="green", command=Level.lev2pick)
        canvas.create_window(500, 300, width=350, height=75, window=level2)

        level3 = Button(root, text="Level 3", font="Times 32 bold", width=300, bg="green", command=Level.lev3pick)
        canvas.create_window(500, 400, width=350, height=75, window=level3)

    def divlevelselect():
        global intLevel, intRound
        intRound = 0
        intLevel = 0
        print("User is at level select screen")
        Container.ConstantLayout()
        canvas.create_text(500, 50, text=phrase3, font="Times 30 bold")

        #Creating level buttons
        level1 = Button(root, text="Level 1", font="Times 32 bold", width=300, bg="yellow", command=Level.lev1pick)
        canvas.create_window(500, 200, width=350, height=75, window=level1)

        level2 = Button(root, text="Level 2", font="Times 32 bold", width=300, bg="yellow", command=Level.lev2pick)
        canvas.create_window(500, 300, width=350, height=75, window=level2)

        level3 = Button(root, text="Level 3", font="Times 32 bold", width=300, bg="yellow", command=Level.lev3pick)
        canvas.create_window(500, 400, width=350, height=75, window=level3)

#Changes the intLevel dependant on which button pressed
    def lev1pick():
        global intLevel
        print("level 1 selected")
        intLevel = 1
        numberpicker()
        Game.creategame()

    def lev2pick():
        global intLevel
        print("level 2 selected")
        intLevel = 2
        numberpicker()
        Game.creategame()

    def lev3pick():
        global intLevel
        print("level 3 selected")
        intLevel = 3
        numberpicker()
        Game.creategame()
        
#This will be displayed on every page, this class will always be called up on startup for each page
class Container():  
    
    def ConstantLayout():
        global canvas, tkinter, root, entry2, entry
        #delete_entry()
        #Deletes everything from previous pages, so new pages dont have old widgets
        canvas.delete("all")
        
        
        #Creates Quit and home buttons
        quit_button = Button(root, text="Quit", font="Times 18 bold", width=100, bg="red", command=quit)
        canvas.create_window(52,577, width=100, height=50, window=quit_button)

        #Creates score box
        canvas.create_rectangle(400,550,600,600, fill="white", outline="black")
        canvas.create_text(475, 575, text="Score:", font="Times 18 bold")
        scoreupdate()

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
            while intScore < 3:
                Game.changescore()
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
        global intRound, intScore
        intRound = 0
        Container.ConstantLayout()
        intScore = 0
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
        canvas.create_text(675,177, text=(str(user_picked[0])), font="Times 35 bold", fill=end_screen.colourchange())
        canvas.create_text(675,242, text=(str(user_picked[1])), font="Times 35 bold", fill=end_screen.colourchange())
        canvas.create_text(675,307, text=(str(user_picked[2])), font="Times 35 bold", fill=end_screen.colourchange())
        canvas.create_text(675,372, text=(str(user_picked[3])), font="Times 35 bold", fill=end_screen.colourchange())

        game_button = Button(root, text="Continue", font="Times 32 bold", width=300, bg="red", command=Gamemode.Gameselect)
        canvas.create_window(500,487, width=300, height=75, window=game_button)

    #Changes the colour of the picked dependandt on if their right, also tally's score
    def colourchange():
        global intColour
        if intColour == 0:
            if list_picked1[0] == user_picked[0]:
                intColour += 1
                return "green"
            else:
                intColour += 1
                return "red"
        elif intColour == 1:
            if list_picked1[1] == user_picked[1]:
                intColour += 1
                return "green"
            else:
                intColour += 1
                return "red"
        elif intColour == 2:
            if list_picked1[2] == user_picked[2]:
                intColour += 1
                return "green"
            else:
                intColour += 1
                return "red"
        else:
            if list_picked1[3] == user_picked[3]:
                intColour += 1
                return "green"
            else:
                intColour += 1
                return "red"
            
                           

##################################################################################################################    
## STANDARD DEFS START HERE ## STANDARD DEFS START HERE ## STANDARD DEFS START HERE ## STANDARD DEFS START HERE ##
##################################################################################################################

#Deleting entries
##def delete_entry():
    ##global entry, entry2
    ##entry.destroy()
    ##entry2.destroy()

#Quits the program
def quit():
    root.destroy()

#Tally's up scores and saves them to be displayed     
def scoreupdate():
    global round_score, total_score
    total_score += round_score#make sure to turn rscore to 0 after calling def
    round_score = 0
    canvas.create_text(525, 575, text=total_score, font="Times 20 bold", anchor=E)
    canvas.pack()
    canvas.update()

##Creates a window to get a username from
def ask():
    global username, entry, root
    Container.ConstantLayout()
    canvas.create_text(475, 270, text="Please enter a username:", font="Times 18 bold")
    entry = Entry(root, textvariable = username, width=33, font="Times 13 bold")
    entry.pack()
    entry.place(x=350, y=300)
    entry.focus_set()
    button1 = Button(root, text = "Submit", width = 10, command = check_name)
    canvas.create_window(685, 310, height=25, width=60, window=button1)
    
    
    
#Checks if name is suitable for running (error catches)
def check_name():
    global canvas, phrase, phrase2, phrase3
    name = (username.get())
    name = name.strip().title()
    length = len(name)
    print(name)
    if name == "":
        canvas.create_rectangle(350,330,650,430, fill="white", outline="black")
        canvas.create_text(500, 350, text="Sorry!", font="Times 15 bold")
        canvas.create_text(500, 395, text="Please enter a username ", font="Times 14 bold") 
    elif length < 2 or length > 12:
        canvas.create_rectangle(350,330,650,430, fill="white", outline="black")
        canvas.create_text(500, 350, text="Sorry!", font="Times 15 bold")
        canvas.create_text(500, 385, text="Your username needs to", font="Times 14 bold")
        canvas.create_text(500, 405, text="be between 2-12 characters.", font="Times 14 bold")#Do a value error, error catch
    else:
        phrase = ("Hello {}! Today you will be playing".format(name))
        phrase2 = ("{}, Please choose a gamemode".format(name))
        phrase3 = ("{}, Please select a level".format(name))
        entry.delete(0, "end")
        entry.destroy()
        Instruction.Instructions()

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

#Generates a random colour and returns it        
def randomColour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return "#%02x%02x%02x"%(r,g,b)

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
    #Subtraction mode
    elif intGamemode == 2:
        if intLevel == 1:#Level 1
            while x < 4:
                choice = random.choice(listSubtraction1)
                list_picked2.append(choice)
                choice = 0
                x += 1
                
            while z < 4:
                choice = random.randint(1, listSubtraction1[z])
                choice = (choice - 1)
                list_picked3.append(choice)
                choice = 0
                z += 1

            while y < 4:
                choice = list_picked2[y] - list_picked3[y]
                list_picked1.append(choice)
                choice = 0
                y += 1

        elif intLevel == 2:#Level 2
            while x < 4:
                choice = random.choice(listSubtraction2)
                list_picked2.append(choice)
                choice = 0
                x += 1
                
            while z < 4:
                choice = random.randint(1, listSubtraction2[z])
                choice = (choice - 1)
                list_picked3.append(choice)
                choice = 0
                z += 1

            while y < 4:
                choice = list_picked2[y] - list_picked3[y]
                list_picked1.append(choice)
                choice = 0
                y += 1

        elif intLevel == 3:#Level 3
            while x < 4:
                choice = random.choice(listSubtraction3)
                list_picked2.append(choice)
                choice = 0
                x += 1
                
            while z < 4:
                choice = random.randint(1, listSubtraction3[z])
                choice = (choice - 1)
                list_picked3.append(choice)
                choice = 0
                z += 1

            while y < 4:
                choice = list_picked2[y] - list_picked3[y]
                list_picked1.append(choice)
                choice = 0
                y += 1
    #Multiplication mode
    elif intGamemode == 3:
        if intLevel == 1:#Level 1
            while x < 4:
                choice = random.choice(listMultiplication1)
                list_picked2.append(choice)
                choice = 0
                x += 1
                
            while z < 4:
                choice = random.choice(listMultiplication1)
                list_picked3.append(choice)
                choice = 0
                z += 1

            while y < 4:
                choice = list_picked3[y] * list_picked2[y]
                list_picked1.append(choice)
                choice = 0
                y += 1

        elif intLevel == 2:#Level 2
            while x < 4:
                choice = random.choice(listMultiplication2)
                list_picked2.append(choice)
                choice = 0
                x += 1
                
            while z < 4:
                choice = random.choice(listMultiplication1)
                list_picked3.append(choice)
                choice = 0
                z += 1

            while y < 4:
                choice = list_picked3[y] * list_picked2[y]
                list_picked1.append(choice)
                choice = 0
                y += 1

        elif intLevel == 3:#Level 3
            while x < 4:
                choice = random.choice(listMultiplication3)
                list_picked2.append(choice)
                choice = 0
                x += 1
                
            while z < 4:
                choice = random.choice(listMultiplication2)
                list_picked3.append(choice)
                choice = 0
                z += 1

            while y < 4:
                choice = list_picked3[y] * list_picked2[y]
                list_picked1.append(choice)
                choice = 0
                y += 1
    #Division mode    
    elif intGamemode == 4:
        if intLevel == 1:#Level 1
            while x < 4:
                choice = random.choice(listDivision1)
                list_picked1.append(choice)
                choice = 0
                x += 1
                
            while z < 4:
                choice = random.choice(listDivision1)
                list_picked3.append(choice)
                choice = 0
                z += 1

            while y < 4:
                choice = list_picked1[y] * list_picked3[y]
                list_picked2.append(choice)
                choice = 0
                y += 1

        elif intLevel == 2:#Level 2
            while x < 4:
                choice = random.choice(listDivision1)
                list_picked1.append(choice)
                choice = 0
                x += 1
                
            while z < 4:
                choice = random.choice(listDivision2)
                list_picked3.append(choice)
                choice = 0
                z += 1

            while y < 4:
                choice = list_picked1[y] * list_picked3[y]
                list_picked2.append(choice)
                choice = 0
                y += 1

        elif intLevel == 3:#Level 3
            while x < 4:
                choice = random.choice(listDivision2)
                list_picked1.append(choice)
                choice = 0
                x += 1
                
            while z < 4:
                choice = random.choice(listDivision3)
                list_picked3.append(choice)
                choice = 0
                z += 1

            while y < 4:
                choice = list_picked1[y] * list_picked3[y]
                list_picked2.append(choice)
                choice = 0
                y += 1
        
            
#Runs the program
Open_window()
