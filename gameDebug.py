import traceback

try:
    from game import *
	
except:
    #import traceback
    txt = traceback.format_exc()
	raw_input(">>")