import time
from imports import *

class Menu:
    def __init__(self, previousSaves):
        self.previousSaves = previousSaves
        
    def start(self, sleep):
        time.sleep(sleep)
        options = "1 = New Game, 2 = More Info, 3 = Options, 4 = Exit"
        if self.previousSaves:
            options = "1 = Continue, 2 = New Game, 3 = More Info, 4 = Options, 5 = Exit"
        
        print("Welcome to Kars's Text-RPG!")
        print('\nType a number below to continue')
        print(options)
        menuInput = input()
        if menuInput == "1":
            if self.previousSaves:
                self.startcontinueGame()
            self.startnewGame()
                
        elif menuInput == "2":
            if self.previousSaves:
                self.startnewGame()
            else:
                self.moreInfo()
                
        elif menuInput == "3":
            if self.previousSaves:
                self.moreInfo()
            else:
                self.options()
                
        elif menuInput == "4":
            if self.previousSaves:
                self.options()
            else:
                exit()
        
        elif menuInput == "5" and self.previousSaves:
            exit()
                
        else:
            print('\nYou did not type a valid number, returning to menu\n\n')
            self.start()
        
           
    def options(self):
        print('\n\nDo you want to enable Speedrun Mode? (This makes text scroll instantly)')
        userInput = input()
        if userInput == 'yes' or userInput == 'Yes':
            print('\n - Speedrun Mode Enabled - ')
            sleepWaitLong = 0
            sleepWaitMedium = 0
            sleepWaitShort = 0
            print('Returning to Menu...\n')
            self.start()
        else:
            print('\n - Speedrun Mode Remains Disabled - ')
            print('Returning to Menu...\n')
            self.start(3)
             
            
    
    def moreInfo(self):
        for x in range (0, 5):
            print()
        print('- More Info -')
        print('This is a Text-RPG, this means that this is an RPG game that only uses text.')
        print('You can play the game by typing in your answer to questions that will be asked.')
        print('Your experience will be different depending on your answers.')
        print('During your adventure you can type "exit" at any time to leave the game')
        print('Progress is automatically saved!')
        print('Enjoy! (ENTER to Return)')
        input()
        print('\nReturning to menu...\n')
        self.start(3)
            
            
    def startnewGame(self):
        return
    
    def startcontinueGame(self):
        return
        
        
        
            
        









































# def startnewGame(newGame):
#     return

# def speedrunMode():
#     return

# def startcontinueGame():
#     return

# previousSaves = False
# newGame = True

# import time


# #Menu
# def menuFunction():
#     print("Welcome to Kars's Text-RPG!")
#     print('\nType a number below to continue')
#     if previousSaves == False:
#         print('1 = New Game, 2 = More Info, 3 = Options, 4 = Exit')
#         menuInput = input()
#         if menuInput == '1':
#             startnewGame(newGame)
#         elif menuInput == '2':
#             for x in range (0, 5):
#                 print()
#             print('- More Info -')
#             print('This is a Text-RPG, this means that this is an RPG game that only uses text.')
#             print('You can play the game by typing in your answer to questions that will be asked.')
#             print('Your experience will be different depending on your answers.')
#             print('During your adventure you can type "exit" at any time to leave the game')
#             print('Progress is automatically saved!')
#             print('Enjoy! (ENTER to Return)')
#             input()
#             print('\nReturning to menu...\n')
#             time.sleep(3)
#             menuFunction()
#         elif menuInput == '3':
#             print('\n\nDo you want to enable Speedrun Mode? (This makes text scroll instantly)')
#             userInput = input()
#             if userInput == 'yes' or userInput == 'Yes':
#                 speedrunMode()
#             else:
#                 print('\n - Speedrun Mode Remains Disabled - ')
#                 print('Returning to Menu...\n')
#                 time.sleep(3)
#                 menuFunction()
#         elif menuInput == '4':
#             print('\n\nGoodbye')
#             exit()
#         else:
#             print('\nYou did not type a valid number, returning to menu\n\n')
#             menuFunction()
#     if previousSaves == True:
#         print('1 = Continue, 2 = New Game, 3 = More Info, 4 = Options, 5 = Exit')
#         menuInput = input()
#         if menuInput == '1':
#             startcontinueGame()
#         elif menuInput == '2':
#             startnewGame()
#         elif menuInput == '3':
#             for x in range (0, 5):
#                 print()
#             print('- More Info -')
#             print('This is a Text-RPG, this means that this is an RPG game that only uses text.')
#             print('You can play the game by typing in your answer to questions that will be asked.')
#             print('Your experience will be different depending on your answers.')
#             print('During your adventure you can type "exit" at any time to leave the game')
#             print('Progress is automatically saved!')
#             print('Enjoy! (ENTER to Return)')
#             input()
#             print('\nReturning to menu...\n')
#             time.sleep(3)
#             menuFunction()
#         elif menuInput == '4':
#             print('\n\nDo you want to enable Speedrun Mode? (This makes text scroll instantly)')
#             userInput = input()
#             if userInput == 'yes' or userInput == 'Yes':
#                 speedrunMode()
#             else:
#                 print('\n - Speedrun Mode Remains Disabled - ')
#                 print('Returning to Menu...\n')
#                 time.sleep(3)
#                 menuFunction()
#         elif menuInput == '5':
#             print('\n\nGoodbye')
#             exit()
#         else:
#             print('\nYou did not type a valid number, returning to menu\n\n')
#             menuFunction()
# menuFunction()