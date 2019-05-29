from room import Room
from player import Player

# Declare all the rooms

# This is a dictionary where the key is a the name of a room, and the value is the invocation of a Room class, with two strings passed in a parameters.
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

# room[''] <== This is bracket notation to access a key inside the room dictionary
                #.n_to this is dot notation, to access an attribute or method on the Room class. 
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])


"""
handle_direction takes in the string entered by user and the current room instance from the player,
creates an attribute variable that concatenates the input string + '_to'
uses hasattr function to check if the current_room Room instance has the attribute we just defined
then if it does return the getattr function to get the value of that attribute from that Room instance
"""
def handle_direction(input, current_room):
    attribute = input + '_to'
    if hasattr(current_room, attribute):
        return getattr(current_room, attribute)
    else:
# Print an error message if the movement isn't allowed.
        print("You can't go that way! \n Either the map doesn't go that direction or you typed an invalid direction key. \n Direction keys are: n, s, e, w \n")
        return current_room

# Write a loop that:
#
while True:
# * Prints the current room name
    print(player.current_room.name)
# * Prints the current description (the textwrap module might be useful here).
    print(player.current_room.description)
# * Waits for user input and decides what to do
    string = input('\nEnter a command: ').lower().split()
    if len(string) == 1:
# If the user enters "q", quit the game.
        if string[0] == 'q':
            print("We'll see you next time, adventurer.")
            break
# If the user enters a cardinal direction, attempt to move to the room there.
        player.current_room = handle_direction(string[0], player.current_room)
    elif len(string) == 2:
        print('You entered a two word command')
    else:
        print('Invalid number of commands given. Please either give a direction(n, s, e, w), or a two word command.')


