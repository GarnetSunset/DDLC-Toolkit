from distutils import dir_util
import os

owd = os.getcwd()

if not os.path.isdir(owd+"/DDLCModded/"):
    os.makedirs(owd+"/DDLCModded/")
    dir_util.copy_tree(owd+"/DDLC/",owd+"/DDLCModded/")

dir_util.copy_tree(owd+"/edits/",owd+"/DDLCModded/game/")

print("Done Merging!")
