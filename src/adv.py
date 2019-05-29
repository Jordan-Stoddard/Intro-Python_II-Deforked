from room import Room
from player import Player
from helper_functions import handle_direction

# Declare all the rooms

# This is a dictionary where the key is a the name of a room, and the value is the invocation of a Room class, with two strings passed in a parameters.
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ["pebble", "stick", "dougnut"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
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
player = Player(room['outside'], 'Bart', [])

def handle_action(input, current_room, player):
    if input[0] == 'get' or input[0] == 'take':
        match = [i for i in current_room.item_list if input[1] in current_room.item_list]
        try:
            return match[0]
        except IndexError:
            print(f"\n**Sorry, but that item doesn't exist in this room. Try something else.**\n")
    else:
        print("""
        ** Invalid two word command.**
        Two word command list: get [item], take [item]\n""")


# Write a loop that:
#
while True:
# * Prints the current room name, description, and items in the room.
    print(player.current_room.name)
    print(player.current_room.description)
    print(f"Items in this area: {', '.join(player.current_room.item_list)}")

# * Waits for user input and decides what to do
    string = input('\nEnter a command: ').lower().split()

# Check if command is 1 word.
    if len(string) == 1:
# If the user enters "q", quit the game.
        if string[0] == 'q':
            print("\nWe'll see you next time, adventurer.")
            break
# If user enters valid direction: n, s, e, w then run handle_direction
        player.current_room = handle_direction(string[0], player.current_room)
        
# Check if command is 2 words.
    elif len(string) == 2:
        handle_action(string, player.current_room)
    else:
        print('\n**Invalid number of commands given.** \n Please either give a direction(n, s, e, w), or a two word command.\n')

"""
If we have a two word command,
check if the first word in the two word command is get or take
if it is, check the second word,
if it isn't send error

if second word is == to an item in the item_list of the room then take the item from the room's item_list and place it in the players inventory.
"""


