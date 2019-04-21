from googleface import detect_faces
from screenshot import take_a_pic
from calculatesalt import determineSalt
from switch import switch
import time
emotionData = []

'''
This function updates the displayimg.png in /current-img/
'''
def switchBar(emotionInfo):
    path2 = "C:\\Users\\Jake\\Documents\\beachhacks2019\\googlecloudapi\\beachhacks-2019\\current-img"
    switch(r"C:\Users\Jake\Documents\beachhacks2019\googlecloudapi\beachhacks-2019\img-src\%d.png"%int(emotionInfo[0]*2),path2, "display0.png")
    switch(r"C:\Users\Jake\Documents\beachhacks2019\googlecloudapi\beachhacks-2019\img-src\%d.png"%int(emotionInfo[1]),path2, "display1.png")
    switch(r"C:\Users\Jake\Documents\beachhacks2019\googlecloudapi\beachhacks-2019\img-src\%d.png"%int(emotionInfo[2]*2),path2, "display2.png")

def main():
    take_a_pic()
    try:
        emotionInfo = []
        frame = detect_faces("frame0.jpg")

        for people in frame:
            emotionData.append(people)
        print(len(emotionData))
        for g in emotionData:
            print(g.anger,g.joy,g.surprise)
            emotionInfo = determineSalt(emotionData)
            print(emotionInfo)
        switchBar(emotionInfo)
    except FileExistsError:
        print('no faces')
    

while True:
    main()
