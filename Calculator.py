class Menu:
    options = []
    pickedOption = 0
    def __init__(self, pickedOption, options): #konstrukto klasy
        self.pickedOption = pickedOption
        self.options = options
    def showoptions(self):
        for o in self.options:
            print(o)
    def pickOption(self):
        self.pickedOption = int(input())
    
class Calculator:
    optionA = 0
    optionB = 0
    result = 0
    def assigneOptionA(self):
        print("pick Option A")
        self.optionA = int(input())
        
    def assigneOptionB(self):
        print("pick option B")
        self.optionB = int(input())
    def add(self):
        self.result = self.optionA + self.optionB
    def subtract(self):
        self.result = self.optionA - self.optionB
    def multiply(self):
        self.result = self.optionA * self.optionB
    def divide(self):
        if self.optionB == 0: 
            print("second value must be diferent than 0")
            self.optionB = int(input())
            self.divide() #recursion

        self.result = self.optionA / self.optionB
    def showResult(self):
        print("result")
        print(self.result)

def runAplication():
    menu = Menu(0, ["1. add", "2. subtract", "3. multiply", "4. divide"])
    menu.showoptions()
    menu.pickOption()
    calculator = Calculator()
    calculator.assigneOptionA()
    calculator.assigneOptionB()
    if menu.pickedOption == 1:
        calculator.add()
    
    if menu.pickedOption == 2:
        calculator.subtract()

    if menu.pickedOption == 3:
        calculator.multiply()

    if menu.pickedOption == 4:
        calculator.divide()
    
    calculator.showResult()
    runAplication()

runAplication()    

    
       


    





