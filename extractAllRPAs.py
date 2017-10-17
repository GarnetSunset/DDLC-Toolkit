import glob, os

owd = os.getcwd()
unrpaDir = owd + "/unrpa/unrpa.py"

if os.path.exists(owd + "/DDLC/game/audio.rpa"):
    os.system(unrpaDir + " " + owd + "/DDLC/game/audio.rpa")
    os.system(unrpaDir + " " + owd + "/DDLC/game/fonts.rpa")
    os.system(unrpaDir + " " + owd + "/DDLC/game/images.rpa")
    os.system(unrpaDir + " " + owd + "/DDLC/game/scripts.rpa")
else:
    print("Already Extracted Nerd!")
