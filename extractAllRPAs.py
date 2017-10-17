from six.moves.urllib.request import urlopen
import glob, os, re, shutil, time

owd = os.getcwd()
unrpaDir = owd + "/unrpa/unrpa.py"

if os.path.exists(owd + "/DDLC/game/audio.rpa"):
    os.chdir(owd + "/DDLC/game/")
    os.system(unrpaDir + " " + owd + "/DDLC/game/audio.rpa")
    os.remove(owd + "/DDLC/game/audio.rpa")
    os.system(unrpaDir + " " + owd + "/DDLC/game/fonts.rpa")
    os.remove(owd + "/DDLC/game/fonts.rpa")
    os.system(unrpaDir + " " + owd + "/DDLC/game/images.rpa")
    os.remove(owd + "/DDLC/game/images.rpa")
    os.system(unrpaDir + " " + owd + "/DDLC/game/scripts.rpa")
    os.remove(owd + "/DDLC/game/scripts.rpa")
    response = urlopen('https://raw.githubusercontent.com/lolbot-iichan/decompile.rpy/master/decompile.rpy')
    with open("decompile.rpy", "w") as file:
        file.write(response.read())
    os.system(owd + "/DDLC/DDLC.exe")
    time.sleep(10)
    os.system("taskkill /im DDLC.exe")
    for filename in os.listdir("."):
        if filename.startswith("game_00"):
            so.remove(filename)
        if filename.startswith("game_"):
            newName = re.sub('game_', '', filename)
            newName = re.sub('.txt', '', newName)
            shutil.move(owd + "/DDLC/game/" + filename, owd + "/DDLC/game/" + newName)
else:
    print("Already Extracted Nerd!")
