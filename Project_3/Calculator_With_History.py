HISTORY_FILE = "history.txt"

def show_history():
    file = open(HISTORY_FILE,"r")
    lines = file.readlines()
    if lines == 0:
        print("No History Found!")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def history_clear():
    file = open(HISTORY_FILE,"w")
    file.close()
    print("History Cleared.")

def save_to_history(equation, result):
    file = open(HISTORY_FILE,"a")
    file.write(equation + "=" + str(result) + "\n")
    file.close()

def calculate(user_input):
    equation = user_input.strip()
    
    try:
        result = eval(equation) # eval() is a Python built-in function that takes a string and executes it as Python code. 
                                # It's like having Python's calculator built inside Python itself!
        
        if isinstance(result, float) and result == int(result):
            result = int(result)
        
        print("Result:", result)
        save_to_history(equation, result)
    
    except ZeroDivisionError:
        print("Error: Cannot divide by Zero!")
    except:
        print("Error: Invalid input!")

def main():
    print("ADVANCED CALCULATOR WITH HISTORY")
    print("\nSupported Operations:")
    print("  +   : Addition")
    print("  -   : Subtraction")
    print("  *   : Multiplication")
    print("  /   : Division")
    print("  %   : Modulus (remainder)")
    print("  **  : Exponential (power)")
    print("\nSupported Commands:")
    print("  history : View calculation history")
    print("  clear   : Clear history")
    print("  exit    : Exit calculator")
    print("\nNote: You can solve multi-input equations!")
    print("Example: 5 + 3 * 2, 10 % 3, 2 ** 8, (5 + 3) * 2")
    
    while True:
        user_input = input("\nInput Calculation (or command): ").strip()
        
        if user_input == "exit":
            print("Have a Nice Day!")
            break
        elif user_input == "history":
            print("\n--- CALCULATION HISTORY ---")
            show_history()
        elif user_input == "clear":
            history_clear()
        elif user_input == "":
            print("Please enter a valid input!")
        else:
            calculate(user_input)

main()