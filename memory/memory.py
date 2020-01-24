
pressedButton = {}
buttonLocation = {}
#                                                                                        STAGE 1
print("Stage 1: ")
print("Input the lower numbers (eg. 2134):")
lowerNumbers = input()
print("Input the top number (eg. 3)")
topNumber = input()
if int(topNumber) == 1:
    print("Press", list(lowerNumbers)[1])
    pressedButton['stage1'] = list(lowerNumbers)[1]
    buttonLocation['stage1'] = 2
elif int(topNumber) == 2:
    print("Press", list(lowerNumbers)[1])
    pressedButton['stage1'] = list(lowerNumbers)[1]
    buttonLocation['stage1'] = 2
elif int(topNumber) == 3:
    print("Press", list(lowerNumbers)[2])
    pressedButton['stage1'] = list(lowerNumbers)[2]
    buttonLocation['stage1'] = 3
elif int(topNumber) == 4:
    print("Press", list(lowerNumbers)[3])
    pressedButton['stage1'] = list(lowerNumbers)[3]
    buttonLocation['stage1'] = 4
#print("Current button history", pressedButton, "Location: ",buttonLocation)
#                                                                                       STAGE 2
print("Stage 2: ")
print("Input the lower numbers (eg. 2134):")
lowerNumbers = input()
print("Input the top number (eg. 3)")
topNumber = input()
if int(topNumber) == 1:
    print("Press", 4)
    pressedButton['stage2'] = 4
    buttonLocation['stage2'] = lowerNumbers.index("4")+1
elif int(topNumber) == 2:
    location = buttonLocation.get("stage1")
    button = lowerNumbers.index(str(location-1))
    print("Press", button)
    pressedButton['stage2'] = list(lowerNumbers)[1]
    buttonLocation['stage2'] = location
elif int(topNumber) == 3:
    print("Press", list(lowerNumbers)[0])
    pressedButton['stage1'] = list(lowerNumbers)[0]
    buttonLocation['stage1'] = 1
elif int(topNumber) == 4:
    location = buttonLocation.get("stage1")
    button = lowerNumbers.index(str(location - 1))
    print("Press", button)
    pressedButton['stage2'] = list(lowerNumbers)[1]
    buttonLocation['stage2'] = location
#print("Current button history", pressedButton, "Location: ", buttonLocation)
#                                                                                       STAGE 3
print("Stage 3: ")
print("Input the lower numbers (eg. 2134):")
lowerNumbers = input()
print("Input the top number (eg. 3)")
topNumber = input()
if int(topNumber) == 1:
    index = lowerNumbers.index(str(pressedButton.get("stage2")))
    label = list(lowerNumbers)[index]
    print("Press", label)
    pressedButton['stage3'] = list(lowerNumbers)[lowerNumbers.index(label)]
    buttonLocation['stage3'] = lowerNumbers.index(label)+1
elif int(topNumber) == 2:
    index = lowerNumbers.index(str(pressedButton.get("stage1")))
    label = list(lowerNumbers)[index]
    print("Press", label)
    pressedButton['stage3'] = list(lowerNumbers)[lowerNumbers.index(label)]
    buttonLocation['stage3'] = lowerNumbers.index(label) + 1
elif int(topNumber) == 3:
    print("Press", list(lowerNumbers)[2])
    pressedButton['stage3'] = list(lowerNumbers)[2]
    buttonLocation['stage3'] = 3
elif int(topNumber) == 4:
    print("Press", 4)
    pressedButton['stage3'] = 4
    buttonLocation['stage3'] = lowerNumbers.index("4") + 1
#print("Current button history", pressedButton, "Location: ", buttonLocation)
#                                                                                       STAGE 4
print("Stage 4: ")
print("Input the lower numbers (eg. 2134):")
lowerNumbers = input()
print("Input the top number (eg. 3)")
topNumber = input()
if int(topNumber) == 1:
    location = buttonLocation.get("stage1")
    button = lowerNumbers.index(str(location - 1))
    print("Press", button)
    pressedButton['stage4'] = list(lowerNumbers)[1]
    buttonLocation['stage4'] = location
elif int(topNumber) == 2:
    print("Press", list(lowerNumbers)[0])
    pressedButton['stage4'] = list(lowerNumbers)[0]
    buttonLocation['stage4'] = 2
elif int(topNumber) == 3:
    location = buttonLocation.get("stage2")
    button = lowerNumbers.index(str(location - 1))
    print("Press", button)
    pressedButton['stage4'] = list(lowerNumbers)[1]
    buttonLocation['stage4'] = location
elif int(topNumber) == 4:
    location = buttonLocation.get("stage2")
    button = lowerNumbers.index(str(location - 1))
    print("Press", button)
    pressedButton['stage4'] = list(lowerNumbers)[1]
    buttonLocation['stage4'] = location
#print("Current button history", pressedButton, "Location: ", buttonLocation)
#                                                                                       STAGE 5
print("Stage 4: ")
print("Input the lower numbers (eg. 2134):")
lowerNumbers = input()
print("Input the top number (eg. 3)")
topNumber = input()
if int(topNumber) == 1:
    index = lowerNumbers.index(str(pressedButton.get("stage1")))
    label = list(lowerNumbers)[index]
    print("Press", label)
    pressedButton['stage5'] = list(lowerNumbers)[lowerNumbers.index(label)]
    buttonLocation['stage5'] = lowerNumbers.index(label)+1
elif int(topNumber) == 2:
    index = lowerNumbers.index(str(pressedButton.get("stage2")))
    label = list(lowerNumbers)[index]
    print("Press", label)
    pressedButton['stage5'] = list(lowerNumbers)[lowerNumbers.index(label)]
    buttonLocation['stage5'] = lowerNumbers.index(label) + 1
elif int(topNumber) == 3:
    index = lowerNumbers.index(str(pressedButton.get("stage4")))
    label = list(lowerNumbers)[index]
    print("Press", label)
    pressedButton['stage5'] = list(lowerNumbers)[lowerNumbers.index(label)]
    buttonLocation['stage5'] = lowerNumbers.index(label) + 1
elif int(topNumber) == 4:
    index = lowerNumbers.index(str(pressedButton.get("stage3")))
    label = list(lowerNumbers)[index]
    print("Press", label)
    pressedButton['stage5'] = list(lowerNumbers)[lowerNumbers.index(label)]
    buttonLocation['stage5'] = lowerNumbers.index(label) + 1
#print("Current button history", pressedButton, "Location: ", buttonLocation)