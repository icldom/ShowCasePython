from character import Character
from location import Town, FarmingZone
from monster import Monster
from item import Item
from NPC import NPC

# Initialize your game components here
def main():
    hero = Character("Arthur", 100)
    town = Town("Village of Beginnings")
    farm_zone = FarmingZone("Green Meadows")
    monster = Monster("Goblin", 30)
    item = Item("Health Potion", "Restores 50 HP", 10)
    vendor = Vendor("Blacksmith", [item])

    # Game logic goes here

if __name__ == "__main__":
    main()
