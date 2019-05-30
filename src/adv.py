from room import Room
from player import Player
from item import Item
from helper_functions import handle_direction, get_item, handle_action

# Declare all the rooms

# This is a dictionary where the key is a the name of a room, and the value is the invocation of a Room class, with two strings passed in a parameters.
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("pebble"), Item("stick"), Item("doughnut")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("runestone")]),

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


# Prints the current room name, description, and items in the room.
# Waits for user input and decides what to do
# Check if command is 1 word.
# If the user enters "q", quit the game.
# If the user enters "i" or "inventory" show player's current inventory.
# Check if command is 1 words: if it is, check if word is a valid direction, if not send error message.
# If user enters valid direction: n, s, e, w then run handle_direction
# Check if command is 2 words: if it is, check that the two word combination is valid, if not send message.
# If two word combination is valid then run get_item and then try handle_action.

while True:
    print(player.current_room)
    string = input('\nEnter a command: ').lower().split()
    if len(string) == 1:
        if string[0] == 'q':
            print("\nWe'll see you next time, adventurer.")
            break
        elif string[0] == 'i' or string[0] == 'inventory':
            inventory = [i.name for i in player.inventory_list]
            print(f"\n Your current inventory: {', '.join(inventory)}\n")
        else:
            player.current_room = handle_direction(string[0], player.current_room)

    elif len(string) == 2:
        item = get_item(string, player)
        try:
            handle_action(item, player)
        except TypeError:
            print('')
    else:
        print('\n**Invalid number of commands given.** \n Please either give a direction(n, s, e, w), or a two word command.\n')


