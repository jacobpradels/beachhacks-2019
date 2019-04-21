def determineSalt(arrayList):
    import time
    angerLevel = 0
    joyLevel = 0
    surpriseLevel = 0
    angerList = []
    joyList = []
    surpriseList = []
    for x in arrayList:
        angerList.append(x.anger-1)
    for x in arrayList:
        joyList.append(x.joy-1)
    for x in arrayList:
        surpriseList.append(x.surprise-1)
    angerLevel = sum(angerList)/len(angerList)
    joyLevel = sum(joyList)/len(joyList)
    surpriseLevel = sum(surpriseList)/len(surpriseList)
    return [angerLevel, joyLevel, surpriseLevel]
