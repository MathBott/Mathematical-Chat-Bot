#chatbot GUIDE From Professor Tony Hintons Class AI
import pyttsx3

#python program to subtract two numbers using function
class Arithmetic(object):
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def PrintArthimeticMessage(self):
        Arithmetic.read_text_outloud(f"The answer for {self.operation_name} is: {self.a} {self.operation_to_speak} {self.b} = {self.total}\n\n")
        print(f"\n\n{self.operation_name} is: {self.a} {self.operation} {self.b} = {self.total}\n\n")#call the function
    
    def read_text_outloud(text_to_read, print_message = False):# initialize the converter
        converter = pyttsx3.init()
        converter.setProperty('rate',130)
        converter.setProperty('volume',0.7)

        if print_message:
            print(text_to_read)
            converter.say(text_to_read)
        else:
            converter.say(text_to_read)

        converter.runAndWait()
        
    def PromptUser():
        d = dict()
        dual_output = "Please enter the first number you want to use"
        Arithmetic.read_text_outloud(dual_output)
        d['a'] = int(input("Please enter the first number you want to use: "))
        dual_output = "Please enter the second number you want to use"
        Arithmetic.read_text_outloud(dual_output)
        d['b'] = int(input("Please enter the second number you want to use: "))
        return d
        
    # Declaring the method 
    def add(self):
        # Returning the value of both intergers 
        self.total = self.a + self.b
        self.operation_name = "Addition"
        self.operation_to_speak = "plus"
        # Call the PrintMessage method
        self.PrintArthimeticMessage()
        
    #Declaring the Method 
    def multiplication(self):
        #Returning the value of both integers
        self.total = self.a * self.b 
        self.operation_name = "Multiplication"
        self.operation_to_speak = "times"
        # Call the PrintMessage method
        self.PrintArthimeticMessage()

    # Handles dividing  the numbers
    def divide(self): 
        # Total is an instance variable that is set to the first number divided by the second
        self.total = self.a / self.b
        self.operation_name = "Division"
        self.operation_to_speak = "divided by"

        # Call the PrintMessage method
        self.PrintArthimeticMessage()
        
    def subtraction(self):  #function definifion for subtraction
        self.total = self.a - self.b
        self.operation_name = "Subtraction"
        self.operation_to_speak = "minus"

        self.PrintArthimeticMessage()
