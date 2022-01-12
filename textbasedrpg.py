import time
import os
import sys
from os import path
#Variables
if path.exists('save.txt'):
    readFile = open('save.txt', 'r')
    print('exists')
    if 'Name' in readFile.read():
        previousSaves = True
previousSaves = False
newGame = False
continueGame = False
moreInfo = False
passedIntro = 0
health = 100
sleepWaitLong = 6
sleepWaitMedium = 4
sleepWaitShort = 3
characterName = 'null'
characterGender = 'null'
savedName = 'null'
endofVillage = False


#Functions
def exitCheck():
    if userInput == 'exit':
        exit()
def healthCheck():
    if userInput == 'health':
        print('Current Health : ',health,'/100')
def startnewGame():
    global newGame
    newGame = True
def startcontinueGame():
    global continueGame
    continueGame = True
def gameOver():
   print('\n---------------------------------------------------')
   print('\n                   - GAME OVER -                   ')
   print('\n---------------------------------------------------')
   print('\nClosing game...')
   time.sleep(5)
   exit()
   while 1:
       os.system("textbasedrpg.py")
       exit()
def speedrunMode():
   print('\n - Speedrun Mode Enabled - ')
   global sleepWaitLong
   global sleepWaitMedium
   global sleepWaitShort
   sleepWaitLong = 0
   sleepWaitMedium = 0
   sleepWaitShort = 0
   print('Returning to Menu...\n')
   time.sleep(3)
   menuFunction()


#Menu
def menuFunction():
    print("Welcome to Kars's Text-RPG!")
    print('\nType a number below to continue')
    if previousSaves == False:
        print('1 = New Game, 2 = More Info, 3 = Options, 4 = Exit')
        menuInput = input()
        if menuInput == '1':
            startnewGame()
        elif menuInput == '2':
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
            time.sleep(3)
            menuFunction()
        elif menuInput == '3':
            print('\n\nDo you want to enable Speedrun Mode? (This makes text scroll instantly)')
            userInput = input()
            if userInput == 'yes' or userInput == 'Yes':
                speedrunMode()
            else:
                print('\n - Speedrun Mode Remains Disabled - ')
                print('Returning to Menu...\n')
                time.sleep(3)
                menuFunction()
        elif menuInput == '4':
            print('\n\nGoodbye')
            exit()
        else:
            print('\nYou did not type a valid number, returning to menu\n\n')
            menuFunction()
    if previousSaves == True:
        print('1 = Continue, 2 = New Game, 3 = More Info, 4 = Options, 5 = Exit')
        menuInput = input()
        if menuInput == '1':
            startcontinueGame()
        elif menuInput == '2':
            startnewGame()
        elif menuInput == '3':
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
            time.sleep(3)
            menuFunction()
        elif menuInput == '4':
            print('\n\nDo you want to enable Speedrun Mode? (This makes text scroll instantly)')
            userInput = input()
            if userInput == 'yes' or userInput == 'Yes':
                speedrunMode()
            else:
                print('\n - Speedrun Mode Remains Disabled - ')
                print('Returning to Menu...\n')
                time.sleep(3)
                menuFunction()
        elif menuInput == '5':
            print('\n\nGoodbye')
            exit()
        else:
            print('\nYou did not type a valid number, returning to menu\n\n')
            menuFunction()
menuFunction()

#Game
if newGame == True:
    for x in range(0,10):
        print('   .      .      .      .      .   ')
        time.sleep(0.1)
        print('  . .    . .    . .    . .    . .  ')
        time.sleep(0.1)
        print(' .   .  .   .  .   .  .   .  .   . ')
        time.sleep(0.1)
        print('  . .    . .    . .    . .    . .  ')
    print('   .      .      .      .      .   ')
    time.sleep(sleepWaitShort)
    print("\n\nYou struggle to open your eyes")
    time.sleep(sleepWaitShort)
    print("As you feel the rain")
    time.sleep(sleepWaitShort)
    print("As you finally open your eyes, you see yourself surrounded by mountains")
    time.sleep(sleepWaitMedium)
    print("Big mountains with snow on the peak")
    time.sleep(sleepWaitShort)
    print("You stand up and feel pain in your legs")
    time.sleep(sleepWaitShort)
    health = 70
    print("With no idea where you are or how you got here")
    time.sleep(sleepWaitShort)
    print("After looking around for a few minutes you see a brown peak on the mountain hill")
    time.sleep(sleepWaitMedium)
    print("It looks like a tower, perhaps its a village!")
    time.sleep(sleepWaitShort)
    villageQ = True
    while villageQ:
        print("Will you go to the village?")
        userInput = input()
        exitCheck()
        healthCheck()
        if userInput == 'yes' or userInput == 'Yes':
            print("\nYou walk towards the village")
            time.sleep(sleepWaitShort)
            print("Your legs start hurting")
            time.sleep(sleepWaitShort)
            print("The village is really far away, this is gonna take a while")
            time.sleep(sleepWaitMedium)
            print("After about 300 meters your legs feel like they're about to fall off")
            time.sleep(sleepWaitMedium)
            print("Maybe you should sit down and give those legs some rest")
            time.sleep(sleepWaitShort)
            userInput = input('Yes or No? :')
            exitCheck()
            healthCheck()
            treeRest = True
            while treeRest:
                if userInput == 'yes' or userInput == 'Yes':
                    print('\nYou sit down underneath a tree')
                    time.sleep(sleepWaitShort)
                    print('Nice and dry')
                    time.sleep(sleepWaitMedium)
                    print('After a few minutes you fall asleep')
                    time.sleep(sleepWaitMedium)
                    print('You get woken up by someone, he has a weapon')
                    time.sleep(sleepWaitMedium)
                    print('The Person : "Are you alright?"')
                    time.sleep(sleepWaitShort)
                    print('You : "I dont know, my legs hurt a lot"')
                    time.sleep(sleepWaitShort)
                    print('The Person : "I can help you walk back to my village, Its dangerous walking out here alone."')
                    time.sleep(sleepWaitLong)
                    print('You stand up and follow him towards the village')
                    time.sleep(sleepWaitShort)
                    print('The Person : "Im glad I found you, you probably wouldve died if you kept walking by yourself')
                    time.sleep(sleepWaitMedium)
                    print('After some walking you arrive in the village')
                    time.sleep(sleepWaitMedium)
                    print('The Person : "Follow me, We can go to my house and I can check your legs')
                    time.sleep(sleepWaitMedium)
                    personHelped = True
                    treeRest = False
                elif userInput == 'no' or userInput == 'No':
                    print('\nYou keep walking')
                    time.sleep(sleepWaitShort)
                    print('After another 500 meters you fall onto your knees')
                    time.sleep(sleepWaitMedium)
                    print('Your legs burst in pain as you are immobilized')
                    time.sleep(sleepWaitShort)
                    print('You look down as you see blood all around you')
                    time.sleep(sleepWaitMedium)
                    gameOver()
                    treeRest = False
                else:
                    print('Please type Yes or No')
                    treeRest = True
            villageQ = False
        elif userInput == 'no' or userInput == 'No':
            print("\nYou decide against going to the village and take shelter under a big rock")
            time.sleep(sleepWaitMedium)
            print("This is a pretty nice place to stay dry for now")
            time.sleep(sleepWaitShort)
            print('A few hours later you look around and start to realize you have no other option')
            time.sleep(sleepWaitMedium)
            print('You decide to go to the village anyway')
            time.sleep(sleepWaitMedium)
            print('You eventually walk up to a dark forest')
            time.sleep(sleepWaitMedium)
            print('Theres no way around the forest so you walk into it')
            time.sleep(sleepWaitMedium)
            print('After a bit of walking you hear a sound coming from the bushes')
            time.sleep(sleepWaitMedium)
            print('You start walking a bit faster')
            time.sleep(sleepWaitShort)
            print('You hear footsteps behind you and you turn around')
            time.sleep(sleepWaitMedium)
            print('\n-----------------------------------------------')
            print('\n              A BEAR has Appeared!             ')
            print('\n-----------------------------------------------\n')
            time.sleep(sleepWaitMedium)
            print('What will you do? (Attack, Run, Nothing)')
            bearQuestion = True
            while bearQuestion:
               userInput = input()
               exitCheck()
               healthCheck()
               if userInput == 'attack' or userInput == 'Attack':
                  print('\nYou attempt an attack')
                  time.sleep(sleepWaitShort)
                  print('You fail to realize the Bear is way stronger')
                  time.sleep(sleepWaitMedium)
                  print('The bear slashes you with his claws')
                  time.sleep(sleepWaitShort)
                  print('You bleed out in the forest')
                  time.sleep(sleepWaitShort)
                  print(' - That was a bad Choice - ')
                  time.sleep(sleepWaitMedium)
                  gameOver()
               elif userInput == 'run':
                  print('\nYou run as fast as you can')
                  time.sleep(sleepWaitShort)
                  print('But the Bear is faster')
                  time.sleep(sleepWaitShort)
                  print('The Bear catches up as you keep running')
                  time.sleep(sleepWaitShort)
                  print('You turn a few corners and hide behind a tree')
                  time.sleep(sleepWaitShort)
                  print('The Bear loses track of you because of turning the corners')
                  time.sleep(sleepWaitMedium)
                  print(' - Wasnt the best Choice but you survived - ')
                  time.sleep(sleepWaitMedium)
                  bearQuestion = False
               elif userInput == 'nothing':
                  print('\nYou stand still as you stare him down')
                  time.sleep(sleepWaitShort)
                  print('The Bear looks confused and walks away into the bushes')
                  time.sleep(sleepWaitShort)
                  print('As you are certain you are out of his sight you continue walking')
                  time.sleep(sleepWaitShort)
                  print(' - That was a good Choice - ')
                  time.sleep(sleepWaitMedium)
                  bearQuestion = False
            print('After some more walking you arrive in the village')
            time.sleep(sleepWaitShort)
            print('A Person walks up to you')
            time.sleep(sleepWaitShort)
            print('The Person : "Oh my god are you ok? You look like youre about to fall apart')
            time.sleep(sleepWaitMedium)
            print('Youre surprised at how worried he is about you when youre a stranger')
            time.sleep(sleepWaitMedium)
            print('The Person : "Your legs look destroyed, Ive got something to help with that. Follow me')
            time.sleep(sleepWaitLong)
            personHelped = False
            villageQ = False
        else:
            print("\nThis is not a valid answer, please type Yes or No")
            villageQ = True
    print('You follow the person into his house, Its quite big')
    time.sleep(sleepWaitShort)
    print('\n - The Persons House - \n')
    time.sleep(sleepWaitShort)
    print('The Person : "Alright, go ahead and take a seat on the couch there"')
    time.sleep(sleepWaitMedium)
    print('You take a seat on the couch')
    time.sleep(sleepWaitShort)
    print('The Person : "I just want to run through some questions to understand who you are first"')
    time.sleep(sleepWaitMedium)
    print('The Person : "Do you want some coffee by any chance?"')
    userInput = input()
    exitCheck()
    healthCheck()
    if userInput == 'yes' or userInput == 'Yes':
        print('The Person nods and goes to make coffee')
        time.sleep(sleepWaitShort)
        print('"Was this the right choice? To follow someone into their home?" You ask yourself')
        time.sleep(sleepWaitMedium)
        print('You look at your legs')
        time.sleep(sleepWaitShort)
        print('Small blood stains on your pants')
        time.sleep(sleepWaitShort)
        print('The Person comes back with coffee')
        time.sleep(sleepWaitShort)
        print('The Person : "Heres your coffee, I hope you like it black"')
        input()
    print('The Person : "Alright well lets get into some questions then"')
    time.sleep(sleepWaitMedium)
    print('The Person : "First off, Whats your name?"')
    characterName = input('Name : ')
    time.sleep(sleepWaitShort)
    print('The Person : "Nice to meet you', characterName,'"')
    time.sleep(sleepWaitShort)
    print('The Person : "So what are you doing here?"')
    time.sleep(sleepWaitShort)
    print('You : "I dont know, I woke up in the middle of a field and I dont remember anything before that"')
    time.sleep(sleepWaitMedium)
    print('The Person : "Hmm, thats odd."')
    time.sleep(sleepWaitShort)
    print('The Person : "Next Question, Whats your gender? (Male, Female, Other)')
    genderQuestion = True
    while genderQuestion:
        userInput = input()
        if userInput == 'Male' or userInput == 'male':
           characterGender = '1'
           genderQuestion = False
        elif userInput == 'Female' or userInput == 'female':
           characterGender = '2'
           genderQuestion = False
        elif userInput == 'Other' or userInput == 'other':
           characterGender = '3'
           genderQuestion = False
        else:
           print('This is not a valid answer please try again\n')
           genderQuestion = True
    time.sleep(sleepWaitShort)
    print('The Person : "Alright and hows your leg feeling?"')
    time.sleep(sleepWaitShort)
    print('You : "Very much in pain but I managed to walk here"')
    time.sleep(sleepWaitShort)
    print('The Person : "Yeah, I think Ill just bandage your leg and then you can rest here for a couple of days"')
    time.sleep(sleepWaitMedium)
    print('The Person : "Ive got a guest room you can stay there if you want"')
    time.sleep(sleepWaitShort)
    print('You : "Sounds good"')
    time.sleep(sleepWaitShort)
    print('The Person shows you to the guest room and bandages your legs')
    time.sleep(sleepWaitShort)
    introComplete = '1'
    print('\n - The Guest Room - \n')
    time.sleep(sleepWaitShort)
    print('Your Progress is being Saved...')
    time.sleep(sleepWaitMedium)
    writeFile = open('save.txt', 'w')
    writeFile.write('Name : ' + characterName)
    writeFile.write('\nGender : ' + characterGender)
    writeFile.write('\n' + introComplete)
    writeFile.close()

if continueGame == True:
    print()
    print()
    with open('save.txt', 'r') as Readfile:
        savedName = Readfile.readline()
        characterName = savedName[7:]
        savedGender = Readfile.readline(1)[9:]
        savedIntro = Readfile.readline(2)
        time.sleep(2)
    if int(savedGender) == 1:
        characterGender = 'Male'
    elif int(savedGender) == 2:
        characterGender = 'Female'
    elif int(savedGender) == 3:
        characterGender = 'Other'
    
    print('This is a test to showcase Saves\n')
    print(savedIntro)
    print('Your name is :', characterName)
    print('Your gender is :', characterGender)
    
      
#Outro
print('\n\n- End of Game - ')
