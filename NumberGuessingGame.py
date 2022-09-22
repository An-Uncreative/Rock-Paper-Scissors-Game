from curses.ascii import isdigit
import random

print("Try to guess the range of the numbers.\n if you need an hint you'll get it after your first miss, but your number of attempts will be reduced by one.\n P:S; you only have ten tries. ")
pickone = ["y","n"]
NumberOfGuesses = 10
trials =  0
options = ["X is between 0 and 30", "X is "]
while NumberOfGuesses > 0:
    print("The number ranges betwwen X and Y. ")
    guessrangex = int(input("guess X : "))
    guessrangey = int(input("guess Y :" ))
    hint = input("press Y for hint, but remember that your number of attempts will be reduced by one. If you dont want press N").lower()
    hint = input("press Y for hint, but remember that your number of attempts will be reduced by one. If you dont want press N").lower()
    x = random.randint(0,30)
    y = random.randint(70,100)
    rangeguess = random.randint(x,y)
    if guessrangex.isdigit() :
        NumberOfGuesses -= 1
        guessrangex = int(guessrangex)
        if guessrangex == x :
            print("Congrats, now lets do Y... try the second number.\n\n\n")
            guessrangey = int(input("guess Y :" ))
            if guessrangey.isdigit() :
             NumberOfGuesses -= 1
             guessrangey = int(guessrangey)
             if guessrangey == y :
                print("Congrats, you got both answers in", NumberOfGuesses, "tries.\n\n\n")
             else :  
                print("Wrong you have ", NumberOfGuesses,"left")
                hint = input("press Y for hint, but remember that your number of attempts will be reduced by one. If you dont want press N").lower()
                while hint not in pickone :
                    hint = input("press Y for hint, but remember that your number of attempts will be reduced by one. If you dont want press N").lower()
                    if hint not in pickone :
                        continue
                if hint == "y" and guessrangex != x :
                    NumberOfGuesses -= 1
                    print("Alright, one extra chance has been removed. You have ", NumberOfGuesses, " left, goodluck.")
                    print("X is between 0 and 30 ")
                    continue
                elif hint =="y" and guessrangex > x :
                    NumberOfGuesses -= 1 
                    print("Alright, one extra chance has been removed. You have ", NumberOfGuesses, " left, goodluck.")
                    print("The number is less than the number you guessed")
                    continue
                elif hint =="y" and guessrangey < x :
                    NumberOfGuesses -= 1
                    print("Alright, one extra chance has been removed. You have ", NumberOfGuesses, " left, goodluck.")
                    print("The number is more than the number you guessed")
            else :
                print("please input a number. ")
                continue
        else :  
            print("Wrong you have ", NumberOfGuesses,"left")
            hint = input("press Y for hint, but remember that your number of attempts will be reduced by one. If you dont want press N").lower()
            while hint not in pickone :
                hint = input("press Y for hint, but remember that your number of attempts will be reduced by one. If you dont want press N").lower()
                if hint not in pickone :
                    continue
            if hint == "y" and guessrangex != x :
                NumberOfGuesses -= 1
                print("Alright, one extra chance has been removed. You have ", NumberOfGuesses, " left, goodluck.")
                print("X is between 0 and 30 ")
                continue
            elif hint =="y" and guessrangex > x :
                NumberOfGuesses -= 1 
                print("Alright, one extra chance has been removed. You have ", NumberOfGuesses, " left, goodluck.")
                print("The number is less than the number you guessed")
                continue
            elif hint =="y" and guessrangey < x :
                NumberOfGuesses -= 1
                print("Alright, one extra chance has been removed. You have ", NumberOfGuesses, " left, goodluck.")
                print("The number is more than the number you guessed")
    else :
        print("please input a number. ")
        continue
   
        if guessrangex == x and guessrangey == y :
            again = input("Cool you actually got it, do you wanna try to guess for the actual number? or just give up. Input Y to continue and N to stop. ").lower()
            while again not in pickone :
             input("Cool you actually got it, do you wanna try to guess for the actual number? or just give up. Input Y to continue and N to stop. ").lower()
             if again not in pickone :
                continue
            if again == "y" :
                actualnumber = input("What is the actual number? : ")
                if actualnumber == rangeguess :
                    print("Wow, I didn't expect anybody to get that")
                    repeat = input("Do you wanna try again? : ")
                    while repeat not in pickone :
                        repeat = input("Do you wanna try again? : ")
                        if repeat not in pickone :
                            continue
                    if repeat == "y" :
                        continue
                    else :
                        break 