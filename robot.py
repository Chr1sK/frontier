import os
import re

#INITIALISATION
placed = False
x = 0
y = 0
heading = ''
directions = ['NORTH', 'EAST', 'SOUTH', 'WEST']

#FUNCTIONS
def move():
    global x,y,heading
    match(str(heading)):
        case 'NORTH':
            if x < 4:
                x+=1
            else: return 'X out of bounds'
        case 'EAST':
            if y < 4:
                y+=1
            else:
                return 'Y out of bounds'
        case 'SOUTH':
            if x > 0:
                x-=1
            else:
                return 'X out of bounds'
        case 'WEST':
            if y > 0:
                y-=1
            else:
                return 'Y out of bounds'
    return "Success"

def right():
    global heading
    heading = directions[directions.index(heading) + 1] if directions.index(heading) < 3 else directions[0]
    return "Success"

def left():
    global heading
    heading = directions[directions.index(heading) - 1] if directions.index(heading) > 0 else directions[3]
    return "Success"

def report():
    global x, y, heading
    return '{}, {}, {}'.format(x,y,heading)

def place(newX, newY, newHeading):
    try:
        newX = int(newX)
        newY = int(newY)
        newHeading = str(newHeading[1:-1])
    except:
        return "Not valid place command arguments"
    
    if (newX < 0 or newX > 4) or (newY < 0 or newY > 4) or (newHeading not in directions): #basic validations for out of bounds or invalid heading
        return "Not valid place command arguments"
    global x, y, heading, placed
    x = newX
    y = newY
    heading = newHeading
    placed = True
    return "Success"
#END OF FUNCTIONS

#MAIN FUNCTION
def mainFunction():
    os.system("clear")
    while True:
        command = input("Enter Command: ")
        if "place" not in command and placed is False: #check if first command is place
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
            pattern = re.search("[^place(]{1}[)]{1}$", command)
            if pattern:
                try:
                    argumentsString = command[command.index("(") + 1:-1].split(',') #basic validations around place command arguments and syntax
                    print(place(argumentsString[0], argumentsString[1], argumentsString[2]))
                except:
                    print("Not valid place command")
            else:
                print("Not valid place command")
        else:
            print("Not valid function, please try again")
        
#CALL MAIN FUNCTION
if __name__ == "__main__":
    mainFunction()



