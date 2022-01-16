import colorama
from colorama import Fore
colorama.init(autoreset=True)
import random
import time
import os

def g(rolls):
	data = "1234567890qwertzuioplkjhgfdsayxcvbnm"
	result = ""
	while rolls >= 1:
		c = random.choice(data)
		result = c + result
		rolls = rolls - 1
	return result

def menu():
	print(f"{Fore.YELLOW}[INFO] The invites you will find in VAC Invites.txt")
	print(" ")
	nn = input("How many invites do you want? ")
	with open("VAC Invites.txt", "w", encoding='utf-8') as file:
		print(" ")
		n = int(nn)
		for x in range(n):
			file.write(f"https://vacban.wtf/?vacinvite={g(40)}\n")
		os.system('cls')
		menu()

print(f"""{Fore.YELLOW}                                                                                         
@@@  @@@  @@@@@@   @@@@@@@ @@@@@@@   @@@@@@  @@@  @@@     @@@  @@@  @@@ @@@@@@@ @@@@@@@@ 
@@!  @@@ @@!  @@@ !@@      @@!  @@@ @@!  @@@ @@!@!@@@     @@!  @@!  @@!   @!!   @@!      
@!@  !@! @!@!@!@! !@!      @!@!@!@  @!@!@!@! @!@@!!@!     @!!  !!@  @!@   @!!   @!!!:!   
 !: .:!  !!:  !!! :!!      !!:  !!! !!:  !!! !!:  !!! !:!  !:  !!:  !!    !!:   !!:      
   ::     :   : :  :: :: : :: : ::   :   : : ::    :  :::   ::.:  :::      :     :       
                                                                                         """)
print("by Dead-Day")
time.sleep(0.1)
print(f"{Fore.BLUE}Discord: https://discord.gg/6Qyufx3mDr")
time.sleep(0.3)
menu()




