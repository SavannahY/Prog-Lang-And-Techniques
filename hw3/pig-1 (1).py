import random

def print_instructions():
    '''the rules of the game. What words you use is up to you.
    Pig is a very simple game.
    Two players take turns;
    on each turn, a player rolls a six-sided die ("die" is the singular of "dice")
    as many times as she wishes,
    or until she rolls a 6.
    Each number she rolls, except a 6, is added to her score this turn;
    but if she rolls a 6, her score for this turn is zero,
    and her turn ends. At the end of each turn,
    the score for that turn is added to the player's total score.
    The first player to reach or exceed 50 wins.
    '''
    print("Welcome to Pig, each turn, you rolls a six-sided die")
    print("Each number you rolls, except a 6, is added to your score this turn")
    print("if you roll a 6, your score for this turn is zero")
    print("the score for that turn is added to the player's total score.")
    print("The first player to reach or exceed 50 wins.")
    
def roll():
    '''Returns a random number in the range 1 to 6, inclusive. (Hint: Find the
    random module on https://docs.pyton.org/3/library/index.html and
    follow the link to find the randint method.)
    '''
    #use imported random pankage to generate die_number
    die_number = random.randint(1,6)
    return die_number

def ask_yes_or_no():
    '''o Prints the prompt as a question to the user, for example, "Roll again? ". If
    the user responds with a string whose first character is 'y' or 'Y', the
    function returns True. If the user responds with a string whose first
    character is 'n' or 'N', the function returns False. Any other response will
    cause the question to be repeated until the user provides an acceptable
    response.
    '''
    # a str including Yy
    answer_yes = 'yY'
    # a str including Nn
    answer_no = 'nN'

    while True:
        choice = input("Roll again?")
        if choice[0] in answer_yes:
            return True
        elif choice[0] in answer_no:
            return False
        #if the answer do not start with yY or nN continue and ask again
        else:
            continue

def computer_move(computer_score, human_score):
    '''The computer rolls some number of times, displays the result of each roll,
    and the function returns the result (either 0 or the total of the rolls). The
    function should use its parameters in order to play more intelligently (for
    example, it may wish to gamble more aggressively if it is behind).
    '''

    score_this_move = 0
    #when the computer score is behind
    if computer_score <= human_score:
        #computer plays more aggresive to achieve more
        while score_this_move < 14:
            this_roll = roll()
            print(this_roll)
            #if computer rolls 6 then first roll is zero
            if this_roll == 6:
                print("computer hit 6, so this tern computer score is 0")
                score_this_move = 0
                break

            else:
                score_this_move += this_roll

    #computer move less aggressive
    else:
        while score_this_move < 10.5:
            #same as above
            this_roll = roll()
            print(this_roll)
            if this_roll == 6:
                print("computer hit 6, so this tern computer score is 0")
                score_this_move = 0
                break

            else:
                score_this_move += this_roll

    print("the computer score this move is {}".format(score_this_move))
    return score_this_move



def human_move(computer_score, human_score):
    '''
    o Repeatedly asks whether the user wants to roll again and displays the
    result of each roll.
    ▪ If the user chooses to roll again, and DOES NOT roll a 6, this
    function adds the roll to the total of the rolls made during this
    move.
    ▪ If the user chooses to roll again, and DOES roll a 6, the function
    returns 0.
    ▪ If the user chooses not to roll again, the function returns the total
    of the rolls made during this move.
    '''
    human_score_this_move = 0
    first_roll = roll()
    print("human first roll is ", first_roll)
    if first_roll != 6:
        human_score_this_move += first_roll

        while ask_yes_or_no():
            this_roll = roll()
            print(this_roll)
            if this_roll ==6:
                print("you hit 6, so this tern your score is 0")
                human_score_this_move = 0
                break
            else:
                human_score_this_move += this_roll
    else:
        print("your first role hit 6, your score is zero")
                
    print("human score this move is {}".format(human_score_this_move))
    return human_score_this_move


def show_current_status(computer_score, human_score):
    '''
    Prints the user’s current score and the computer's current score, how far
    behind (or ahead) the user is, or if there is a tie. (Hint: Call this before
    and after the human's move.)

    '''
    print("now the computer score is", computer_score)
    print("now the human score is", human_score)
    if computer_score>human_score:
        print("you are {} points behind the computer".format(computer_score-human_score))
    elif computer_score<human_score:
        print("you are {} points ahead the computer".format(human_score-computer_score))
    else:
        print("there is a tie")


def show_final_results(computer_score, human_score):
    '''
    Tells whether the human won or lost, and by how much. (Hint: Call this
    when the game has ended.)
    '''
    if computer_score > human_score:
        print("you lost by {} points".format(computer_score - human_score))
    elif computer_score < human_score:
        print("you win by {} points".format(human_score - computer_score))
    else:
        print("there is a tie")
    



def is_game_over(computer_score, human_score):
    
    """
    Returns True if either player has 50 or more, and the players are not tied,
    otherwise it returns False. (Hint: Call this only after the human's move.)
    """
    if computer_score >= 50 or human_score>= 50:
        if computer_score != human_score:
                return True
        else:
            return False
    else:
        return False

def main():
    '''
    This is where your program will start execution.
    Add starter code to the bottom of your script to run the main function
    '''
    #print the rule of the game
    print_instructions()
    #give the initial zero score
    computer_score = 0
    human_score = 0

    #the loop is to determine whether the game is over

    while is_game_over(computer_score, human_score) == False:
        # if the game is not over, the computer and human will take their tern
        computer_score += computer_move(computer_score,human_score)
        #before human move, show current status
        show_current_status(computer_score, human_score)
        #human move
        human_score += human_move(computer_score,human_score )
        #after human move, show current status
        show_current_status(computer_score, human_score)

        #determine whether the computer is the first to exceed 50 and give human another tern
        first_hit = True
        #only give one chance to give human another tern
        if computer_score >= 50 and human_score < 50 and first_hit:
            #another term
            human_score += human_move(computer_score, human_score)
            #the if sentence can only be used once by using the boolean value
            first_hit = False

    #the gave is over, show result
    show_final_results(computer_score, human_score)

if __name__ == "__main__":
    main()



    


