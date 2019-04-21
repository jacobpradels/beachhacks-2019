from googleface import detect_faces
from screenshot import take_a_pic
from calculatesalt import determineSalt
from switch import switch
from twitchBot import POGGERS
import time
import os

emotionData = []
prevEmotion = [0, 0, 0]
'''
This function updates the displayimg.gif in /current-img/
'''


def switchBar(emotionInfo):
    path2 = r"C:\Users\Jake\Documents\beachhacks2019\googlecloudapi\beachhacks-2019"
    os.system("cd "+ path2)
    if (emotionInfo[0] != prevEmotion[0]):
        switch(r"%d" % round(emotionInfo[0]), path2, "display0")

        prevEmotion[0] = emotionInfo[0]
    if (emotionInfo[1] != prevEmotion[1]):
        switch(r"%d" % round(emotionInfo[1]), path2, "display1")

        prevEmotion[1] = emotionInfo[1]

    if (emotionInfo[2] != prevEmotion[2]):
        switch(r"%d" % round(emotionInfo[2]), path2, "display2")

        prevEmotion[2] = emotionInfo[2]
    # os.system("cd " + path2)
    # switch(r"%d"%round(emotionInfo[0]), path2, "display0")
    # switch(r"%d"%round(emotionInfo[1]), path2, "display1")
    # switch(r"%d"%round(emotionInfo[2]), path2, "display2")


# def botSelection(emotionInfo):
# if (emotionInfo[1] > 2):
# POGGERS()

def main():
    take_a_pic()
    try:
        emotionInfo = []
        # detect faces returns a list of the face objects
        frame = detect_faces("frame0.jpg")

        # This loop is to seperate the list of faces and add them one by one into the list of emotion data
        for people in frame:
            # if (len(emotionData) >= 10):
            #     emotionData.append(people)
            #     emotionData.pop(0)
            # else:
            emotionData.append(people)
        # Prints the total amount of faces we have in our data
        # print(len(emotionData))
        # Goes through every face and calculates its data
        for g in emotionData:
            # print(g.anger,g.joy,g.surprise)
            # Determine salt returns a list in the form [angervalue, joyvalue, surprisevalue]
            emotionInfo = determineSalt(emotionData)
        print(emotionInfo)
        # This function updates all of the gauges for emotions
        try:
            switchBar(emotionInfo)
            # botSelection(emotionInfo)
        except IndexError:
            print('list empty')
    except FileExistsError:
        print('no faces')


while (True):
    main()