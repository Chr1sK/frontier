from inspect import isroutine
import os
import re

placed = True
x = 0
y = 0
heading = ""


def move():
    return "Success"

def right():
    return "Success"

def left():
    return "Success"

def report():
    return '{}, {}, {}'.format(x,y,heading)

def place(x, y, newHeading):
    if x is None or y is None or newHeading is None:
        return "Not valid place command"
    return "Success"

def mainFunction():
    while True:
        command = input("Enter Command: ")
        os.system("clear")
        if "place" not in command and placed is False:
            print ("Issue valid place command first")
        elif command == "move()":
            print(move())
        elif command == "left()":
            print(left())
        elif command == "right()":
            print(right())
        elif command == "report()":
            print(report())
        elif "place" in command:
            pattern = re.search("^[place(]{1}[,]{2}[)]{1}$", command)
            print(bool(pattern))
            if pattern:
                try:
                    argumentsString = command[command.index("(") + 1:-1].split(',')
                except:
                    print("Invalid place() command")
                print(argumentsString)
                try: print(eval(command))
                except Exception as e:
                    print("error: " + e)
            else:
                print("Not valid place command")
            
            
        else:
            print("Not valid function, please try again")
        
if __name__ == "__main__":
    mainFunction()



