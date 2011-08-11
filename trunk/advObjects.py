######
#
# Class definitions for all game objects
#
######

# superclass for all adventure game objects
class BaseObject:
	def __init__(self, nme):
		self.name = nme

# standard item
class Item(BaseObject):
	qty = 0
	use = ''
	wrongUse = ''
	useRoom = None
	equip = False
	trade = None
	
# Viewable Object Class
class VObject(BaseObject):
	description = ''

# base room class
class Room(BaseObject):
	description = ''
	item = []
	vObject = []
	door = [0,0,0,0]
	connect = [None, None, None, None]
	required = None
	npc = []
	def View(self, objectName):
		# Check room's vObjects
		for vObj in self.vObject:
			if(vObj.name == objectName):
				return vObj.description
		# if it doesn't find one
		return "There is no " + objectName + " in here..."
	
	def Pickup(self, itemName):
		for itm in self.item:
			if(itm.name == itemName):
				self.item.remove(itm)
				return itm
		# if it doesn't find one
		return None

# Movement Direction Enum
from tools.enum import enum
Direc = enum('N', 'S', 'E', 'W')

class Level:
	def __init__(self, idx):
		self.num = idx
		
	room = []
	item = []
	vObject = []
	startRoom = None
			
# character superclass
class Character(BaseObject):
	health = 3

class NPC(Character):
	def sayHello(self):
		return self.name + " says 'HELLO'"

	
class Player(Character):
	inventory = []
	equipment = []
	def Pickup(self, item):
		self.inventory.append(item)
	def Use(self, itemName, curRoom):
		itemExists = 0
		for itm in self.inventory:
			if(itm.name == itemName):
				if(itm.equip):
					self.equipment.append(itm)
				# Check if player is in correct room for item's use
				elif(itm.useRoom != curRoom and itm.useRoom != None):
					return itm.wrongUse
				elif(itm.trade != None):
					self.inventory.append(itm.trade)
				
				self.inventory.remove(itm)
				return itm.use
					
				#else:
					#print "You cannot use that right now"
		return "There is no " + itemName + " in your inventory..."
		