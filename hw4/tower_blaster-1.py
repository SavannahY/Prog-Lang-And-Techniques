def print_instructions():
    '''
    Tower Blaster is often played with 2 human players, but we will keep this simple and just play the user versus the computer.
     The user’s moves are decided by the user playing the game, by asking for input, and the computer’s moves are decided by the program.
    For an online version of Tower Blaster, go here: https://www.gamefools.com/onlinegames/free/towerblaster.html
    A Tower Blaster game starts with a main pile of 60 bricks, each numbered from 1 to 60.
    Think
     of the numbers on the bricks as the width of the bricks.
    The objective is to be the first player to arrange 10 bricks in your own tower from lowest to highest
    (from the top down), because the tower will be unstable otherwise.

    The bricks in the main pile are shuffled at the start and
    both the user and the computer are dealt 10 bricks from the main pile.
    As a player receives each brick, they must place it on top of their current tower in the order it is received.
    Yes, initially your tower is likely to be unstable.

    After the first 10 bricks are dealt to the user and the computer,
    there will be 40 bricks remaining in the main pile.
    The top brick of the main pile is turned over to begin the discarded brick pile.
    On each player’s turn, the player chooses to pick up the top brick from the discard pile or
    to pick up the top brick from the main pile.
     The top brick from the discard pile is known. In other words, the discard pile is ‘face up’ and
     everyone knows how wide the top brick is.
     The main pile is ‘face down’. Choosing the top brick from the main pile can be risky,
     because the player does not know what the brick is.
    Once a player chooses a brick, either from the discard pile or from the main pile,
    the player decides where in the tower to put the brick. The tower is always 10 bricks high,
    so placing a brick means that an existing brick in the tower is removed and replaced with the new brick.
    If the player takes a brick from the main pile (the one that is ‘face down’), the player can reject it and place it in the discard pile.
    This means that nothing in that player’s tower changes during that turn.
    If the player takes a brick from the discard pile (the one that is ‘face up’), the player MUST place it into the tower.
    The first player to get their 10 bricks in order wins.
    If, at any point, all of the cards have been removed from the main pile of bricks,
    then all of the cards in the discard pile are shuffled and moved to the main pile.
    Then the top card is turned over to start the new discard pile.

    '''
    print("Welcome to Tower Blaster, just play the user versus the computer")
    print("For an online version of Tower Blaster, go here: https://www.gamefools.com/onlinegames/free/towerblaster.html")
    print("A Tower Blaster game starts with a main pile of 60 bricks, each numbered from 1 to 60.")
    print("Think of the numbers on the bricks as the width of the bricks.")
    print("The bricks in the main pile are shuffled at the start and both the user and the computer are dealt 10 bricks from the main pile. ")
    print("The first player to reach or exceed 50 wins.")
    print(" The objective is to be the first player to arrange 10 bricks in your own tower from lowest to highest ")
    print("The top brick of the main pile is turned over to begin the discarded brick pile.")
    print("The top brick from the discard pile is known. In other words, the discard pile is ‘face up’ and everyone knows how wide the top brick is. ")
    print("The main pile is ‘face down’. Choosing the top brick from the main pile can be risky, because the player does not know what the brick is.")
    print("Once a player chooses a brick, either from the discard pile or from the main pile, the player decides where in the tower to put the brick. ")
    print("so placing a brick means that an existing brick in the tower is removed and replaced with the new brick.")
    print("If the player takes a brick from the main pile (the one that is ‘face down’), the player can reject it and place it in the discard pile.")
    print("This means that nothing in that player’s tower changes during that turn.")
    print("If the player takes a brick from the discard pile (the one that is ‘face up’), the player MUST place it into the tower.")
    print("The first player to get their 10 bricks in order wins.")
    print("***********************************************************************************************************************************************")



def setup_bricks():
    '''
    • You’ll run this function once at the beginning of the game.
    • Creates a main pile of 60 bricks,
    represented as a list containing the integers 1 –
    60.
    • Creates a discard pile of 0 bricks, represented as an empty list.
    • This function returns both lists.
    o The method of returning 2 things from a function is to make a tuple
    out of the return values.
    For an example of this, refer to the lecture slides/code
    where we return both the maximum and minimum in a list.  
    '''

    #give an empty main pile
    main_pile = []
    #put 1-60
    for i in range(1,61):
        main_pile.append(i)
    #set up an empty discard
    discard = []
    return((main_pile,discard))



import random

def shuffle_bricks(bricks):
    '''
    • Shuffle the given bricks (represented as a list). (You’ll do this to start the game.)
    • This function does not return anything.
    • You are allowed to import the random module and just use random.shuffle.
    '''
    random.shuffle(bricks)
    #print(bricks)


#main_pile =[]
#discard=[6,5,7,9,100]

def check_bricks(main_pile, discard):
    '''
    • Check if there are any cards left in the given main pile of bricks.
    • If not, shuffle the discard pile (using the shuffle function) and move those bricks
    to the main pile.
    • Then turn over the top card to be the start of the new discard pile.
    '''
    if main_pile == []:
        #shuffle the discard
        shuffle_bricks(discard)
        #let main pile get discrad
        main_pile = discard
        #reset discard
        discard = main_pile[0]
        #pop first of main pile
        main_pile.pop(0)

    #return(main_pile,discard)

#(main_pile,discard) = check_bricks(main_pile, discard)
#print(main_pile)
#print(discard)



def check_tower_blaster(tower):
    '''
    • Given a tower (the user’s or the computer’s list), determine if stability has been achieved.
    • Remember, stability means that the bricks are in ascending order.
    • This function returns a boolean value.
    '''
    if(tower == sorted(tower)):
        return True
    else:
        return False
#main_pile =[]
#discard= [4,5,6]
#print(check_tower_blaster(discard))



def get_top_brick(brick_pile):
    '''
    • Remove and return the top brick from any given pile of bricks. This can be the main_pile, the discard pile, or your tower or the computer's tower. In short, remove and return the first element of any given list.  
    • It is used at the start of game play for dealing bricks. This function will also be used during each player’s turn to take the top brick from either the discarded brick pile or from the main pile.  
    • Note: Brick piles are vertically oriented structures, with the top having index 0.
    • This function must return an integer.
    '''
    first_element = brick_pile[0]
    brick_pile.pop(0)
    return(first_element)
#discard= [4,5,6]
#print(get_top_brick(discard))


def deal_initial_bricks(main_pile):
    '''
    • Start the game by dealing two sets of 10 bricks each, from the given main_pile.  
    • Make sure that you follow the normal conventions of dealing. So, you have to
    deal one brick to the computer, one to the user, one to the computer, one to the
    user, and so on.  
    • The computer is always the first person that gets dealt to and always plays first.
    • Remember that the rules dictate that you have to place your bricks one on top of
    the other. In the earlier picture, this would mean that someone was dealt 46, 33,
    10, ..., in that order.
    • This function returns a tuple containing two lists - one representing the user’s
    hand and the other representing the computer’s hand.
    '''
    #set up human_tower and computer tower
    human_tower = []
    computer_tower = []
    for i in range(0,10):
        #you have to deal one brick to the computer, one to the user
        computer_tower.append(get_top_brick(main_pile))
        human_tower.append(get_top_brick(main_pile))
    return((human_tower,computer_tower))
#print(deal_initial_bricks(main_pile))
#print(main_pile)




def add_brick_to_discard(brick, discard):
    '''
    • Add the given brick (represented as an integer) to the top of the given discard pile
    (which is a list)
    • This function does not return anything.
    '''
    discard.insert(0,brick)

#brick = 9
#discard =[4,5]
#add_brick_to_discard(brick, discard)
#print(discard)

#new_brick, brick_to_be_replaced=899,78
#tower=[2,3,4,67,64,5]
#discard=[8]
#print((new_brick, brick_to_be_replaced, tower, discard))

def find_and_replace(new_brick, brick_to_be_replaced, tower, discard):
    '''
    • Find the given brick to be replaced (represented by an integer)
     in the given tower and replace it with the given new brick.
    • Check and make sure that the given brick to be replaced
     is truly a brick in the given tower.
    • The given brick to be replaced then
    gets put on top of the given discard pile.  
    • Return True if the given brick is replaced,
    otherwise return False.
    '''

    if brick_to_be_replaced in tower:
        #find the index of brick to be replaced
        brick_index = tower.index(brick_to_be_replaced)
        #add_brick_to_discard
        add_brick_to_discard(brick_to_be_replaced, discard)
        #pop old and insert new
        tower.pop(brick_index)
        tower.insert(brick_index, new_brick)
        return True
    else:
        return False
#print(find_and_replace(new_brick, brick_to_be_replaced, tower, discard))
#print((new_brick, brick_to_be_replaced, tower, discard))

def ask_yes_or_no():
    '''Prints the prompt as a question to the user, for example, "Roll again? ". If
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
        choice = input("choose it? your response starts with  'y' or 'Y'is YES, 'n' or 'N' is NO")
        if choice[0] in answer_yes:
            return True
        elif choice[0] in answer_no:
            return False
        #if the answer do not start with yY or nN continue and ask again
        else:
            continue


def computer_play(tower, main_pile, discard):
    '''

    • This function is where you can write the computer’s strategy.
    It is also the function where we are giving you very little guidance in terms of actual code.
    • You are supposed to be somewhat creative here, but I do want your code to be deterministic.
    That is, given a particular tower and a particular brick
    (either from the discarded brick pile or as the top brick of the main pile),
    you either always take the brick or always reject it.  
    • Here are some potential decisions the computer has to make:
    o Given the computer’s current tower,
    do you want to take the top brick from the discarded brick pile or
    do you want to take the top brick from
    the main pile and see if that brick is useful to you.  
    o How do you evaluate the usefulness of a brick and which position it
    should go into.  
    o There might be some simple rules you can give the computer. For
    instance, it is disastrous (provably so) to put something like a 5 at the
    very bottom of the tower. You want big numbers over there.  
    • You are allowed to do pretty much anything in this function except make a
    random decision or make a decision that is obviously incorrect. For instance,
    making your bottom brick a 5 is not very smart and a recipe for disaster.  
    • Also, the computer CANNOT CHEAT. What does that mean? The computer
    cannot peek at the top brick of the main pile and then make a decision to
    go to the discard pile. Its decisions should be something that a human could
     be able to make as well.  
    • This function returns the new tower for the computer.
    • Hint: One approach is to try to think of how you, as a human user, would
    consider selecting a new brick (from the main pile or discard pile) and
    using it to replace a brick in your own tower.
    '''


    #brick_in_need is a list of bricks that computer is looking for
    brick_in_need = []
    #find the brick in need in terms of the number in need
    for i in range(0,10):
        # if brick in need is already there continue
        if tower[i] in range((6*i+1),(6*i+7)):
            continue
        else:
            #extend the list

            brick_in_need.extend(range((6*i+1),(6*i+7)))

    #check if discard[0] meets the need
    if discard[0] in brick_in_need:

        print("computer use first brick of discard",discard[0])
        #use it
        new_brick = get_top_brick(discard)
        #find index
        tower_index = int((new_brick-1)/6)
        print("brick replaced by computer index",tower_index)

        #find brick to be replaced
        brick_to_be_replaced = tower[tower_index]

        #use the functions to replace
        #brick_to_be_replaced = tower[int(discard[0]/6)]
        find_and_replace(new_brick, brick_to_be_replaced, tower, discard)
        #use the function to add brick to discard
        add_brick_to_discard(brick_to_be_replaced, discard)


    #check if computer will use main_pile[0]
    elif main_pile[0] in brick_in_need:
        print("computer used first brick of main pile",main_pile[0])

        #use it
        new_brick = get_top_brick(main_pile)
        #same as above
        tower_index = int((new_brick-1)/6)

        print("index of brick replaced by computer is", tower_index)

        brick_to_be_replaced = tower[tower_index]
        #same as use in discard
        find_and_replace(new_brick, brick_to_be_replaced, tower, discard)
        add_brick_to_discard(brick_to_be_replaced, discard)
    else:
        print(discard[0],main_pile[0],"computer did no action")

    return(tower)





def main():
    '''
    • The function that puts it all together.  
    • You play until either the user or the computer gets Tower Blaster, which means
    their tower stability has been achieved.
    • Unlike the previous HW, we want you to assemble the functionality in the main
    function by yourself. Think about how the game should proceed and where each
    function should go.  
    • All user input should take place in the main function.
    '''
    #prict instruction
    print_instructions()
    #use function to set up
    main_pile, discard = setup_bricks()
    #shuffle
    shuffle_bricks(main_pile)
    #set up human tower and computer tower
    human_tower, computer_tower = deal_initial_bricks(main_pile)
    #set up discard
    discard.append(main_pile.pop(0))

    #print("main_pile,discard", main_pile, discard)
    print("human_tower,computer_tower", human_tower, computer_tower)

    while True:

        #computer move first
        computer_tower = computer_play(computer_tower, main_pile, discard)
        #let user know the human tower
        print("human_tower", human_tower)
        #show first brick in discard
        print("first brick in discard", discard[0])


        #ask if user will use discard[0]
        if ask_yes_or_no():
            #get it
            new_brick = get_top_brick(discard)


            #use int to transform it into int
            brick_to_be_replaced = int(input("which one do you want to be replaced?"))


            #if not find the given value try again
            while find_and_replace(new_brick, brick_to_be_replaced, human_tower, discard) == False:
                brick_to_be_replaced = int(input("which one do you want to be replaced?"))

            #use the two function to replace and add brick to discard
            find_and_replace(new_brick, brick_to_be_replaced, human_tower, discard)
            add_brick_to_discard(brick_to_be_replaced, discard)
            #print(human_tower)

            find_and_replace(new_brick, brick_to_be_replaced, human_tower, discard)
        else:
            print("first brick in main pile",main_pile[0])
            if ask_yes_or_no():
                new_brick = get_top_brick(main_pile)

                brick_to_be_replaced = int(input("which one do you want to be replaced?"))
                # if find_and_replace(new_brick, brick_to_be_replaced, tower, discard) == True:
                #    print("great")
                # else:
                #    print("sorry")
                find_and_replace(new_brick, brick_to_be_replaced, human_tower, discard)
                add_brick_to_discard(brick_to_be_replaced, discard)
                #print(human_tower)
        if check_tower_blaster(human_tower) == True:
            print("you win")
            break

        if check_tower_blaster(computer_tower) == True:
            print("computer win")
            break

        check_bricks(main_pile, discard)
        print("human_tower",human_tower)



if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()
