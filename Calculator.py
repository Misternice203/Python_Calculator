
class Calculator:
    def __init__(self):
        self.operations = Operations()

    def add(self, a, b):
        return self.operations.add(a, b)
    
    def subtract(self, a, b):
        return self.operations.subtract(a, b)
    
    def multiply(self, a, b):
        return self.operations.multiply(a, b)
    
    def divide(self, a, b):
        return self.operations.divide(a, b)



class Operations:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        else:
            return a / b
        

class Menu:
    def display(self):
        print("\n-----Calculator-----\n")
        print('''
            1. Add
            2. Subtract
            3. Multiply
            4. Divide
            5. Exit
        ''')

    def get_choice(self):
        return input("Please select a option from the menu: ")
    
    def get_numbers(self):
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        return a, b
    
class App:
    def __init__(self):
        self.calculator = Calculator()
        self.menu = Menu()

    def run(self):
        while True:
            self.menu.display()
            choice = self.menu.get_choice()

            if choice == "5":
                print("You selected to end the program! Have A Great Day!")
                break

            a, b = self.menu.get_numbers()

            if choice == "1":
                print(self.calculator.add(a, b))

            elif choice == "2":
                print(self.calculator.subtract(a, b))

            elif choice == "3":
                print(self.calculator.multiply(a, b))

            elif choice == "4":
                print(self.calculator.divide(a, b))

            else:
                print("Invalid choice. Please enter a option from menu.")

App().run()
