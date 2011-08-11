######
#
# Initialize Game
#
######

# Import modules
import string

from advObjects import *
from levels import *
from traversal import *

# import levels.level0
import shared
		
## Welcome / Intro
print "What is your name?"
shared.player.name = raw_input(">>")
print "-----"
print "Welcome " + shared.player.name + "!"


# Initialize Levels & starting point
lev = [level0.lev0, level1.lev1]
curLevel = 0

enter(lev[curLevel].startRoom)
command = raw_input(">>")

######
# Main Game Loop
# ... listens for commands
######

while True:
	command = string.upper(command)
    
	if "GO " in command:
		# Isolate direction
		command = command.replace("GO ", "")
		print ""
		Go(command)
		print ""
		command = raw_input(">>")
		
	elif "PICKUP " in command:
		# Isolate name of object
		command = command.replace("PICKUP ", "")
		#player.Pickup(command)
		pickupItem = shared.currentRoom.Pickup(command)
		print ""
		if(pickupItem != None):
			shared.player.Pickup(pickupItem)
			print "-----"
			print "Your current inventory:"
			for itm in shared.player.inventory:
				print itm.name
			print "-----"
		
		else:
			print "There is no " + command + " in here..."
		
		print ""
		command = raw_input(">>")
		
	elif "USE " in command:
		command = command.replace("USE ", "")
		print ""
		print shared.player.Use(command, shared.currentRoom)
		print ""
		command = raw_input(">>")
		
	# Viewing is currently room-based
	elif "VIEW " in command:
		command = command.replace("VIEW ", "")
		print ""
		print shared.currentRoom.View(command)
		print ""
		command = raw_input(">>")
		
		
	elif(command == "HELP" or command == "?"):
		print "-----"
		print "Objects you can interact with are written in CAPS."
		print "Common interactions:"
		print "     VIEW: Take a closer look"
		print "     GO: Move to an adjacent room... ie( GO EAST )"
		print "     PICKUP: Adds an item to your inventory"
		print "     USE: Uses an item in your inventory.  Some items are equipped (like a coat or hat).  Others can only be used in a specific area of the game."
		print "     QUIT or Q: Exits the game"
		print "-----"
		command = raw_input(">>")
		
	elif(command == "DEBUG"):
		print "---DEBUG---"
		for eqp in shared.player.equipment:
			print eqp.name
		print "-----"
		command = raw_input(">>")
	
	elif(command == shared.winPhrase[0] and shared.currentRoom.name == shared.winRoom[0]):
		print "-----"
		print "Level Complete!"
		print "-----"
		print ""
		curLevel = curLevel+1
		print "Level " + str(curLevel) + ": " + "the title text, soon to be dynamic"
		print "-----"
		enter(lev[curLevel].startRoom)
		command = raw_input(">>")
	
	elif(command == "FART"):
		print ""
		print "A disgusting belch spews from your butthole..."
		print ""
		command = raw_input(">>")
	
	elif(command == "XYZZY"):
		print ""
		print "What do you think this is, Colossal Adventure?"
		print ""
		command = raw_input(">>")
	
	elif(command == "QUIT" or command == "Q"):
		break
		
	else:
		print ""
		print "Invalid Command!"
		print ""
		command = raw_input(">>")