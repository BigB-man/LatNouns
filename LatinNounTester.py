# Import module 
import tkinter as tk
import json
import os
import random
# Create the main window
root = tk.Tk()
root.title("Latin Noun Tester")
#root.wm_attributes('-transparentcolor','#ab23ff')
root.iconbitmap("images/NounDeclension.ico")

root.geometry("720x480")
genders=["Fem","Masc","Neut"]

cases= ["nom","acc","gen","dat","abl"]
pluralOptions = ["sing","plur"]
print(os. getcwd())
os.chdir("json")
# Create object 
def getLatinWord():
    # Get the directory of the current script
    
    #print(script_directory)


    key=1
    wordList=[]
    wordCount = 0
    
    global chosenWord,chosenCase,chosenPlural, word

    fileDecs = 'NounDeclensions.json'
    with open(fileDecs, 'r',encoding='utf-8') as k:
        dataDecs = json.load(k)

    while key<6:
        filename = 'NounDeclension'+str(key)+'.json'
        with open(filename, 'r',encoding='utf-8') as k:
            data = json.load(k)
        for k in range(3):
            for i in data[genders[k]]:
                for j in range(data[genders[k]][i]["weight"]*dataDecs["Declension"+str(key)]*data["weight"][genders[k]]):
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
    
    for n in range(2):
        for o in range(data[pluralOptions[n]]):
            plurality.append(pluralOptions[n])
    chosenPlural =random.choice(plurality)

    filename = 'NounDeclension'+str(chosenWord[2])+'.json'
    with open(filename, 'r',encoding='utf-8') as k:
            data = json.load(k)

    print(data[chosenWord[1]][chosenWord[0]][chosenCase][chosenPlural])
    
    # generatedWord = tk.Label(wordframe, text=data[chosenWord[1]][chosenWord[0]][chosenCase][chosenPlural], bg ="gray")
    # generatedWord = tk.Text(wordframe)
    # generatedWord.pack()
    for widget in wordframe.winfo_children():
        widget.destroy()
    generatedWord = tk.Label(wordframe, text=data[chosenWord[1]][chosenWord[0]][chosenCase][chosenPlural], bg ="gray")
    generatedWord.pack()
    # print(wordList)
    # print(chosenWord)
    word = data[chosenWord[1]][chosenWord[0]][chosenCase][chosenPlural]
    declensionTrueLabel.config(text="",bg="white")
    caseTrueLabel.config(text="",bg="white")
    genderTrueLabel.config(text="", bg="white")
    pluralTrueLabel.config(text="",bg="white")

def checkWord():
    filename = 'NounDeclension'+str(chosenWord[2])+'.json'
    with open(filename, 'r',encoding='utf-8') as k:
            data = json.load(k)
    if(gender.get() != chosenWord[1]):
         print("wrong")
         incrementWeight()
    elif(declension.get()!=str(chosenWord[2])):
        print("wrong")
        incrementWeight()
    elif(data[chosenWord[1]][chosenWord[0]][case.get()][plural.get()] == data[chosenWord[1]][chosenWord[0]][chosenCase][chosenPlural]):
         print("true")
         decrementWeight()
    else:
         print("wrong")
         incrementWeight()
    print(data[chosenWord[1]][chosenWord[0]][case.get()][plural.get()])
    print(data[chosenWord[1]][chosenWord[0]][chosenCase][chosenPlural])
    global genderTrue, caseTrue,pluralTrue,declensionTrue
    genderTrue = "❌"
    genderColor = "red"
    caseTrue = "❌"
    caseColor = "red"
    pluralTrue = "❌"
    pluralColor = "red"
    declensionTrue = "❌"
    declensionColor = "red"
    if(gender.get() == chosenWord[1]):
        genderTrue = "✔️"
        genderColor = "green"
    if(declension.get()==str(chosenWord[2])):
        declensionTrue ="✔️"
        declensionColor = "green"
    if(data[chosenWord[1]][chosenWord[0]][case.get()][chosenPlural] == data[chosenWord[1]][chosenWord[0]][chosenCase][chosenPlural]):
        caseTrue = "✔️"
        caseColor = "green"
    if(data[chosenWord[1]][chosenWord[0]][chosenCase][plural.get()] == data[chosenWord[1]][chosenWord[0]][chosenCase][chosenPlural]):
        pluralTrue = "✔️"
        pluralColor = "green"
    declensionTrueLabel.config(text=declensionTrue,bg=declensionColor)
    caseTrueLabel.config(text=caseTrue,bg=caseColor)
    genderTrueLabel.config(text=genderTrue, bg=genderColor)
    pluralTrueLabel.config(text=pluralTrue,bg=pluralColor)
    


def resize_image(event):
    """
    Function to resize the image when the window size changes
    """
    global bg_image, bg_image_id
    window_width = event.width
    window_height = event.height

    # Calculate the scaling factors for width and height
    scale_width = window_width / bg_image_orig.width()
    scale_height = window_height / bg_image_orig.height()

    # Choose the minimum of the two scaling factors
    scale_factor = min(scale_width, scale_height)

    # Use the scaling factor to resize the image
    new_width = int(bg_image_orig.width() * scale_factor)
    new_height = int(bg_image_orig.height() * scale_factor)

    bg_image = bg_image_orig.subsample(int(bg_image_orig.width() / new_width), int(bg_image_orig.height() / new_height))
    canvas.itemconfig(bg_image_id, image=bg_image)
    canvas.coords(bg_image_id, window_width/2, window_height/2)

def decrementWeight():#remember to add edit to declension weight
    filename = 'NounDeclension'+str(chosenWord[2])+'.json' 
    with open(filename, 'r',encoding='utf-8') as k:
        data = json.load(k)
    word = data[chosenWord[1]][chosenWord[0]][chosenCase][chosenPlural]
    if(data[chosenWord[1]][chosenWord[0]]["weight"] > 1):
        data[chosenWord[1]][chosenWord[0]]["weight"] -=1
    if(data["weight"][chosenWord[1]] > 1):
        data["weight"][chosenWord[1]] -= 1
    val = set()
    for i in cases:
        for j in pluralOptions:
            if(data[chosenWord[1]][chosenWord[0]][i][j] == word):
                val.add(i)
                val.add(j) 
    for k in val:
        if(data[k] > 1):
            data[k] -=1
    print(val)
    os.remove(filename)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    
    fileDecs = 'NounDeclensions.json'
    with open(fileDecs, 'r',encoding='utf-8') as k:
        dataDecs = json.load(k)
    
    if(dataDecs["Declension"+str(chosenWord[2])] > 1):
        dataDecs["Declension"+str(chosenWord[2])] -= 1
    os.remove(fileDecs)
    with open(fileDecs, 'w', encoding='utf-8') as f:
        json.dump(dataDecs, f, indent=4, ensure_ascii=False)
    
def incrementWeight():#remember to add edit to declension weight
    filename = 'NounDeclension'+str(chosenWord[2])+'.json' 
    with open(filename, 'r',encoding='utf-8') as k:
        data = json.load(k)
    word = data[chosenWord[1]][chosenWord[0]][chosenCase][chosenPlural]
    if(data[chosenWord[1]][chosenWord[0]]["weight"] < 10):
        data[chosenWord[1]][chosenWord[0]]["weight"] +=1
    if(data["weight"][chosenWord[1]] < 10):
        data["weight"][chosenWord[1]] += 1
    val = set()
    for i in cases:
        for j in pluralOptions:
            if(data[chosenWord[1]][chosenWord[0]][i][j] == word):
                val.add(i)
                val.add(j) 
    for k in val:
        if(data[k] < 10):
            data[k] +=1
    print(val)
    os.remove(filename)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    
    fileDecs = 'NounDeclensions.json'
    with open(fileDecs, 'r',encoding='utf-8') as k:
        dataDecs = json.load(k)
    
    if(dataDecs["Declension"+str(chosenWord[2])] < 10):
        dataDecs["Declension"+str(chosenWord[2])] += 1
    os.remove(fileDecs)
    with open(fileDecs, 'w', encoding='utf-8') as f:
        json.dump(dataDecs, f, indent=4, ensure_ascii=False)    





# Load the image file
os.chdir('..')
bg_image_orig = tk.PhotoImage(file="images/pomp.png")
bg_image = bg_image_orig
os.chdir('json')
# Create a canvas
canvas = tk.Canvas(root, bg="#dbfcff")
canvas.pack(fill="both", expand=True)

# Create a frame to hold widgets
frame = tk.Frame(canvas, bg="")
frame.pack(expand=True, fill="both", padx=20, pady=20)
header = tk.Frame(frame, bg="")
header.pack(fill='x')
def resetWeightFunc():
    key=1
    while key<6:
        filename = 'NounDeclension'+str(key)+'.json'
        filenameO = 'base/NounDeclension'+str(key)+'.json'
        with open(filenameO, 'r',encoding='utf-8') as k:
            dataOrigin = json.load(k)
        key+=1
        os.remove(filename)
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(dataOrigin, f, indent=4, ensure_ascii=False)
    filename = 'NounDeclensions.json'
    filenameO = 'base/NounDeclensions.json'
    with open(filenameO, 'r',encoding='utf-8') as k:
        dataOrigin = json.load(k)
    key+=1
    os.remove(filename)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(dataOrigin, f, indent=4, ensure_ascii=False)
        
def settingsWindow():
    settingsWindow = tk.Toplevel(root)
    settingsWindow.title("Settings")
    settingsWindow.geometry("480x480")
    settingsWindow.grab_set()
    resetWeight = tk.Button(settingsWindow, text="Reset Weight", padx=10, pady=5, fg="white", bg="#262D42", command=resetWeightFunc)
    resetWeight.pack()
    customBackground = tk.Button(settingsWindow, text="Custom Background", padx=10, pady=5, fg="white", bg="#262D42")
    customBackground.pack()

os.chdir('..')
photo = tk.PhotoImage(file="images/settings.png")
os.chdir('json')
photo = photo.subsample(int(photo.width() / 75), int(photo.height() / 50))
settingsButton = tk.Button(header,text="Settings",image=photo, command=lambda:settingsWindow())
settingsButton.pack(side = "right")

# Create a frame to hold widgets
wordframe = tk.Frame(frame, bg="")
wordframe.pack()
generatedWord = tk.Label(wordframe, text="Word🗿", bg ="gray")
generatedWord.pack()
# Create a frame to hold widgets
buttons = tk.Frame(frame, bg="")
buttons.pack()
choices = tk.Frame(buttons, bg="")
choices.grid(row=0,column=1)
results = tk.Frame(buttons, bg="")
results.grid(row=0,column=2)
labels = tk.Frame(buttons, bg="")
labels.grid(row=0,column=0)

#Declension Choices
DeclensionText = tk.Label(labels, text = "Declension:")
DeclensionText.pack()
declension = tk.StringVar(root, "1")
declensionButtons = tk.Frame(choices, bg="")
declensionButtons.pack()
# Dictionary to create multiple buttons
values = {"First" : "1",
          "Second" : "2",
          "Third" : "3",
          "Fourth" : "4",
          "Fith" : "5"}
 
# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
count=1
for (text, value) in values.items():
    tk.Radiobutton(declensionButtons, text = text, variable = declension, 
                value = value, indicator = 0,
                background = "light blue").grid(row=0, column=count)
    count+=1
declensionTrueLabel = tk.Label(results,text="",bg="white")
declensionTrueLabel.pack()

#Cases Choices
caseButtons = tk.Frame(choices, bg="")
caseButtons.pack()
caseText = tk.Label(labels, text = "Case:")
caseText.pack()
case = tk.StringVar(root, "1")
# Dictionary to create multiple buttons
values = {"Nominative" : "nom",
          "Accusative" : "acc",
          "Genative" : "gen",
          "Dative" : "dat",
          "Ablative" : "abl"}
 
# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
count=1
for (text, value) in values.items():
    tk.Radiobutton(caseButtons, text = text, variable = case, 
                value = value, indicator = 0,
                background = "light blue").grid(row=1, column=count)
    count+=1
caseTrueLabel = tk.Label(results,text="",bg="white")
caseTrueLabel.pack()
#Declension words
genderButtons = tk.Frame(choices, bg="")
genderButtons.pack()
GenderText = tk.Label(labels, text = "Gender:")
GenderText.pack()
gender = tk.StringVar(root, "1")
 
# Dictionary to create multiple buttons
values = {"Feminine" : "Fem",
          "Masculine" : "Masc",
          "Neuter" : "Neut"}
 
# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
count=1
for (text, value) in values.items():
    tk.Radiobutton(genderButtons, text = text, variable = gender, 
                value = value, indicator = 0,
                background = "light blue",width=int(choices.winfo_width()/len(value))).grid(row=2, column=count)
    count+=1
genderTrueLabel = tk.Label(results,text="",bg="white")
genderTrueLabel.pack()
#Plural words
PluralText = tk.Label(labels, text = "Plurality:")
PluralText.pack()
plural = tk.StringVar(root, "1")
pluralButtons = tk.Frame(choices, bg="")
pluralButtons.pack()
# Dictionary to create multiple buttons
values = {"Singular" : "sing",
          "Plural" : "plur"}
 
# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
count=1
for (text, value) in values.items():
    tk.Radiobutton(pluralButtons, text = text, variable = plural, 
                value = value, indicator = 0,
                background = "light blue").grid(row=3, column=count)
    count+=1
pluralTrueLabel = tk.Label(results,text="",bg="white")
pluralTrueLabel.pack()

pluralButtons.grid_columnconfigure(1, weight=1)

genWord = tk.Button(frame, text="Generate Word", padx=10, pady=5, fg="white", bg="#262D42", command=getLatinWord)
genWord.pack()

checkWordButton = tk.Button(frame, text="CheckWord", padx=10, pady=5, fg="white", bg="#262D42", command=checkWord)
checkWordButton.pack()




# Center and fill the image
bg_image_id = canvas.create_image(0, 0, image=bg_image, anchor="center")
canvas.bind("<Configure>", resize_image)

# Run the Tkinter event loop
root.mainloop()
