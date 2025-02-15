from location import LocationBase, talking_island
class Character:
	def __init__(self,name):
		self.name = name
		self.lvl = 80
		self.gear = {}
		self.inventory = {"Adena": 100000}
		self.location = talking_island
		self.profession = "Duelist"

	def __repr__(self):
		return (f"{self.name} | {self.profession}\n"
		        f"Inventory: {self.inventory}\n{self.location}\n")

	def move(self,new_location):
		print(f"{self.name} teleported to {new_location}.")
		if "Adena" in self.inventory:
			self.inventory["Adena"] -= 5000

	def attack(self,monster):
		pass

	def use_item(self,item):
		pass

	def buy_item(self,item):
		pass
	#	if self.location == town and npc.can_sell(item):
	#		self.inventory.append(item)

	def sell_item(self,item):
		pass
char = Character("AnimalPK")
print(char)