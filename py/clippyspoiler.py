#Licensed under GPL3
###Troll script for discord.
###Puts every letter in your copy/paste clipboard in a spoiler
###Clever cyclic program means that it doesn't care if it has alrady been converted
###Original input -> Converted output -> Identical converted output
###Requires pyperclip (pip install pypercip)

##How to use:
##Set mode below
##Start script with `python clippyspoiler.py`
##Copy with ctrl+c or right-click -> copy
##Text strings will be turned into spoilers automatically
##Paste with ctrl+v or right-click -> paste
##To stop the automatically spoiler exit the script

import sched, time
import pyperclip
words = True  #Don't touch this
chars = False #Don't touch this

#set mode to either words or chars
#chars will spoiler every character
#words will spoiler every word

mode = chars #Change this to 'words' or chars'

s = sched.scheduler(time.time, time.sleep)

def do_something(sc): 
	data = pyperclip.paste()
	data = data.strip().replace("|","")

	newdata = ""
	for w in data:
        if mode == words:
            newdata += "||{}||".format(w)
        else:
    		for c in w:
    			newdata += "||{}||".format(c)

	pyperclip.copy(newdata)
	s.enter(1, 1, do_something, (sc,))

s.enter(1, 1, do_something, (s,))
s.run()

