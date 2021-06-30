#CSC318 Team ChatBot

# Heidi - Jeffrey - Deloris - & - Geri - UAT Summer 2021
#-----------------------------------------------------------------Demo Example----------------------------------------------------------

import pyttsx3
# Class Project - sprint01 - Base Code Design - 06/17/2021
# Here we put the import files
from Arithmetic import Arithmetic
#from Multiplication import Multiplication
import random
#function to read text to speech chatbot From Professor Tony Hintons Class AI @ UAT
def read_text_outloud(text_to_read, print_message = False):
    # initialize the converter
    converter = pyttsx3.init()
    converter.setProperty('rate',140)
    converter.setProperty('volume',0.7)

    if print_message:
        print(text_to_read)
        converter.say(text_to_read)
    else:
        converter.say(text_to_read)

    converter.runAndWait()



# Here we declare global variables
program_over = True    # sets the main loop to run
#End Of function to read text to speech chatbot From Professor Tony Hintons Class AI @ UAT
print("\n\n\n\t\t\t\t\t\n The Mathematical Tutor Program")

dual_output ="\t\t\n Welcome To The Mathematical Tutor Program"
read_text_outloud(dual_output, True)
dual_output ="\t\t\n Choose From The Menu Below To Start Your Program And Follow The Instructions"
read_text_outloud(dual_output, True)
# Here we will define our classes and functions
class MainMenu:  # This is the main menu

    def intro():
        dual_output ="\t\t\n In This Menu You Will Be Given A Number Of Options."
        read_text_outloud(dual_output, True)
        dual_output ="\t\t\n I Am Your Math Tutor Chatbot And I Am Here To Help You Learn."
        read_text_outloud(dual_output, True)
        dual_output ="\t\t\n Please Choose What You Would Like To Do Next: "
        read_text_outloud(dual_output, True)
        dual_output ="\t\t\n 1. Directions"
        read_text_outloud(dual_output, True)
        dual_output ="\t\t\n 2. Start Program"
        read_text_outloud(dual_output, True)
        dual_output ="\t\t\n 3. Quit"
        read_text_outloud(dual_output, True)
        dual_output = "\t\t\n What do you choose to do? "
        read_text_outloud(dual_output)
        choice = input("\t\t\n\n What do you choose to do? ")

        if choice == "1":
            MainMenu.directions() # If user chooses 1 then go to MainMenu.directions()
        elif choice == "2":
            play = TheBrain.start() # If user chooses 2 then go to TheBrain.start() and start the game
        elif choice == "3":
            dual_output = "You Have Chosen To Quit, See You Next Time"
            read_text_outloud(dual_output)
            print("You Have Chosen To Quit, chat With You Next Time")
            program_over = False # If user chooses 3 then quit the program
            quit()
            
        else:
            dual_output = "\t\t\n Please try again."
            read_text_outloud(dual_output)
            print("\t\t\n Please try again.") # If choice is not in the list, try again (exception handeling)
            dual_output = "\n Please press Enter to continue."
            read_text_outloud(dual_output)
            press = input("\n Please press Enter to continue.")   

    def directions(): # The directions function
        dual_output ="\t\t\n Greetings I am your mathematical tutor."
        print(dual_output)
        read_text_outloud(dual_output)
        dual_output ="\t\t\n I am here to help you learn math."
        print(dual_output)
        read_text_outloud(dual_output)
        dual_output ="\t\t\n You can choose to do addition, subtraction, multiplication, or division."
        print(dual_output)
        read_text_outloud(dual_output)
        dual_output = "\t\t\n Please press Enter to continue."
        read_text_outloud(dual_output)
        press = input("\t\t\n\n Please press Enter to continue.")

class TheBrain:   # This class will be the main intelligence of the program.
   def divideInput(firstNumber, secondNumber):
       Arithmetic(firstNumber, secondNumber, "/").divide()
    
   def addInput(firstNumber, secondNumber):
       Arithmetic(firstNumber, secondNumber, "+").add()
    
   def subtractInput(firstNumber, secondNumber):
       Arithmetic(firstNumber, secondNumber, "-").subtraction()

   def multiplyInput(firstNumber, secondNumber):
       Arithmetic(firstNumber, secondNumber, "*").multiplication()

   def start(): # This function is the main function that will give the user choices on what type of problems to solve
    
    dual_output = "\t\t\n I have several options for you to learn from."
    read_text_outloud(dual_output, True)
    dual_output = "\t\t\n You may choose from the following tutorial programs."
    read_text_outloud(dual_output, True)
    
    dual_output = "\t\t\n 1. Addition" 
    read_text_outloud(dual_output, True)
    dual_output = "\t\t\n 2. Subtraction"
    read_text_outloud(dual_output, True)
    dual_output = "\t\t\n 3. Multiplication"
    read_text_outloud(dual_output, True)
    dual_output = "\t\t\n 4. Division"
    read_text_outloud(dual_output, True)
    dual_output = "\t\t\n 5 Quit"
    read_text_outloud(dual_output, True)
    dual_output = "\t\t\n What is your choice"
    read_text_outloud(dual_output)
    choice = input ("\t\t\n\n What is your choice: ") # this get input from the user
    
    dual_output = "\t\t\n Please enter the first number you want to use"
    read_text_outloud(dual_output)
    firstNumber = int(input("\t\t\n Please enter the first number you want to use: "))
    dual_output = "\t\t\n Please enter the second number you want to use"
    read_text_outloud(dual_output)
    secondNumber = int(input("\t\t\n Please enter the second number you want to use: "))

    if choice == "1":
        TheBrain.addInput(firstNumber, secondNumber) # This is where the Addition Class will go
    elif choice == "2":
        TheBrain.subtractInput(firstNumber, secondNumber) # This is where the Subtraction Class will go
    elif choice == "3":
        TheBrain.multiplyInput(firstNumber, secondNumber) # This is where the Multiplication Class will go
    elif choice == "4":
        TheBrain.divideInput(firstNumber, secondNumber)
        
    elif choice == "5":
        print("\t\t\n Thank you for playing! Goodbye.")
        dual_output = "\t\t\n Thank you for playing! Goodbye."
        read_text_outloud(dual_output)
        program_over = False # Quit the program
        quit()
    else:
        print ("\t\t\n I am sorry can you please try again.")
        dual_output = "\t\t\n I am sorry can you please try again."
        read_text_outloud(dual_output)
        press = input("\t\t\n Please press Enter to continue")
        dual_output = "\t\t\n Please press Enter to continue"
        read_text_outloud(dual_output)
        play = TheBrain.start()

        # Please note I gave each Class a .start() function that will initiate that class into doing some work

while program_over:
    game = MainMenu.intro()

