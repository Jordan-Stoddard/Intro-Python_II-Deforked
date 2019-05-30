# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, item_list):
        self.name = name
        self.description = description
        self.item_list = item_list

    def __str__(self):
        item_list = self.item_list
        item_list = [i.name  for i in item_list]
        return f"\n-----------------\n{self.name}\n{self.description}\nItems in this room: {', '.join(item_list)}"