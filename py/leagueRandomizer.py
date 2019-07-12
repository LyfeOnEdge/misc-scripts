##leagueRandomizer.py
##picks a random gamemode in league to play
##Copyright LyfeOnEdge (Andrew) 2019
import random

mode_list = [
"5v5",
"aram",
"tft",
#"3v3",
#"rotating gamemode",
]

choice = random.randint(0,len(mode_list)-1)
print(mode_list[choice])
