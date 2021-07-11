
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
def read_text_outloud(text_to_read, print_message, text_to_write = False):
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
print("\n\n\n\t\t\t The Mathematical Tutor Program\n")
dual_output ="Welcome To The Mathematical Tutor Program, We Are Going To Help You Do Your Math Equations"
read_text_outloud(dual_output, True)
dual_output ="I Am Your Math Tutor Chatbot And I Am Here To Help You Learn Mathematics."
read_text_outloud(dual_output, True)
dual_output ="Choose From The Menu Below To Start Your Program And Follow The Instructions"
read_text_outloud(dual_output, True)
dual_output = "In This Menu You Will Choose A Number For Addition, Subtraction, Multiplication, Or Division."
read_text_outloud(dual_output, True)
dual_output = "Then You Will Be Given The List Again For Another Try Or You May Choose To Quit."
read_text_outloud(dual_output, True)
# Here we declare global variables
program_over = True    # sets the main loop to run

# Here we will define our classes and functions
class MainMenu:
    def please_retry():
        dual_output = "Please Choose From The Menu Options Below To Try Again"
        read_text_outloud(dual_output, True)
        press = TheBrain.start() 

    def intro():
        press = TheBrain.start() 

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
    dual_output = "1. Addition" 
    read_text_outloud(dual_output, True)
    dual_output = "2. Subtraction"
    read_text_outloud(dual_output, True)
    dual_output = "3. Multiplication"
    read_text_outloud(dual_output, True)
    dual_output = "4. Division"
    read_text_outloud(dual_output, True)
    dual_output = "5. Vocalized Calculator"
    read_text_outloud(dual_output, True)
    dual_output = "6. Quit"
    read_text_outloud(dual_output, True)
    #dual_output = "\t\t\n Please Enter The Number You Would Like To Try From The Subject List"
    choice = input ("\t\t\n Please Enter The Number You Would Like To Try From The Subject List: ") # this get input from the user
    
    #if choice 6 user input our program runs the below code for choosing number 6  and exits
    if choice in ["6"]:
        try:
            dual_output = "Thank You For Using Our Mathematical Tutor Chat Bot Tutor Program It Has Been A Pleasure."
            read_text_outloud(dual_output, True)
            program_over = False # Quit the program
            quit()
            
        #except ValueError to exclude accudental errors and loops
        except ValueError: # Break if the user did not enter an integer
            MainMenu.please_retry()

        # Press ctrl-c or ctrl-d on the keyboard to exit
        #except to exclude accudental errors and exits if called or typed
        except(KeyboardInterrupt, EOFError, SystemExit):
            quit()

    #if choice 5 user input our program runs the below code for choosing number 5 and loops
    if choice in ["5"]:
        try:
            dual_output = "You Have Chosen To Try Out The Vocalized Calculator For Your Math."
            read_text_outloud(dual_output, True)
            program_over = False # Quit the program
            import speech_recognition as s_r
            try:
                print("Your speech_recognition version is: "+s_r.__version__)
                r = s_r.Recognizer()
                my_mic_device = s_r.Microphone(device_index=1)
                with my_mic_device as source:
                    # print(len(my_mic_device))
                    dual_output = "Please Say What You Would Like To Calculate Only Speak Like The Example, For Example Say 3 plus 3"
                    read_text_outloud(dual_output, True)
                    r.adjust_for_ambient_noise(source, duration = 1)
                    audio = r.listen(source)
                my_string = r.recognize_google(audio)
                if  my_string  == "":
                    my_string = "I Did Not Hear You Vocally Respond To The Voice Activated Calculator "
                print(my_string)
            except s_r.UnknownValueError as e:
                dual_output = "I Will Show You The Menu Again For Another Try, Here Goes"
                
            import operator
            def get_operator_fn(op):
                return {
                    '+' : operator.add,
                    '-' : operator.sub,
                    'x' : operator.mul,
                    'divided' :operator.__truediv__,
                    'Mod' : operator.mod,
                    'mod' : operator.mod,
                    '^' : operator.xor,
                    }[op]
            def eval_binary_expr(op1, oper, op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
                
            try:
                print(eval_binary_expr(*(my_string.split())))
            except:
                print("Invalid Input ")
                
        #except ValueError to exclude accudental errors and loops
        except ValueError: # Break if the user did not enter an integer
            MainMenu.intro()

        # Press ctrl-c or ctrl-d on the keyboard to exit
        #except to exclude accudental errors and exits if called or typed
        except(KeyboardInterrupt, EOFError, SystemExit):
            quit()
    
    #if choice 1, 2, 3, 4,  user input our program runs the below code for choosing number 1, 2, 3, 4, and loops
    if choice in  ["1", "2", "3", "4"]: # If the users input is one of the options we provide
        try: # Try running this block of code
            prompt_user = Arithmetic.PromptUser()
            firstNumber = prompt_user['a']
            secondNumber = prompt_user['b'] 
            
            #if choice 1 user input our program runs the below code for choosing number 1 runs only addition/ sub function in class TheBrain (choice) and loops
            if choice == "1":
                TheBrain.addInput(firstNumber, secondNumber) # This is where the Addition Class will go
            #elif choice 2 user input our program runs the below code for choosing number 2 runs only addition/ sub function in class TheBrain (choice) and loops
            elif choice == "2":
                TheBrain.subtractInput(firstNumber, secondNumber) # This is where the Subtraction Class will go
            
            #elif choice 2 user input our program runs the below code for choosing number 2 runs only addition/ sub function in class TheBrain (choice) and loops
            elif choice == "3":
                TheBrain.multiplyInput(firstNumber, secondNumber) # This is where the Multiplication Class will go
            
            #elif choice 2 user input our program runs the below code for choosing number 2 runs only addition/ sub function in class TheBrain (choice) and loops
            elif choice == "4":
                TheBrain.divideInput(firstNumber, secondNumber)
        

            #except ValueError to exclude accudental errors and loops
        except ValueError: # Break if the user did not enter an integer
            MainMenu.please_retry()

        # Press ctrl-c or ctrl-d on the keyboard to exit
        #except to exclude accudental errors and exits if called or typed
        except(KeyboardInterrupt, EOFError, SystemExit):
            quit()
    else: # Restart the program
            MainMenu.please_retry()
        # Please note I gave each Class a .start() function that will initiate that class into doing some work
    #while loop program over for the entire games functionality that is performing the loop
while program_over:
    game = MainMenu.intro()
    

