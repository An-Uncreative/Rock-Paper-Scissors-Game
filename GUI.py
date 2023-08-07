# GuI for Rock paper scissors game
import random
from tkinter import *

# Variables Dictionaries and Fuction

schema ={
    "rock" : {"rock" :1, "paper":0, "scissors":2},
    "paper" : {"rock" :2, "paper":1, "scissors":0},
    "scissors" : {"rock" :0, "paper":2, "scissors":1},
}

computer_score =0
user_score =0

def converted_outcome(number):
    if number == 1:
        return "rock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "scissors"
    
def outcome_handler(user_choice) :
    global computer_score
    global user_score
    random_pick = random.randint(1,3)
    computer_choice = converted_outcome(random_pick)
    result = schema[user_choice][computer_choice]

    player_choice_view.config(fg="red", text="You picked : " + str(user_choice))
    computer_choice_view.config(fg="green", text="Computer picked : " + str(computer_choice))

    if result == 2 :
        user_score += 1
        player_score_view.config(text="Player Score : " + str(user_score))
        outcome_view.config(text="Congrats you won", fg="blue")
    elif result == 1 :
        outcome_view.config(text="That was a draw")
    elif result == 0 :
        computer_score+= 1
        computer_score_view.config(text="Computer Score : " + str(computer_score))
        outcome_view.config(text="Computer won, you Loser", fg="blue")

# Main screen 
master = Tk()
master.title("A game of Rock, Paper, Scissors")

# labels
Label(master, text="Rock, Paper, Scissors", font=("calibri",14)).grid(row=0,sticky=N,pady=10,padx=200)
Label(master, text="Please pick an option", font=("calibri",12)).grid(row=1,sticky=N)
player_score_view = Label(master,text="Player Score : 0", font=("calibiri",11))
player_score_view.grid(row=2, sticky=W)
computer_score_view = Label(master,text="Computer Score : 0", font=("calibiri",11))
computer_score_view.grid(row=2, sticky=E)
player_choice_view = Label(master,font=("calibiri",11))
player_choice_view.grid(row=3, sticky=W)
computer_choice_view = Label(master, font=("calibiri",11))
computer_choice_view.grid(row=3, sticky=E)
outcome_view = Label(master, font=("calibiri",11))
outcome_view.grid(row=3, sticky=N)

# Buttons
Button(master, text="Rock", width=15, command=lambda:outcome_handler("rock")).grid(row=4, sticky=W, padx=5, pady=5)
Button(master, text="Paper", width=15, command=lambda:outcome_handler("paper")).grid(row=4, sticky=N, pady=5)
Button(master, text="Scissors", width=15, command=lambda:outcome_handler("scissors")).grid(row=4, sticky=E, padx=5, pady=5)
Label(master).grid(row=5)



master.mainloop()