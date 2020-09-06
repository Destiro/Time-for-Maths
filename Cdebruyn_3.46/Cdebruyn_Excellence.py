#Name: Time for Maths!
#Author: Connor de Bruyn
#Date: 21/4/18
#Ver: 3


########################################################################################################
##  IMPORTS/VARIABLES START HERE  ##  IMPORTS/VARIABLES START HERE  ##  IMPORTS/VARIABLES START HERE  ##
########################################################################################################

#Importing tkinter modules and a random module
from tkinter import *
import random
root = Tk()
background = PhotoImage(file="background.gif")

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
total_played = 0
round_played = 0
intRun = 0

##################################################################################################
##  CLASSES START HERE  ##  CLASSES START HERE  ##  CLASSES START HERE  ##  CLASSES START HERE  ##
##################################################################################################

##Creates the window for the canvas to be made on all pages past this point
class Open_window():
    def __init__(self):
        global tkinter, canvas, root
        root.title("Time for Maths! by Connor de Bruyn")
        root.resizable(0,0)
        canvas = Canvas(root, width = 1000, height = 600, bg = 'black', highlightthickness=0, relief='ridge')
        Title_screen.Page_one()
        root.mainloop()

#Shows the title screen with button to play
class Title_screen():
    def Page_one():
        global canvas, root
        Container.ConstantLayout()
        #Makes a title
        canvas.create_rectangle(150, 10, 850, 110, fill="white", outline="black")
        canvas.create_text(500, 60, text="Time for Maths!", font="Verdana 46 bold")
        
        #Creates a play button for them to press
        play_button = Button(root, text="Play", font="Ariel 40 bold", width=300, bg="red", command=Instruction.Instruction_screen)
        canvas.create_window(500,350, width=350, height=100, window=play_button)
        canvas.create_text(500,460, text="By Connor de Bruyn 2018", font="Ariel 26 bold")
        canvas.create_text(500,500, text="Endorsed by © Flow Computing", font="Ariel 20 bold")
        
        canvas.update()

#Creates an instructions screen telling them how to play, also calls up an enter username before showing instructions
class Instruction():
    def Instruction_screen():
        ask()

    def Instructions():
        global entry
        Container.ConstantLayout()
        canvas.create_text(500, 50, text=phrase, font="Ariel 25 bold")
        canvas.create_text(500, 100, text="a maths game were you will be shown ", font="Ariel 25 bold")
        canvas.create_text(500, 150, text="an equation and type in the answer. ", font="Ariel 25 bold")
        canvas.create_text(500, 200, text="There are 4 gamemodes with 3 levels ", font="Ariel 25 bold")
        canvas.create_text(500, 250, text="of difficulty, dependant on what you", font="Ariel 25 bold")
        canvas.create_text(500, 300, text="choose the game will get easier to  ", font="Ariel 25 bold")
        canvas.create_text(500, 350, text="tougher. Hope you enjoy!   ~Connor", font="Ariel 25 bold")
        cont_button = Button(root, text="Continue", font="Ariel 32 bold", width=300, bg="red", command=Gamemode.Gameselect)
        canvas.create_window(500,437, width=300, height=75, window=cont_button)

#Creates a screen where they choose a gamemode that takes them to a level screen
class Gamemode():
    def Gameselect():
        global intGamemode, symbol
        symbol = ""
        intGamemode = 0
        Container.ConstantLayout()
        canvas.create_text(500, 50, text=phrase2, font="Ariel 30 bold")
        
        #Creating buttons to pick a gamemode
        add_button = Button(root, text="Addition", font="Ariel 32 bold", width=300, bg="red", command=Gamemode.addpick)
        canvas.create_window(250, 250, width=350, height=100, window=add_button)

        sub_button = Button(root, text="Subtraction", font="Ariel 32 bold", width=300, bg="light blue", command=Gamemode.subpick)
        canvas.create_window(750, 250, width=350, height=100, window=sub_button)

        mul_button = Button(root, text="Multiplication", font="Ariel 32 bold", width=300, bg="green", command=Gamemode.mulpick)
        canvas.create_window(250, 400, width=350, height=100, window=mul_button)

        div_button = Button(root, text="Division", font="Ariel 32 bold", width=300, bg="yellow", command=Gamemode.divpick)
        canvas.create_window(750, 400, width=350, height=100, window=div_button)

#Changes the intGamemode which decides what variables to use in the maths game
    def addpick(): #User picks addition mode
        global intGamemode, symbol
        intGamemode = 1
        symbol = "+"
        Level.addlevelselect()

    def subpick(): #User picks subtraction mode
        global intGamemode, symbol
        intGamemode = 2
        symbol = "-"
        Level.addlevelselect()

    def mulpick(): #User picks multiplication mode
        global intGamemode, symbol
        intGamemode = 3
        symbol = "x"
        Level.addlevelselect()

    def divpick(): #User picks division mode
        global intGamemode, symbol
        intGamemode = 4
        symbol = "/"
        Level.addlevelselect()
        
#User gets to a screen to pick a level, that level is saved under intLevel
class Level():
    def addlevelselect():
        global intLevel
        intLevel = 0
        Container.ConstantLayout()
        canvas.create_text(500, 50, text=phrase3, font="Ariel 30 bold")

        #Creating level buttons
        level1 = Button(root, text="Level 1", font="Ariel 32 bold", width=300, bg=Level.levelbutton_colour(), command=Level.lev1pick)
        canvas.create_window(500, 200, width=350, height=75, window=level1)
        level2 = Button(root, text="Level 2", font="Ariel 32 bold", width=300, bg=Level.levelbutton_colour(), command=Level.lev2pick)
        canvas.create_window(500, 300, width=350, height=75, window=level2)
        level3 = Button(root, text="Level 3", font="Ariel 32 bold", width=300, bg=Level.levelbutton_colour(), command=Level.lev3pick)
        canvas.create_window(500, 400, width=350, height=75, window=level3)

    #Returns the colour for the level buttons depending on what gamemode chosen
    def levelbutton_colour():
        if intGamemode == 1:
            return "red"
        elif intGamemode == 2:
            return "light blue"
        elif intGamemode == 3:
            return "green"
        elif intGamemode == 4:
            return "yellow"

#Changes the intLevel dependant on which button pressed
    def lev1pick():
        global intLevel
        intLevel = 1
        numberpicker()
        Game.creategame()

    def lev2pick():
        global intLevel
        intLevel = 2
        numberpicker()
        Game.creategame()

    def lev3pick():
        global intLevel
        intLevel = 3
        numberpicker()
        Game.creategame()
        
#This will be displayed on every page, this class will always be called up on startup for each page
class Container():  
    def ConstantLayout():
        global canvas, tkinter, root, entry2, entry
        #Deletes everything from previous pages, so new pages dont have old widgets
        canvas.delete("all")
        canvas.create_image(500,0, image=background, anchor=N)
        
        #Creates Quit and home buttons
        quit_button = Button(root, text="Quit", font="Ariel 18 bold", width=100, bg="red", command=quit)
        canvas.create_window(50,577, width=100, height=50, window=quit_button)
        home_button = Button(root, text="Home", font="Ariel 18 bold", width=100, bg="red", command=delete_entry)
        canvas.create_window(952, 577, width=100, height=50, window=home_button)

        #Creates score box
        scoreupdate()

#This will run the game with the gamemode, level and correct numbers in equations
class Game():
    def creategame():
        global strAccept, intColour
        intColour = 0
        #4 rounds to ask questions
        if strAccept != "True":
            Game.loop()   
        elif strAccept == "True":
            while intScore < 4:
                Game.changescore()
            end_screen.showscreen()

    #This will run the next equation in the loop, until the user puts in a suitable answer -> the next equation will show
    def loop():
        global strAccept
        if intRound < 3:
            Game.loop_visual()
            
        elif intRound == 3:
            Game.loop_visual()
            strAccept = "True"

    #Creates the equation shown on the game screen
    def loop_visual():
        Container.ConstantLayout()
        canvas.create_rectangle(100,50,900,350, fill="white", outline="black")
        canvas.create_rectangle(100,350,900,425, fill="grey", outline="black")
        canvas.create_text(500,200,text=(str(list_picked2[intRound]),symbol,str(list_picked3[intRound]),"=", "?"),font="Ariel 70 bold")
        Game.gameask()

    #Creates an entry box to type in for game
    def gameask():
        global entry2, roundinput
        entry2 = Entry(root, textvariable = roundinput, width=33, font="Ariel 13 bold")
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
        global round_score, intScore, round_played #if intscore < 3 then do one line with listpicked[intscore]
        if intScore < 3:
            if list_picked1[intScore] == user_picked[intScore]:
                round_score += 1
                intScore += 1
            else:
                intScore += 1
        else:
            if list_picked1[intScore] == user_picked[intScore]:
                round_score += 1
                intScore += 1
                round_played = 4
            else:
                intScore += 1
                round_played = 4
        
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
        canvas.create_text(500,75, text="Results Table", font="Ariel 25 bold")
        canvas.create_text(490,120, text="Correct Answers                        Your Answers", font = "Ariel 20 bold")
        #Creating correct answers
        canvas.create_text(325,177, text=(str(list_picked1[0])), font="Ariel 35 bold", fill="black")
        canvas.create_text(325,242, text=(str(list_picked1[1])), font="Ariel 35 bold", fill="black")
        canvas.create_text(325,307, text=(str(list_picked1[2])), font="Ariel 35 bold", fill="black")
        canvas.create_text(325,372, text=(str(list_picked1[3])), font="Ariel 35 bold", fill="black")

        #User answers
        canvas.create_text(675,177, text=(str(user_picked[0])), font="Ariel 35 bold", fill=end_screen.colourchange())
        canvas.create_text(675,242, text=(str(user_picked[1])), font="Ariel 35 bold", fill=end_screen.colourchange())
        canvas.create_text(675,307, text=(str(user_picked[2])), font="Ariel 35 bold", fill=end_screen.colourchange())
        canvas.create_text(675,372, text=(str(user_picked[3])), font="Ariel 35 bold", fill=end_screen.colourchange())

        game_button = Button(root, text="Continue", font="Ariel 32 bold", width=300, bg="red", command=Gamemode.Gameselect)
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
def delete_entry():
    global entry, entry2, total_score, total_played
    try:
        entry.destroy()
        entry2.destroy()
    except:
        pass

    total_score = 0
    total_played = 0
    Title_screen.Page_one()

#Quits the program
def quit():
    root.destroy()

#Tally's up scores and saves them to be displayed     
def scoreupdate():
    global round_score, total_score, round_played, total_played
    canvas.create_rectangle(400,550,600,600, fill="white", outline="black")
    total_score += round_score
    round_score = 0
    total_played += round_played
    round_played = 0
    canvas.create_text(500, 575, text=("Score:", str(total_score), "/", str(total_played)), font="Ariel 20 bold")
    canvas.pack()
    canvas.update()

##Creates a window to get a username from
def ask():
    global username, entry, root
    #root.bind("<Return>", enter)
    Container.ConstantLayout()
    canvas.create_text(495, 270, text="Please enter a username:", font="Ariel 18 bold")
    entry = Entry(root, textvariable = username, width=33, font="Ariel 13 bold")
    entry.pack()
    entry.place(x=350, y=300)
    entry.focus_set()
    button1 = Button(root, text = "Submit", width = 10, command = check_name)
    canvas.create_window(685, 312, height=25, width=60, window=button1)
    
#Checks if name is suitable for running (error catches)
def check_name():
    global canvas, phrase, phrase2, phrase3
    name = (username.get())
    name = name.strip().title()
    length = len(name)
    if name == "":
        canvas.create_rectangle(350,330,650,430, fill="white", outline="black")
        canvas.create_text(500, 350, text="Sorry!", font="Ariel 18 bold", fill="red")
        canvas.create_text(500, 395, text="Please enter a username ", font="Ariel 14 bold")
    elif not name.isalpha():
        canvas.create_rectangle(350,330,650,430, fill="white", outline="black")
        canvas.create_text(500, 350, text="Sorry!", font="Ariel 18 bold", fill="red")
        canvas.create_text(500, 395, text="Please only enter letters (a-z)", font="Ariel 14 bold")
    elif length < 2 or length > 12:
        canvas.create_rectangle(350,330,650,430, fill="white", outline="black")
        canvas.create_text(500, 350, text="Sorry!", font="Ariel 18 bold", fill="red")
        canvas.create_text(500, 385, text="Your username needs to", font="Ariel 14 bold")
        canvas.create_text(500, 405, text="be between 2-12 characters.", font="Ariel 14 bold")#Do a value error, error catch
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
            canvas.create_text(500,450, text="Sorry!", font="Ariel 18 bold", fill="red")
            canvas.create_text(500, 485, text="You cannot have a number under 0.", font="Ariel 14 bold")
        elif int(roundguess) > 999:
            canvas.create_rectangle(325,435,675,525, fill="white", outline="black")
            canvas.create_text(500,450, text="Sorry!", font="Ariel 18 bold", fill="red")
            canvas.create_text(500, 485, text="You cannot have a number over 999.", font="Ariel 14 bold")
        else:
            Game.nextround()
    except ValueError:
        canvas.create_rectangle(325,435,675,525, fill="white", outline="black")
        canvas.create_text(500,450, text="Sorry!", font="Ariel 18 bold", fill="red")
        canvas.create_text(500, 485, text="You need to input an interger.", font="Ariel 14 bold")

#Number picking definition (picks a 4 random numbers appended to a list to be used in each gamemode/level)
def numberpicker():
    global list_picked1, list_picked2, list_picked3, strAccept, user_picked, intRun
    user_picked = []
    list_picked1 = []
    list_picked2 = []
    list_picked3 = []
    strAccept = "False"
    x = 0
    z = 0
    intRun = 0
    #Addition mode
    if intGamemode == 1:
        if intLevel == 1:#Level 1
            while intRun < 4:
                choice = random.randint(1, 6)
                list_picked2.append(choice)
                choice2 = random.randint(1, 4)
                list_picked3.append(choice2)
                choice = 0
                choice2 = 0
                add_finish()
                intRun += 1

        elif intLevel == 2:#Level 2
            while intRun < 4:
                choice = random.randint(11, 30)
                list_picked2.append(choice)
                choice2 = random.randint(10, 25)
                list_picked3.append(choice2)
                choice = 0
                choice2 = 0
                add_finish()
                intRun += 1

        elif intLevel == 3:#Level 3
            while intRun < 4:
                choice = random.randint(60, 170)
                list_picked2.append(choice)
                choice2 = random.randint(40, 130)
                list_picked3.append(choice2)
                choice = 0
                choice2 = 0
                add_finish()
                intRun += 1
                
    #Subtraction mode
    elif intGamemode == 2:
        if intLevel == 1:#Level 1
            while intRun < 4:
                choice = random.randint(3, 8)
                list_picked3.append(choice)
                choice2 = random.randint(1, choice)
                list_picked1.append(choice2)
                choice = 0
                choice = 0
                sub_finish()
                intRun += 1

        elif intLevel == 2:#Level 2
            while intRun < 4:
                choice = random.randint(18, 34)
                list_picked3.append(choice)
                choice2 = random.randint(5, choice)
                list_picked1.append(choice2)
                choice = 0
                choice = 0
                sub_finish()
                intRun += 1

        elif intLevel == 3:#Level 3
            while intRun < 4:
                choice = random.randint(70, 150)
                list_picked3.append(choice)
                choice2 = random.randint(20, choice)
                list_picked1.append(choice2)
                choice = 0
                choice = 0
                sub_finish()
                intRun += 1
                
    #Multiplication mode
    elif intGamemode == 3:
        if intLevel == 1:#Level 1
            while intRun < 4:
                choice = random.randint(1, 5)
                list_picked2.append(choice)
                choice = 0
                choice2 = random.randint(1, 4)
                list_picked3.append(choice2)
                choice2 = 0
                mul_finish()
                intRun += 1
 
        elif intLevel == 2:#Level 2
            while intRun < 4:
                choice = random.randint(4, 12)
                list_picked2.append(choice)
                choice = 0
                choice2 = random.randint(3, 11)
                list_picked3.append(choice2)
                choice2 = 0
                mul_finish()
                intRun += 1

        elif intLevel == 3:#Level 3
            while intRun < 4:
                choice = random.randint(10, 30)
                list_picked2.append(choice)
                choice = 0
                choice2 = random.randint(11, 30)
                list_picked3.append(choice2)
                choice2 = 0
                mul_finish()
                intRun += 1
                
    #Division mode    
    elif intGamemode == 4:
        if intLevel == 1:#Level 1
            while intRun < 4:
                choice = random.randint(1, 5)
                list_picked1.append(choice)
                choice2 = random.randint(1, 6)
                list_picked3.append(choice2)
                choice = 0
                choice2 = 0
                div_finish()
                intRun += 1
                
        elif intLevel == 2:#Level 2
            while intRun < 4:
                choice = random.randint(2, 9)
                list_picked1.append(choice)
                choice2 = random.randint(4, 12)
                list_picked3.append(choice2)
                choice = 0
                choice2 = 0
                div_finish()
                intRun += 1

        elif intLevel == 3:#Level 3
            while intRun < 4:
                choice = random.randint(6, 25)
                list_picked1.append(choice)
                choice2 = random.randint(7, 35)
                list_picked3.append(choice2)
                choice = 0
                choice2 = 0
                div_finish()
                intRun += 1

#These defs (_finish) will find the answer of equation by using numbers generated      
def add_finish():
    choice = list_picked2[intRun] + list_picked3[intRun]
    list_picked1.append(choice)
    choice = 0

def sub_finish():
    choice = list_picked1[intRun] + list_picked3[intRun]
    list_picked2.append(choice)
    choice = 0

def mul_finish():
    choice = list_picked3[intRun] * list_picked2[intRun]
    list_picked1.append(choice)
    choice = 0

def div_finish():
    choice = list_picked1[intRun] * list_picked3[intRun]
    list_picked2.append(choice)
    choice = 0

#Runs the program
Open_window()
