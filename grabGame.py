from distutils import dir_util
from six.moves.urllib.request import urlopen
import itertools, os, sys, threading, time, zipfile

done = False

if os.path.isfile("DDLC.zip"):
    os.remove("DDLC.zip")

if os.path.isdir("/DDLC/"):
    dir_util.remove_tree("/DDLC/")

def loading():
    for s in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rDownloading... ' + s)
        sys.stdout.flush()
        time.sleep(0.1)

owd = os.getcwd()

response = urlopen('https://download837.mediafire.com/fx6cai2u5xxg/471gl4z7mw0w2un/ddlc-win.zip')

g = threading.Thread(target=loading)
g.start()

f = open("DDLC.zip", 'wb')
f.write(response.read())
f.close()

done = True
print("\nDone DLing... Moving on...")

ddlczip = zipfile.ZipFile("DDLC.zip", 'r')
ddlczip.extractall(owd)
ddlczip.close()

dir_util.copy_tree(owd+"/DDLC-1.0.9-pc/",owd+"/DDLC/")
dir_util.remove_tree(owd+"/DDLC-1.0.9-pc/")

os.remove("DDLC.zip")
