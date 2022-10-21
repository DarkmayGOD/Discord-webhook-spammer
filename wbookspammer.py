
#We need to import things
from dhooks import Webhook #download it.
import time
from colorama import Fore
from colorama import Style
from colorama import init
init()

#By DarkmayGOD
#Github: DarkmayGOD


#Colors

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
#End of colors


print(f"""




{bcolors.HEADER} _____ __ __ ____  ____  __ __      __    __   ___ ____  __ __  ___   ___  __  _       _________   ____ ___ ___ ___ ___   ___ ____  
|     |  |  |    \|    \|  |  |    |  |__|  | /  _]    \|  |  |/   \ /   \|  |/ ]     / ___/    \ /    |   |   |   |   | /  _]    \ 
|   __|  |  |  _  |  _  |  |  |    |  |  |  |/  [_|  o  )  |  |     |     |  ' /     (   \_|  o  )  o  | _   _ | _   _ |/  [_|  D  )
|  |_ |  |  |  |  |  |  |  ~  |    |  |  |  |    _]     |  _  |  O  |  O  |    \      \__  |   _/|     |  \_/  |  \_/  |    _]    / 
|   _]|  :  |  |  |  |  |___, |    |  `  '  |   [_|  O  |  |  |     |     |     \     /  \ |  |  |  _  |   |   |   |   |   [_|    \ 
|  |  |     |  |  |  |  |     |     \      /|     |     |  |  |     |     |  .  |     \    |  |  |  |  |   |   |   |   |     |  .  \
                                                                                                                                    
                                                        
                                                                                                                                                   
                                                    Github: DarkmayGOD
                                             Made with love, by DarkmayGOD <3





 {bcolors.OKCYAN}""")



#Questions

print("What message do you want to send?")
message = input()
print("What delay do you want there? (in seconds) RECOMMENDED: 1")
delay = int(input())
print("Webhook here: (Server settings->Integrations->Webhooks->New Webhook->Copy Webhook)")
webhook = Webhook(input())

#Thing

print(f"Do you want to continue? ({bcolors.OKGREEN}y{bcolors.HEADER}/{bcolors.FAIL}n{Style.RESET_ALL})")
contin = input()

#If

if contin == "y":
    print("Starting in 3. seconds then..")
    time.sleep(1)
    print("1.")
    time.sleep(1)
    print("2.")
    time.sleep(1)
    print("3.")
    time.sleep(1)
    print("Okay, I am sending this! in 2 seconds")
    time.sleep(2)

    #Spammer

    while True:
        webhook.send(message)
        time.sleep(delay)
        print(bcolors.OKGREEN, "Message was succesfully sent")
#End of the story :(