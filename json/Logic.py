import json
import os
import random

# Get the directory of the current script
script_directory = os.path.dirname(os.path.realpath(__file__))

# Set the working directory to the script's directory
os.chdir(script_directory)



key=1
wordList=[]
wordCount = 0
genders=["Fem","Masc","Neut"]

fileDecs = 'NounDeclensions.json'
with open(fileDecs, 'r',encoding='utf-8') as k:
    dataDecs = json.load(k)

while key<6:
    filename = 'NounDeclension'+str(key)+'.json'
    with open(filename, 'r',encoding='utf-8') as k:
        data = json.load(k)
    for k in range(3):
        for i in data[genders[k]]:
            for j in range(data[genders[k]][i]["weight"]*dataDecs["Declension"+str(key)]):
                wordList.append([])
                wordList[wordCount].append(i)
                wordList[wordCount].append(genders[k])
                wordList[wordCount].append(key)
                wordCount+=1
    key+=1
chosenWord=random.choice(wordList)
caseNoun =[]
cases= ["nom","acc","gen","dat","abl"]
for l in range(len(cases)):
    for m in range(data[cases[l]]):
        caseNoun.append(cases[l])
chosenCase =random.choice(caseNoun)

plurality =[]
pluralOptions = ["sing","plur"]
for n in range(2):
    for o in range(data[pluralOptions[n]]):
        plurality.append(pluralOptions[n])
chosenPlural =random.choice(plurality)

filename = 'NounDeclension'+str(chosenWord[2])+'.json'
with open(filename, 'r',encoding='utf-8') as k:
        data = json.load(k)

print(data[chosenWord[1]][chosenWord[0]][chosenCase][chosenPlural])

# print(wordList)
# print(chosenWord)

