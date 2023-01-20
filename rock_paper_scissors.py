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

assets = [rock, paper, scissors]

txt = input("Insert '0' for rock, '1' for paper or '2' for scissors: ")
i = int(txt)
player = assets[i]

j = random.randint(0,2)
ai = assets[j]

if i == j:
    message = "Tie!"
elif (i-j) ==  -1 or (i-j) == 2:
    message = "You Lost!"
else:
    message = "You Win!"

print("You: ")
print(player)
print("Computer: ")
print(ai)
print(message)
