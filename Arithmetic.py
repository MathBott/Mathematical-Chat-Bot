#python program to subtract two numbers using function
class Arithmetic(object):
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation
        
    def subtraction(self):  #function definifion for subtraction
        self.total = self.a - self.b
        self.operation_name = "Subtraction"
        self.PrintArithmeticMessage()

    def PrintArithmeticMessage(self):
        print(f"\n\n{self.operation_name} is: {self.a} {self.operation} {self.b} = {self.total}\n\n")#call the function
    # #Class Project MathBot
    
        # Handles dividing  the numbers
    def divide(self): 
        # Total is an instance variable that is set to the first number divided by the second
        self.total = self.a / self.b
        self.operation_name = "Division"
        # Call the PrintMessage method
        self.PrintArithmeticMessage()
        
    # Declaring the method 
    def add(self):
        # Returning the value of both intergers 
        self.total = self.a + self.b
        self.operation_name = "Addition"
        # Call the PrintMessage method
        self.PrintArithmeticMessage()
        
    #Declaring the Method 
    def multiplication(self):
        #Returning the value of both integers
        self.total = self.a * self.b 
        self.operation_name = "Multiplication"
        # Call the PrintMessage method
        self.PrintArithmeticMessage()
    
# #Class For Arithmetic.
# #Being able to add two or more intergers together.
# class Arithmetic:

# #Letting the user put in input to Add two intergers
# a=int(input("Enter First Number: ")) 
# b=int(input("Enter Second Number: "))

# #Creating an object for Addition
# obj = Addition(a, b) 
# #Prints the Answer to the user
# print("Result: ",obj.add()) 

# #Letting the user put in input to Multiply two intergers
# a=int(input("Enter First Number: ")) 
# b=int(input("Enter Second Number: "))
# #Creating an object for Multiplication
# obj =  Multiplication(a,b)
# #Prints the Answer to the user
# print("Result: ",obj.multiply()) 