from six.moves.urllib.request import urlopen
import glob, os, re, shutil, time

owd = os.getcwd()
unrpaDir = owd + "/unrpa/unrpa.py"

if os.path.exists(owd + "/DDLC/game/audio.rpa"):
    os.chdir(owd + "/DDLC/game/")
    os.system(unrpaDir + " " + owd + "/DDLC/game/audio.rpa")
    os.rename(owd + "/DDLC/game/audio.rpa",owd + "/DDLC/game/audioBKP.rpa")
    os.system(unrpaDir + " " + owd + "/DDLC/game/fonts.rpa")
    os.rename(owd + "/DDLC/game/fonts.rpa",owd + "/DDLC/game/fontsBKP.rpa")
    os.system(unrpaDir + " " + owd + "/DDLC/game/images.rpa")
    os.rename(owd + "/DDLC/game/images.rpa",owd + "/DDLC/game/imagesBKP.rpa")
    os.system(unrpaDir + " " + owd + "/DDLC/game/scripts.rpa")
    os.rename(owd + "/DDLC/game/scripts.rpa",owd + "/DDLC/game/scriptsBKP.rpa")
    for filename in os.listdir("."):
        if filename.startswith("game_00"):
            so.remove(filename)
        if filename.startswith("game_"):
            newName = re.sub('game_', '', filename)
            newName = re.sub('.txt', '', newName)
            shutil.move(owd + "/DDLC/game/" + filename, owd + "/DDLC/game/" + newName)
else:
    print("Already Extracted Nerd!")
