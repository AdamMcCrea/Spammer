import time
import random
import pyautogui

x = 0
useNames = False
adamInMessage = True
count = input("How many times would you like to spam?\n")

choice = input("Would you like to use names? ('Y' for yes, 'N' for no, 'exit' to exit)\n")

def read_random_line(filename):
    with open(filename, "r") as f:
        random_line = random.randint(0, 2943)
        f.seek(random_line)
        f.readline()
        return_line = f.readline()
        f.close()
        return return_line

if choice.lower() == "y":
    f = open("names.txt")
    while adamInMessage ==True:
        message = input("Enter message to spam, the names will appear at the end of the message:\n")
        if("adam" in message.lower()):
            print("NO, you can't use my own spammer against me bozo, try again\n")
        else:
            adamInMessage = False
    
    print("You have 10 seconds to place your cursor where you want to spam!")
    time.sleep(10)
    for i in range(int(count)):
        newMessage = message + read_random_line("names.txt")
        pyautogui.typewrite(newMessage)
        pyautogui.press("enter")

elif choice.lower() == "n":
    while adamInMessage ==True:
        message = input("Enter message to spam:\n")
        if("adam" in message.lower()):
            print("NO, you can't use my own spammer against me bozo, try again\n")
        else:
            adamInMessage = False
            
    print("You have 10 seconds to place your cursor where you want to spam!")
    time.sleep(10)
    for i in range(int(count)):
        pyautogui.typewrite(message)
        pyautogui.press("enter")
        


        



