import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
face='''
   ******  
  *      *  
 *  ◕‿◕  * 
 *        * 
  *      *  
   ******  
'''
sad_face = '''
   ******  
  *      *  
 *  ಥ_ಥ  * 
 *        * 
  * \/\/ *  
   ******   

'''

draw = '''
█████╗░░█████╗░██████╗░
██╔══██╗██╔══██╗██╔══██╗
██║░░██║██║░░██║██║░░██║
██║░░██║██║░░██║██║░░██║
╚█████╔╝╚█████╔╝██████╔╝
░╚════╝░░╚════╝░╚═════╝░




'''
choice = [rock,paper,scissors]
start = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print("your choise: \n"+ choice[start])

choice_pc = random.randint(0,2)
print("choice pc: \n" + choice[choice_pc])

if start > choice_pc :

    print(f"you win {face} ")
elif choice_pc == start:
    print(f"draw {draw}")
else :
    print(f"you lose {sad_face}")