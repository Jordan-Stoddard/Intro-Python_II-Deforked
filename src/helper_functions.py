from item import Item

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
        print("""
        
        **You can't go that way!**
        Either the map doesn't go that direction or you typed an invalid direction key.
        Direction keys are: n, s, e, w 
        Other valid commands: get [item], take [item], drop [item]
        
        """)
        return current_room


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


def handle_action(item, player):
    if item[0] == 'getItem':
        player.current_room.item_list = [i.name if i.name == item[1] else i  for i in player.current_room.item_list]
        player.current_room.item_list = [True if i == item[1] else i  for i in player.current_room.item_list]              
        player.current_room.item_list.remove(True)
        player.inventory_list.append(Item(item[1]))
        print(f"\n**You picked up the {item[1]}!**\n It's now in your inventory.\n Try i or inventory to see your current inventory.\n")
    elif item[0] == 'dropItem':
        player.inventory_list = [i.name if i.name == item[1] else i  for i in player.inventory_list]
        player.inventory_list = [True if i == item[1] else i  for i in player.inventory_list]              
        player.inventory_list.remove(True)
        player.current_room.item_list.append(Item(item[1]))
        print(f"\n**You dropped your {item[1]}!**\n")