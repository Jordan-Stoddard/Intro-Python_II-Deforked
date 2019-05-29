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
        print("\n**You can't go that way!** \n Either the map doesn't go that direction or you typed an invalid direction key. \n Direction keys are: n, s, e, w \n")
        return current_room