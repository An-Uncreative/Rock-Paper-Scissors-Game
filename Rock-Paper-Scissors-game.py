import random

options = ["rock","paper","scissors"]
play_again = ["yes", "no"]
user_wins = 0
computer_wins = 0

while True :
    guess = input("Choose Rock, Paper, or Scissors = ").lower()
    x = random.randint(0,2)
    #0 is rock, 1 is paper, 2 is scissors
    computer_pick = options[x]
    if guess not in options :
        print("Please input Rock, Paper, or Scissors...")
        continue
    elif guess == computer_pick :
        print("I also picked ", computer_pick, ", you cheat.")
        user_wins += 0
        computer_wins += 0
        replay = input("Do you wanna play again? : ").lower()
        while replay not in play_again :
            replay = input("Do you wanna play again : ")
            if replay not in play_again :
                continue
        if replay == "yes" :
            continue
        else :
            print("Alright lets call it a day, bye")
            break
    elif guess == "rock" and computer_pick == "scissors" :
        user_wins += 1
        print("Noo... I picked", computer_pick, " you beat me, Congrats")
        replay = input("Do you wanna play again? : ").lower()
        while replay not in play_again :
            replay = input("Do you wanna play again : ")
            if replay not in play_again :
                continue
        if replay == "yes" :
            continue
        elif replay == "no" :
            print("Alright lets call it a day, bye")
            break
    elif guess == "paper" and computer_pick == "rock" :
        user_wins += 1
        print("Noo... I picked", computer_pick, " you beat me, Congrats")
        replay = input("Do you wanna play again? : ").lower()
        while replay not in play_again :
            replay = input("Do you wanna play again : ")
            if replay not in play_again :
                continue
        if replay == "yes" :
            continue
        else :
            print("Alright lets call it a day, bye")
            break
    elif guess == "scissors" and computer_pick == "paper" :
        user_wins += 1
        print("Noo... I picked", computer_pick, " you beat me, Congrats")
        replay = input("Do you wanna play again? : ").lower()
        while replay not in play_again :
            replay = input("Do you wanna play again : ")
            if replay not in play_again :
                continue
        if replay == "yes" :
            continue
        else :
            print("Alright lets call it a day, bye")
            break
    else :
        computer_wins += 1
        print("Yes!!... I picked", computer_pick, " I beat you, LOSER... hehe, you are a LOSER!")
        replay = input("Do you wanna play again? : ").lower()
        while replay not in play_again :
            replay = input("Do you wanna play again : ")
            if replay not in play_again :
                continue
        if replay == "yes" :
            continue
        else :
            print("Alright lets call it a day, bye")
            break
if computer_wins > user_wins :
    print("hehehe... I beat you. That wasn't even challenging at all. Anyways I won ", computer_wins, " times, and you won ", user_wins," times")
elif computer_wins < user_wins :
    print("Finally someone has bested me. You won ", user_wins, "times, and I won ", computer_wins, " times.")
else :
    print("I've finally met my match, it was a tie.")
        
