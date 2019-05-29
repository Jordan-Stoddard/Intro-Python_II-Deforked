import random

wins = 0
losses = 0
ties = 0

cmds = ["r", "p", "s"]

def compare_answers(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 0
    elif (player_choice == "r" and computer_choice == "s") or \
        (player_choice == "p" and computer_choice == "r") or \
        (player_choice == "s" and computer_choice == "p"):
        return 1
    else:
        return -1

while True:
    print(f"\n {wins} - {losses} - {ties}")
    cmd = input("Please input r/p/s: ")
    opponent_cmd = random.choice(cmds)
    print(f"Opponent picks {opponent_cmd}")
    if cmd == "q":
        print("Thank you for playing.")
        break
    elif cmd in cmds:
        results = compare_answers(cmd, opponent_cmd)
    else:
        print ("I did not understand that command")
        continue
    if results == 1:
        print("you win")
        wins += 1
    elif results == 0:
        print("you tie")
        ties += 1
    else: 
        print("you lose")
        losses += 1
        


