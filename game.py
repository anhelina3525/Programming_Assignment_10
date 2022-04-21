"""
Programming Assignment 4. A quest game.
Includes classes: Room, Character, Enemy,
Friend, Item.
"""


class Room:
    """
    A class for room.
    """

    def __init__(self, room_type):
        """
        Initializes the class object.
        """
        self.room_type = room_type
        self.linked_rooms = {}
        self.character = None
        self.description = ''
        self.item = None

    def __str__(self):
        """
        Gives the string representation of a Room object.
        """
        return self.room_type

    def set_description(self, description):
        """
        Sets a description to the object.
        """
        self.description += description

    def link_room(self, other, side):
        """
        Links the rooms.
        """
        self.linked_rooms[side] = other

    def set_character(self, character):
        """
        Sets the character in the room.
        """
        self.character = character

    def set_item(self, item):
        """
        Sets the item in the room.
        """
        self.item = item

    def get_details(self):
        """
        Prints out details about a room object.
        """
        room = "{}\n--------------------\n{}".format(
            self.room_type, self.description)
        around = ''
        for i in self.linked_rooms.keys():
            around += '\nThe {} is {}'.format(self.linked_rooms[i], i)
        print(room+around)

    def get_character(self):
        """
        Returns the character.
        """
        return self.character

    def get_item(self):
        """
        Returns the item.
        """
        return self.item

    def move(self, direction):
        """
        Changes the character's location to a different room.
        """
        try:
            return self.linked_rooms[direction]
        except KeyError:
            print('There is no room to the {} of {}'.format(
                direction, self.room_type))


class Character:
    """
    A class for Character.
    """

    def __init__(self, name, description):
        """
        Initializes the class object.
        """
        self.name = name
        self.description = description

    def describe(self):
        """
        Prints out the description of the class object.
        """
        print('{} is here!\n{}'.format(self.name, self.description))


class Enemy(Character):
    """
    A class for Enemy. Inherits from
    the Character class.
    """
    defeats = 0

    def __init__(self, name, description):
        """
        Initializes the class object.
        """
        super().__init__(name, description)
        self.weakness = ''
        self.convo = []

    def set_conversation(self, replica):
        """
        Sets the conversation.
        """
        self.convo.append(replica)

    def set_weakness(self, weakness):
        """
        Sets the weakness of an enemy.
        """
        self.weakness += weakness

    def talk(self):
        """
        Prints out the enemy's replicas.
        """
        print("[{} says]: {}".format(self.name, self.convo[0]))

    def fight(self, fight_with):
        """
        Fights the enemy. Returns True
        if the enemy is defeated, returns
        False otherwise.
        """
        if self.weakness == fight_with:
            Enemy.defeats += 1
            return True
        return False

    def get_defeated(self):
        """
        Returns the number of defeats
        that all representatives of the
        Enemy class had.
        """
        return Enemy.defeats


class Friend(Character):
    """
    A class for Friend. Inherits
    from the class Character.
    """
    pass


class Item:
    """
    A class for Item.
    """

    def __init__(self, name):
        """
        Initializes the class object.
        """
        self.name = name
        self.description = ''

    def set_description(self, descr):
        """
        Sets the description to an item.
        """
        self.description += descr

    def describe(self):
        """
        Prints out the description of
        an item.
        """
        print('The [{}] is here - {}'.format(self.name, self.description))

    def get_name(self):
        """
        Returns the name of an item.
        """
        return self.name
