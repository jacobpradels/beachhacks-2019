from expression import detect_faces


emotionData = []
emotionData.append(detect_faces("anger2.jpg"))
print(emotionData[0].anger,emotionData[0].joy,emotionData[0].surprise)

# while True:
#     emotion = detect_faces("anger2.jpg")
#     emotionData.append(emotion)

