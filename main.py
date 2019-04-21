from googleface import detect_faces
from screenshot import take_a_pic
from calculatesalt import determineSalt
import time
emotionData = []

def main():
    take_a_pic()
    try:
        frame = detect_faces("frame0.jpg")
        print(len(emotionData))
        for people in frame:
            emotionData.append(people)
        for g in emotionData:
            print(g.anger,g.joy,g.surprise)
            print(determineSalt(emotionData))
    except FileExistsError:
        print('no faces')

for x in range(3):
    main()
