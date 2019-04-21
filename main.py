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
        #detect faces returns a list of the face objects
        frame = detect_faces("frame0.jpg")

        #This loop is to seperate the list of faces and add them one by one into the list of emotion data
        for people in frame:
            emotionData.append(people)
        #Prints the total amount of faces we have in our data
        print(len(emotionData))
        #Goes through every face and calculates its data
        for g in emotionData:
            print(g.anger,g.joy,g.surprise)
            #Determine salt returns a list in the form [angervalue, joyvalue, surprisevalue]
            emotionInfo = determineSalt(emotionData)
            print(emotionInfo)
        #This function updates all of the gauges for emotions
        switchBar(emotionInfo)
    except FileExistsError:
        print('no faces')
    

while True:
    main()
