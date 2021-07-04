#CSC318 Team ChatBot

# Heidi - Jeffrey - Deloris - & - Geri - UAT Summer 2021
#-----------------------------------------------------------------Demo Example Sprint01----------------------------------------------------------
#chatbot GUIDE From Professor Tony Hintons Class AI
import pyttsx3
# Class Project - sprint01 - Base Code Design - 06/17/2021
# Here we put the import files
from Arithmetic import Arithmetic
#from Multiplication import Multiplication
import random
#function to read text to speech
def read_text_outloud(text_to_read, print_message = False):
    # initialize the converter
    converter = pyttsx3.init()
    converter.setProperty('rate',130)
    converter.setProperty('volume',0.7)

    if print_message:
        print(text_to_read)
        converter.say(text_to_read)
    else:
        converter.say(text_to_read)

    converter.runAndWait()
    
dual_output ="Welcome To The Mathematical Tutor Program, We Are Going To Show You Some Math Equasions"
read_text_outloud(dual_output, True)

# Here we declare global variables
program_over = True    # sets the main loop to run

# Here we will define our classes and functions
class MainMenu:  # This is the main menu
    
    def please_retry():
        print ("I am sorry can you please try again.")
        dual_output = "I am sorry can you please try again."
        read_text_outloud(dual_output)

    def intro():
        dual_output ="Please Choose From The Following Options:"
        read_text_outloud(dual_output, True)
        dual_output =" 1. Directions"
        read_text_outloud(dual_output, True)
        dual_output =" 2. Start Program"
        read_text_outloud(dual_output, True)
        dual_output =" 3. Quit"
        read_text_outloud(dual_output, True)
        dual_output = "What do you choose to do? "
        read_text_outloud(dual_output)
        choice = input("\n What do you choose to do? ")

        if choice == "1":
            MainMenu.directions() # If user chooses 1 then go to MainMenu.directions()
        elif choice == "2":
            TheBrain.start() # If user chooses 2 then go to TheBrain.start() and start the game
        elif choice == "3":
            dual_output = "You Have Chosen To Quit, See You Next Time"
            read_text_outloud(dual_output, True)
            program_over = False # If user chooses 3 then quit the program
            quit()
        else:
            MainMenu.please_retry()
            dual_output = "\n Please press Enter to continue."
            read_text_outloud(dual_output)
            input("\n Please press Enter to continue.")

    def directions(): # The directions function
        dual_output ="Greetings I am your mathematical tutor."
        print(dual_output)
        read_text_outloud(dual_output)
        dual_output ="I am here to help you learn math."
        print(dual_output)
        read_text_outloud(dual_output)
        dual_output ="You can choose to do addition, subtraction, multiplication, or division."
        print(dual_output)
        read_text_outloud(dual_output)
        dual_output ="If you solve the problem correctly you will earn score points."
        print(dual_output)
        read_text_outloud(dual_output)
        dual_output ="If you do not answer correctly, you will not get any score points."
        print(dual_output)
        read_text_outloud(dual_output)
        dual_output = "Please press Enter to continue."
        read_text_outloud(dual_output)
        press = input("\n Please press Enter to continue.")

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
    dual_output = "You may choose from the following tutorial programs."
    read_text_outloud(dual_output, True)
    
    dual_output = "1. Addition" 
    read_text_outloud(dual_output, True)
    dual_output = "2. Subtraction"
    read_text_outloud(dual_output, True)
    dual_output = "3. Multiplication"
    read_text_outloud(dual_output, True)
    dual_output = "4. Division"
    read_text_outloud(dual_output, True)
    dual_output = "5 Quit"
    read_text_outloud(dual_output, True)
    dual_output = "What is your choice"
    read_text_outloud(dual_output)
    choice = input ("\nWhat is your choice: ") # this get input from the user
   
    if choice in  ["1", "2", "3", "4", "5"]: # If the users input is one of the options we provide
        try: # Try running this block of code
            prompt_user = Arithmetic.PromptUser()
            firstNumber = prompt_user['a']
            secondNumber = prompt_user['b'] 
    
            if choice == "1":
                TheBrain.addInput(firstNumber, secondNumber) # This is where the Addition Class will go
            elif choice == "2":
                TheBrain.subtractInput(firstNumber, secondNumber) # This is where the Subtraction Class will go
            elif choice == "3":
                TheBrain.multiplyInput(firstNumber, secondNumber) # This is where the Multiplication Class will go
            elif choice == "4":
                TheBrain.divideInput(firstNumber, secondNumber)
        
            elif choice == "5":
                print("Thank you for playing! Goodbye.")
                dual_output = "Thank you for playing! Goodbye."
                read_text_outloud(dual_output)
                program_over = False # Quit the program
                quit()
            
        except ValueError: # Break if the user did not enter an integer
            MainMenu.please_retry()
            TheBrain.start()

        # Press ctrl-c or ctrl-d on the keyboard to exit
        except(KeyboardInterrupt, EOFError, SystemExit):
            quit()
    else: # Restart the program
        MainMenu.please_retry()
        TheBrain.start()

while program_over:
    game = MainMenu.intro()