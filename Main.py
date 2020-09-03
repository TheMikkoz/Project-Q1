import psutil, os

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def user(userInput):
    global run
    if userInput == "quit":
        run = False
        
    if userInput == "cpu":
        clear()
        print("- - - - \nCPU usage: " + str(psutil.cpu_percent()) + " %\nCPU threads: "+ str(psutil.cpu_count()) +"\nCPU cores: "+str(psutil.cpu_count(logical=False))+"\n- - - -")
        userInput = input(": ")
        user(userInput)

    if userInput == "ram":
        clear()
        print("- - - - \nRAM usage: " + str(psutil.virtual_memory().percent) + " %\nRAM available: "+ str(round(psutil.virtual_memory().free/2.**30, 2)) +" GB\nRAM total: "+ str(round(psutil.virtual_memory().total/2.**30,2)) +" GB\n- - - -")
        userInput = input(": ")
        user(userInput)
    
    if userInput == "all":
        clear()
        print("- - - - -\nCPU usage:"+ str(psutil.cpu_percent()) +" % \nRAM usage: "+str(psutil.virtual_memory().percent)+" %\n- - - - -")
        userInput = input(": ")
        user(userInput)

if __name__ == "__main__":
    run = True
    while run:
        clear()
        print("- - - - - \nCPU (cpu usage), RAM (ram usage), ALL(ram and cpu usage), QUIT (quit) \n- - - - -")
        userInput = input(": ")
        userInput.lower()
        user(userInput)
        