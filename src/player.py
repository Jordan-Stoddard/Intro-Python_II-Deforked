# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_room, name, inventory_list):
        self.current_room = current_room
        self.name = name
        self.inventory_list = inventory_list

    def __str__(self):
        return f"Player name: {self.name}, Current room: {self.current_room}, Inventory: {self.inventory_list}"