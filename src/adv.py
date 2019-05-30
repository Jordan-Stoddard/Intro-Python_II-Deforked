from room import Room
from player import Player
from item import Item
from helper_functions import handle_direction

# Declare all the rooms

# This is a dictionary where the key is a the name of a room, and the value is the invocation of a Room class, with two strings passed in a parameters.
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("pebble"), Item("stick"), Item("doughnut")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

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

def get_item(input, player):
    if input[0] == 'get' or input[0] == 'take':
        item_list = [i.name for i in player.current_room.item_list]
        match = [i  for i in item_list  if i == input[1]]
        try:
            return ['getItem', match[0]]
        except IndexError:
            print(f"\n**Sorry, but that item doesn't exist in this room. Try something else.**")

    elif input[0] == 'drop':
        inventory_list = [i.name for i in player.inventory_list]
        match = [i  for i in inventory_list  if i == input[1]]
        try:
            return ['dropItem', match[0]]
        except IndexError:
            print(f"\n**Sorry, but that item doesn't exist in your inventory. Try something else.**")

    else:
        print("""
        ** Invalid two word command.**
        Two word command list: get [item], take [item], drop [item]\n""")


# Write a loop that:
#
while True:
# * Prints the current room name, description, and items in the room.
    print(player.current_room)

# * Waits for user input and decides what to do
    string = input('\nEnter a command: ').lower().split()

# Check if command is 1 word.
    if len(string) == 1:
# If the user enters "q", quit the game.
        if string[0] == 'q':
            print("\nWe'll see you next time, adventurer.")
            break
# If hte user enters "q" or "inventory" show player's current inventory.
        elif string[0] == 'i' or string[0] == 'inventory':
            inventory = [i.name for i in player.inventory_list]
            print(f"\n Your current inventory: {', '.join(inventory)}\n")
# If user enters valid direction: n, s, e, w then run handle_direction
        else:
            player.current_room = handle_direction(string[0], player.current_room)
        
# Check if command is 2 words.
    elif len(string) == 2:
        item = get_item(string, player)
        try:
            if item[0] == 'getItem':
                player.current_room.item_list = [i.name if i.name == item[1] else i  for i in player.current_room.item_list]
                player.current_room.item_list = [True if i == item[1] else i  for i in player.current_room.item_list]              
                player.current_room.item_list.remove(True)
                player.inventory_list.append(Item(item[1]))
                print(f"\n**You picked up the {item[1]}!**\n It's now in your inventory.\n Try i or inventory to see your current inventory.\n")
            elif item[0] == 'dropItem':
                print('Went into getDrop')
                player.inventory_list = [i.name if i.name == item[1] else i  for i in player.inventory_list]
                player.inventory_list = [True if i == item[1] else i  for i in player.inventory_list]              
                player.inventory_list.remove(True)
                player.current_room.item_list.append(Item(item[1]))
                print(player.inventory_list)
                print(f"\n**You dropped your {item[1]}!**\n")
        except TypeError:
            print('')
    else:
        print('\n**Invalid number of commands given.** \n Please either give a direction(n, s, e, w), or a two word command.\n')

"""
If we have a two word command,
check if the first word in the two word command is get or take
if it is, check the second word,
if it isn't send error

if second word is == to an item in the item_list of the room then take the item from the room's item_list and place it in the players inventory.
"""


