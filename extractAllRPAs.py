from six.moves.urllib.request import urlopen
import glob, os, re, shutil, sys, time

owd = os.getcwd()
if sys.version_info <= (3, 0):
    unrpaDir = owd + "/unrpa2/unrpa.py"
if sys.version_info >= (3, 0):
    unrpaDir = owd + "/unrpa/unrpa"

if os.path.exists(owd + "/DDLC/game/audio.rpa"):
    os.chdir(owd + "/DDLC/game/")
    os.system("python " + unrpaDir + " " + owd + "/DDLC/game/audio.rpa")
    os.remove(owd + "/DDLC/game/audio.rpa")
    os.system("python " + unrpaDir + " " + owd + "/DDLC/game/fonts.rpa")
    os.remove(owd + "/DDLC/game/fonts.rpa")
    os.system("python " + unrpaDir + " " + owd + "/DDLC/game/images.rpa")
    os.remove(owd + "/DDLC/game/images.rpa")
    os.system("python " + unrpaDir + " " + owd + "/DDLC/game/scripts.rpa")
    os.remove(owd + "/DDLC/game/scripts.rpa")
else:
    print("Already Extracted Nerd!")
