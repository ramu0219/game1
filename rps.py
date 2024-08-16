import random
while True:
      choices = ["rock","paper","scissors"]
      computer = random.choice(choices)
      player=None
      while player not in choices:
          player = input("rock,paper,scissors?:").lower()

      if player == computer:
         print("computer:", computer)
         print("player:", player)
         print("tie")
      elif player == "rock":
         if computer == "scisoors":
             print("computer:", computer)
             print("player:", player)
             print("you win")
         if computer == "paper":
             print("computer:", computer)
             print("player:", player)
             print("you lose")
      elif player == "paper":
         if computer == "scisoors":
             print("computer:", computer)
             print("player:", player)
             print("you lose")
         if computer == "rock":
             print("computer:", computer)
             print("player:", player)
             print("you win")
      elif player == "scissors":
         if computer == "rock":
             print("computer:", computer)
             print("player:", player)
             print("you lose")
         if computer == "paper":
             print("computer:", computer)
             print("player:", player)
             print("you win")

      play_again=input("playagain?(yes/no):")
      if play_again != "yes":
          break
print("thank you for playing")

