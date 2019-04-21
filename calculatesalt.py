def determineSalt(emotionData):
    import time
    angerLevel = 0
    joyLevel = 0
    surpriseLevel = 0
    angerList = []
    joyList = []
    surpriseList = []
    storageTime = 2
    for x in emotionData:
        if (len(angerList) >= storageTime):
            angerList.pop(0)
            angerList.append(x.anger-1)
        else:
            angerList.append(x.anger-1)
    for x in emotionData:
        if (len(joyList) >= storageTime):
            joyList.pop(0)
            joyList.append(x.joy-1)
        else:
            joyList.append(x.joy-1)
    for x in emotionData:
        if (len(surpriseList) >= storageTime):
            surpriseList.pop(0)
            surpriseList.append(x.surprise-1)
        else:
            surpriseList.append(x.surprise-1)
    angerLevel = sum(angerList)/len(angerList)
    joyLevel = sum(joyList)/len(joyList)
    surpriseLevel = sum(surpriseList)/len(surpriseList)
    return [angerLevel, joyLevel, surpriseLevel]
    # return [angerList, joyList, surpriseList]
