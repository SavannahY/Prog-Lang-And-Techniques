'''
Name: Zhengjie Yang
Penn ID: 44562517
Statement of work:
    when met with error, I go to https://stackoverflow.com
    I worked alone without asking for eternal help
inputs that leads to "win": 0,0,0,0,0,0,0,0,0,0,5,3
inputs that leads to "lose":0,0,0,0,0,0,0,0,0,0,0
'''
def lunar_landing():
    '''
    this is a game that called lunar_landing
    You will take the role of an astronaut in the lunar module
    attempting to land on the moon’s surface.
    Gravity pulls you towards the moon at an increasing rate of speed.
    In order to land safely, you must burn fuel to
    counter gravity’s acceleration to land on the moon
    at a safe speed (below 10 m/s). However, be careful,
    you can only use so much fuel.
    And if you are too high when you run out of fuel,
    you’ll inevitably crash at an unsafe speed. 
    '''
    t = 0 #set initial time (second)
    altitude = 100.0 #initial altitude (meters)
    v = 0.0 #initial velocity (meters/second)
    fuel = 100.0 #intial fuel (liters)
    '''
    Note that the game should set an initial altitude, velocity,
    and fuel amount. Altitude = 100.0 meters, velocity = 0.0 meters/second,
    and fuel = 100.0 liters can lead to interesting games.
    '''
    print("an initial altitude=",altitude," meters,")
    print("velocity = ",v," meters/second")
    print("fuel =",fuel," liters")

    while altitude >0:

        #Your fuel decreases by the amount specified by the player.
        fuel_burn = input("How much fuel to burn in the next second =")
    
        try:
            val = int(fuel_burn)
        except ValueError:
            print("That's not an number, please try again")
            continue
    
        fuel_burn = float(fuel_burn)
    
        if fuel_burn<0:
            #If a player tries to burn a negative amount of fuel,
            #treat it as if they burnt zero fuel.   
            fuel_burn=0
        if fuel_burn > fuel:
            #If a player specifies to burn more fuel than they have,
            #burn all their fuel.
            fuel_burn=fuel
    
        v = v + 1.6 - fuel_burn * 1.5
        #Each turn, your velocity increases by 1.6 meters per second
        #due to the force of gravity of the moon
        #your velocity decreases by an amount proportional to the fuel you burn.
        #This means you multiply fuel burnt times some constant to get the velocity change.  Using a constant of 0.15 makes the game fairly easy to win.
        #Note, a negative velocity means the lunar module is moving in reverse.

        altitude = altitude - v
        #Your altitude decreases by your velocity
        #left fuel calculation
        fuel = fuel - fuel_burn
        t = t + 1
        #The player will be given their current altitude, velocity, and fuel. 
        print("current time =", t,"seconds")
        print("velocity = ",v," meters/second")
        print("altitude =", altitude," meters,")
        print("fuel left=", fuel," liters")
        #help to seperate different time
        print("\n")
        
    #check the velocity to help indentify win or lose
    if v < 10:
        print("You safely land")
        # land on the moon at a safe speed(below 10 m/s).
    else:
        # land on the moon at a speef >= 10 m/s 
        print("Sorry, your landing is not safe")

    #print landing velocity   
    print("at v =",v,"m/s the landing occured")
    #print time when landing occurs
    print("the landing took",t,"seconds")
    #print fuel left
    print("fuel left is",fuel,"liters")
    return


#go for it
lunar_landing()


# the program should ask if the player wants to play again.

#set up a while loop to restart or end the game
check_point = True
#this while loop is always true
while check_point:
    again_check = input("Hi, Do you want to play again?")
    #set a string including y and Y to check YES
    letters_yes = "yY"
    #set a string including n and N to check NO
    letters_no ="nN"

    if again_check[0] in letters_yes:
        # Any response that begins with ‘y’
        #(capital or lowercase) should play again.
        print("Great, it is time to start again!")
        #play lunar landing again
        lunar_landing()
    
    elif again_check[0] in letters_no:
        # Any response that begins with ‘n’
        #(capital or lowercase) means the user wants to exit.
        print("Okay, goodbye!")
        #exit
        break
    else:
        #Any response that begins with any other character
        #should ask the player again. 
        print("Can you please enter again,")
        #kind message to remind the player what to enter
        print("be sure your response begins with ‘y’or 'n' (capital or lowercase)")

        continue





