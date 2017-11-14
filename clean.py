from distutils import dir_util
import os

owd = os.getcwd()

if not os.path.isdir(owd+"/DDLCModded/"):
    dir_util.remove_tree(owd+"/DDLCModded/")

    print("Done Cleaning!")    

else:
    print("It's Clean!") 
