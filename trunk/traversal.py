######
#
# Traversal Functions
#
######

from advObjects import *
import shared

def enter(theRoom):
	#global currentRoom
	shared.currentRoom = theRoom
	
	print "-----"
	print shared.currentRoom.description
	return 0
	
	
def Go(direction):
	if(direction == "NORTH"):
		curDirec = Direc.N
		
	elif(direction == "SOUTH"):
		curDirec = Direc.S

	elif(direction == "EAST"):
		curDirec = Direc.E
		
	elif(direction == "WEST"):
		curDirec = Direc.W
	
	else: 
		print direction + " is not a direction"
		return 0
	
	if(shared.currentRoom.door[curDirec] != 0):
		if(shared.currentRoom.connect[curDirec].required != None):
			# make sure player has something equipped
			if(shared.player.equipment == []):
				print "You should equip the " + shared.currentRoom.connect[curDirec].required.name
				return 0
			# loop through equipped items	
			for eqp in shared.player.equipment:
				if(eqp.name == shared.currentRoom.connect[curDirec].required.name):
					print ''
				else:
					print "You should equip the " + shared.currentRoom.connect[curDirec].required.name
					return 0
					
		print "You went " + direction
		enter(shared.currentRoom.connect[curDirec])
	else:
		print "You cannot go " + direction
	


