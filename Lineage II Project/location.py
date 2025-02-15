import random
from character import Character
class Coordinates:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"(x:{self.x} | y:{self.y})"

class LocationBase:
    def __init__(self, name: str, coordinates: Coordinates):
        self.name = name
        self.coordinates = coordinates

    def __repr__(self):
        return f"LocationBase(name='{self.name}', coordinates={self.coordinates})"

class Town(LocationBase):
	def __init__(self,name,coordinates,farming_zones):
		super().__init__(name,coordinates)
		self.farming_zones = farming_zones

	def __repr__(self):
			return f"Location: {self.name} {self.coordinates}\nFarming Zones:\n{farming_zones}"

class FarmingZone(LocationBase):
	def __init__(self,name,coordinates,monsters):
		super().__init__(name,coordinates)
		self.monsters = monsters

	def __repr__(self):
		return f"{self.name} {self.coordinates}\nMonsters: {self.monsters}\n"
# Coordinates
giran_coordinates = Coordinates(22, 22)
talking_island_coordinates = Coordinates(17,25)
loa_coordinates = Coordinates(20, 26)
dv_north_coordinates = Coordinates(20, 24)
dv_south_coordinates = Coordinates(20, 28)
#Monsters

# Farming Zones
farming_zones = FarmingZone
loa = FarmingZone(" Lair of Antharas",loa_coordinates,[])
dv_north = FarmingZone(" Dragon Valley-North",dv_north_coordinates,[])
dv_south = FarmingZone(" Dragon Valley-South",dv_south_coordinates,[])
farming_zones_giran = [loa,dv_north,dv_south]
# Town
giran = Town("Giran Town",giran_coordinates,[loa,dv_north,dv_south])
#print(giran)
talking_island = Town("Talking Island Village",talking_island_coordinates,[])























