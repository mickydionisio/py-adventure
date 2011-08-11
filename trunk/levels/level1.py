######
#
# Example level file
#
######

from advObjects import *

# Initialize Rooms
bedroom = Room("bedroom")
hall = Room("hall")
livingroom = Room("livingroom")
den = Room("den")
kitchen = Room("kitchen")
yard = Room("yard")
corner = Room("corner")
bus = Room("bus")

# declare Items
pencil = Item("PENCIL")
pencil.use = "You stab yourself in the eye with the PENCIL! Why would you do that?!?"

calc = Item("CALCULATOR")
calc.use = "You just figured up some awesome math!  Too bad this was only a one time use calculator..."

skittle  = Item("SKITTLE")
skittle.use = "You ate the skittle... Mmmm Purple!"

coat = Item("COAT")
coat.equip = True
coat.use = "You put on the coat... That should keep you warm!"

dollar = Item("DOLLAR")
dollar.useRoom = bus
dollar.wrongUse = "You should hang on to this DOLLAR for now. You might need it later (hint, hint)"
dollar.use = "The bus driver happily accepts your dollar, and will take off as soon as you find your SEAT."

dictionary = Item("DICTIONARY")
#dictionary.useRoom = livingroom
#dictionary.wrongUse = "You don't need to look up any words right now."
dictionary.use = "As you open the dictionary, a DOLLAR bill falls to the floor. Free money, sweet! You put down the dictionary and pickup the DOLLAR."
dictionary.trade = dollar

coffee = Item("COFFEE")
coffee.use = "Mmm... Caffeine..."

nickel = Item("NICKEL")
nickel.useRoom = corner
nickel.wrongUse = "You should save this nickel 'til you really need it."
nickel.use = "You purchased a hot mug of COFFEE!  What a great deal!"
nickel.trade = coffee

knife = Item("KNIFE")
knife.useRoom = bedroom
knife.wrongUse = "There is nothing to cut here."
knife.use = "Yeah, cut that shit!"

pipe = Item("PIPE")
pipe.use = "Smoking is bad for you!"

button = Item("BUTTON")
button.use = "What did you expect a button to do?"



######
# vObjects
######

desk = VObject("DESK")
desk.description = "There is a PENCIL, a CALCULATOR, and a SKITTLE on the desk."

coatrack = VObject("COATRACK")
coatrack.description = "There is a heavy winter COAT on the COATRACK."

bookshelf = VObject("BOOKSHELF")
bookshelf.description = "There are dozens of books... A large, red DICTIONARY on the 3rd shelf catches your eye."

coffeetable = VObject("COFFEETABLE")
coffeetable.description = "There is nothing of interest on the COFFEETABLE"

sofa = VObject("SOFA")
sofa.description = "The SOFA looks comfortable, but you have no time to sit down right now."

box = VObject("BOX")
box.description = "A shiny new NICKEL is resting atop the junk-filled box"

snowman = VObject("SNOWMAN")
snowman.description = "...with a corncob PIPE and a BUTTON nose..."

coffeeStand = VObject("COFFEE-STAND")
coffeeStand.description = "The sign reads: '5 cents per mug'"

busSeat = VObject("SEAT")
busSeat.description = "Right up front, and looks very comfortable. Type SIT to rest your rump."



# NPCs ... currently not being used

CoffeeGirl = NPC("GIRL")
	#print Victor.sayHello()
	#print Victor.health
	

######
# Setup Rooms
######

# Starting Room 
# Bedroom properties
bedroom.description = "You are in your bedroom2.  There is a door to the EAST, piles of dirty clothes, and a DESK with random stuff on it."
bedroom.item = [pencil, calc, skittle]
bedroom.vObject = [desk]
bedroom.door = [0,0,1,0]
#bedroom.connect[Direc.E] = hall
bedroom.connect = [None, None, hall, None]

# Living Room properties
livingroom.description = "You have entered the Living Room.  The BOOKSHELF contains many books.  There is a SOFA and a COFFEETABLE.  The door to the SOUTH will take you back to the HALL."
livingroom.item = [dictionary]
livingroom.vObject = [bookshelf, coffeetable, sofa]
livingroom.door = [0,1,0,0]
#livingroom.connect[Direc.S] = hall
livingroom.connect = [None, hall, None, None]

# Den properties
den.description = "Welcome to your DEN.  The TV is showing an old episode of Family Guy.  You can see a BOX in the corner that is filled with goodies. NORTH goes back to the hall, WEST leads to the kitchen, and EAST goes outside."
den.item = [nickel]
den.vObject = [box]
den.door = [1,0,1,1]
#den.connect[Direc.N] = hall
den.connect = [hall, None, yard, kitchen]

# Hall properties
hall.description = "You have entered the hall.  A softly glowing lamp illuminates a COATRACK.  There are doors to the NORTH, SOUTH, and WEST."
hall.item = [coat]
hall.vObject = [coatrack]
hall.door = [1,1,0,1]
hall.connect = [livingroom, den, None, bedroom]
#hall.connect[Direc.N] = livingroom 
#hall.connect[Direc.S] = den
#hall.connect[Direc.W] = bedroom

# Kitchen properties
kitchen.description = "You are in the kitchen.  There is a shiny new KNIFE on the counter."
kitchen.item = [knife]
kitchen.door = [0,0,1,0]
kitchen.connect = [None, None, den, None]

# Yard properties
yard.description = "You have stepped outside, to your front yard.  There is good sized SNOWMAN"
yard.item = [pipe, button]
yard.vObject = [snowman]
yard.door = [1,0,0,1]
yard.connect = [corner, None, None, den]
yard.required = coat

# Corner properties
corner.description = "You have walked up to the corner of the block. A little GIRL is running a COFFEE-STAND.  A bus is idling to the EAST"
corner.item = []
corner.npc = [CoffeeGirl]
corner.vObject = [coffeeStand]
corner.door = [0,1,1,0]
corner.connect = [None, yard, bus, None]

# Bus properties
bus.description = "You are on the bus.  The driver says it costs one DOLLAR to ride."
bus.item = []
bus.npc = [CoffeeGirl]
bus.vObject = [busSeat]
bus.door = [0,0,0,1]
bus.connect = [None, None, None, corner]


# add all the stuff to lev
lev = Level(1)

lev.room = [bedroom, hall, livingroom, den, kitchen, yard, corner, bus]
lev.item = [pencil, calc, skittle, coat, dollar, dictionary, coffee, nickel, knife, pipe, button]
lev.vObject = [desk, coatrack, bookshelf, coffeetable, sofa, box, snowman, coffeeStand, busSeat]

# set startroom
lev.startRoom = yard






