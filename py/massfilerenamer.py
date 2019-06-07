
###HOW TO USE: Replace 'prefix' with the string you wish to replace
###Replace newprefix with the string you would like to replace the old prefix with
###Be careful, leaving prefix or newprefix blank is a bad idea
###This script also crawls subfolders. 
###Be safe, happy renaming
###~~~LyfeOnEdge

#example:
#your files come in format: spongebob season 2 episode 03
#dump format is title_03
#replace ?? with title_03
#replace !! with "spongebob season 2 episode"

prefix = "??"
newprefix = "!!"

import os, sys

def subfiles(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            file = os.path.join(root, name)
            newfile = name.replace(prefix, newprefix)
            newfile = os.path.join(root, newfile)
            os.rename(file,newfile)
            print("Renamed {} to {}".format(file,newfile))

subfiles(sys.path[0])