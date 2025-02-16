from random import *

seed("ADIAHUDJKFAI")

# print(randint(1,20)) ### 12 ### 12 ### 12 ### 12 ### 12 ###

contents = ''

try:
    file = open("INPUT.txt","r")
    contents = file.readlines()[0].split(",")
    file.close()
except FileNotFoundError:
    print("INPUT.txt not found, try again!!")

if contents != '':
    indexMax = contents.index(max(contents))

    sumPastMax = 0
    for num in contents[indexMax+1:]:
        sumPastMax += int(num)

    currentIndex = 0
    firstNegIndex = 0
    while True:
        if int(contents[currentIndex]) < 0:
            firstNegIndex = currentIndex
            break
        currentIndex += 1

    contents[firstNegIndex] = str(sumPastMax)
    out = ''
    for char in contents:
        out += char + ','
    out = out[:-1]
    file2 = open('OUT.txt','w')
    file2.write(str(out))
    file2.close()

print('OK')
