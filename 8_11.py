from random import *
seed("ghfdjryfdhrfewjd")

alph = 'abcdefghijklmnopqrstuvwxyz'

surnameList = []
for i in range(0,20):
    s = 0
    e = randint(4,7)
    surnameList.append('')
    while s < e:
        surnameList[i] += (choice(alph))
        s += 1

# surnameList = ["ab","ac","aa","da"]

# print(randint(1,15)) ### 11 ### 11 ### 11 ### 11 ### 11 ### 11 ### 11 ### 11 ### 11 ### 11 ###

swap = True
i = 0
currentLetter = 0
print(surnameList)

j = 0
while True:
    noSwap = True
    for i in range(0,len(surnameList)-1):
        currentLetter = 0
        cycle = 0
        while True:
            cycle +=1
            if alph.find(surnameList[i][currentLetter]) > alph.find(surnameList[i+1][currentLetter]):
                surnameList[i],surnameList[i+1] = surnameList[i+1],surnameList[i]
                noSwap = False
                break

            elif surnameList[i][currentLetter] == surnameList[i+1][currentLetter]:
                currentLetter += 1
            elif cycle > 10: ### STUPID HACK :SOB:
                break

    j += 1
    if noSwap:
        break

print(surnameList)