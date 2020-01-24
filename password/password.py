words = []
file = open("words.txt","r")
for line in file:
    nl = line.rstrip()
    words.append(nl)
print(words)

words2 = []
words3 = []
words4 = []
words5 = []
words6 = []
print("Insert first row letters: (asdfse)")
row1 = input("First row:")
for i in words:
    for j in list(row1):
        if list(i)[0] == j:
            words2.append(i)
print(words2)
row2 = input("Second row:")
for i in words2:
    for j in list(row2):
        if list(i)[1] == j:
            words3.append(i)
print(words3)
row3 = input("Third row:")
for i in words3:
    for j in list(row3):
        if list(i)[2] == j:
            words4.append(i)
print(words4)
row4 = input("Fourth row:")
for i in words4:
    for j in list(row4):
        if list(i)[3] == j:
            words5.append(i)
print(words5)
row5 = input("Fifth row:")
for i in words5:
    for j in list(row5):
        if list(i)[4] == j:
            words6.append(i)
print(words6)
if len(words6) == 1:
    print(f"**********************    WORD IS:       {words6}                ************************")
else:
    print("no word found you suck lol kys xd")