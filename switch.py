import glob
import shutil
import os
from PIL import Image




# path2 = "C:\\Users\\Jake\\Documents\\beachhacks2019\\googlecloudapi\\beachhacks-2019\\current-img"
def switch(displayimg, location, name):
    logo = Image.open(displayimg)
    # logo.save(os.path.join(location,name), save_all=True)
    logo.save(os.path.join(location,name))
