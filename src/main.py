class Add:
    """Adds two numbers"""

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def do(self):
        return self.num1 + self.num2


class Subtract:
    """Subtracts two numbers"""

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def do(self):
        return self.num1 - self.num2


class Multiplication:
    """Multiplies two numbers"""

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def do(self):
        return self.num1 * self.num2


class Division:
    """Divides two numbers"""

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def do(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            return "Cannot divide by zero!"


def main():
    while True:
        print("---Welcome to Calculator---")
        print("1. Add two numbers")
        print("2. Subtract two numbers")
        print("3. Multiply two numbers")
        print("4. Divide two numbers")
        print("5. Quit")
        x = int(input("Enter your choice number: "))
        print("--------------------------")

        first_num, second_num = None, None

        if x in [1, 2, 3, 4]:
            while True:
                try:
                    first_num = int(input("Enter first number: "))
                except ValueError:
                    print("Invalid input, please enter a number!")
                    continue
                else:
                    break

            while True:
                try:
                    second_num = int(input("Enter second number: "))
                except ValueError:
                    print("Invalid input, please enter a number!")
                    continue
                else:
                    break

            if x == 1:
                ins = Add(first_num, second_num)
                result = ins.do()
                print(f"Result: {result}")

            elif x == 2:
                ins = Subtract(first_num, second_num)
                result = ins.do()
                print(f"Result: {result}")

            elif x == 3:
                ins = Multiplication(first_num, second_num)
                result = ins.do()
                print(f"Result: {result}")

            elif x == 4:
                ins = Division(first_num, second_num)
                result = ins.do()
                print(f"Result: {result}")


        elif x == 5:
            print("Thank you for using calculator! Goodbye!")
            break

        else:
            print("Invalid choice!")



if __name__ == "__main__":
    main()