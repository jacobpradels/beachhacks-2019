
import os
from PIL import Image




# path2 = "C:\\Users\\Jake\\Documents\\beachhacks2019\\googlecloudapi\\beachhacks-2019\\current-img"
def switch(displayimg, location, name):
    logo = Image.open(os.path.join(location,displayimg+".gif"))
    logo.save(os.path.join(location,name+".gif"), save_all=True)
    # logo.save(os.path.join(location,name+"-temp"))
    # logo.close()
    # os.system("cd")
    # print(location)
    # os.system("rename "+"\\"+displayimg+"-temp.gif %s.gif"%name)
    # print("rename "+displayimg+"-temp.gif %s.gif"%name)
    os.system("move "+"%s.gif"%name + " current-img")
    print("move "+"%s.gif"%name + " current-img")
    