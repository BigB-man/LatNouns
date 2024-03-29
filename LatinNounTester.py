# Import module 
import tkinter as tk
from tkinter import filedialog
import json
import os
import random
import shutil
from functools import partial

# Create the main window
root = tk.Tk()
root.title("Latin Noun Tester")
#root.wm_attributes('-transparentcolor','#ab23ff')
root.iconbitmap("images/SquareNounDeclension.ico")
initImage = True
root.geometry("680x380")
genders=["Fem","Masc","Neut"]
guessLimit = 1
currentGuesses = 0
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
    generatedWord = tk.Label(wordframe, text=data[chosenWord[1]][chosenWord[0]][chosenCase][chosenPlural], bg ="white")
    generatedWord.pack()
    # print(wordList)
    # print(chosenWord)
    word = data[chosenWord[1]][chosenWord[0]][chosenCase][chosenPlural]
    declensionTrueLabel.config(text="",bg="white")
    caseTrueLabel.config(text="",bg="white")
    genderTrueLabel.config(text="", bg="white")
    pluralTrueLabel.config(text="",bg="white")
    checkWordButton.pack()

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
    global genderTrue, caseTrue,pluralTrue,declensionTrue, currentGuesses
    genderTrue = "❌"
    genderColor = "red"
    caseTrue = "❌"
    caseColor = "red"
    pluralTrue = "❌"
    pluralColor = "red"
    declensionTrue = "❌"
    declensionColor = "red"
    if(gender.get() == chosenWord[1]):
        genderTrue = "✓"
        genderColor = "green"
    if(declension.get()==str(chosenWord[2])):
        declensionTrue ="✓"
        declensionColor = "green"
    if(data[chosenWord[1]][chosenWord[0]][case.get()][chosenPlural] == data[chosenWord[1]][chosenWord[0]][chosenCase][chosenPlural]):
        caseTrue = "✓"
        caseColor = "green"
    if(data[chosenWord[1]][chosenWord[0]][chosenCase][plural.get()] == data[chosenWord[1]][chosenWord[0]][chosenCase][chosenPlural]):
        pluralTrue = "✓"
        pluralColor = "green"
    declensionTrueLabel.config(text=declensionTrue,bg=declensionColor)
    caseTrueLabel.config(text=caseTrue,bg=caseColor)
    genderTrueLabel.config(text=genderTrue, bg=genderColor)
    pluralTrueLabel.config(text=pluralTrue,bg=pluralColor)
    currentGuesses += 1
    if(genderColor==caseColor and caseColor == pluralColor and pluralColor == declensionColor and declensionColor == "green"):
        currentGuesses = 0
        checkWordButton.pack_forget()
    if(currentGuesses >= guessLimit):
        currentGuesses = 0
        checkWordButton.pack_forget()
   


def resize_image():

    global bg_image, bg_image_id
    window_width = root.winfo_width()
    window_height = root.winfo_height()

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
    if(data[chosenWord[1]][chosenWord[0]]["weight"] < 50):
        data[chosenWord[1]][chosenWord[0]]["weight"] +=1
    if(data["weight"][chosenWord[1]] < 50):
        data["weight"][chosenWord[1]] += 1
    val = set()
    for i in cases:
        for j in pluralOptions:
            if(data[chosenWord[1]][chosenWord[0]][i][j] == word):
                val.add(i)
                val.add(j) 
    for k in val:
        if(data[k] < 50):
            data[k] +=1
    print(val)
    os.remove(filename)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    
    fileDecs = 'NounDeclensions.json'
    with open(fileDecs, 'r',encoding='utf-8') as k:
        dataDecs = json.load(k)
    
    if(dataDecs["Declension"+str(chosenWord[2])] < 50):
        dataDecs["Declension"+str(chosenWord[2])] += 1
    os.remove(fileDecs)
    with open(fileDecs, 'w', encoding='utf-8') as f:
        json.dump(dataDecs, f, indent=4, ensure_ascii=False)    



# Create a canvas
canvas = tk.Canvas(root, bg="#dbfcff")
canvas.pack(fill="both", expand=True)





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
def UploadAction():
    os.chdir('..')
    try:
        filename = filedialog.askopenfilename(filetypes=[('image files', '.png')])
        print('Selected:', filename)
        file = filename[filename.rindex("/")+1:]
        print(os.getcwd())
        shutil.copyfile(filename, 'backgrounds/'+file)
        os.chdir('json')
    except:
        os.chdir('json')
        print("Upload errored this is the current directory:"+os.getcwd)
        
    




        

os.chdir('..')
photo = tk.PhotoImage(file="images/settings.png")
os.chdir('json')
photo = photo.subsample(int(photo.width() / 75), int(photo.height() / 50))



def settingsWindow():
    settingsWindow = tk.Toplevel(root)
    settingsWindow.title("Settings")
    settingsWindow.geometry("280x280")
    settingsWindow.grab_set()
    
    def SetBackground():
        SetBackgroundWin = tk.Toplevel(root)
        SetBackgroundWin.title("Backgrounds")
        SetBackgroundWin.grab_set()
        settingsWindow.destroy()

        os.chdir("..")
        os.chdir("backgrounds")
        files = os.listdir()
        backgroundImages = []
        for i in files:
            img = tk.PhotoImage(file=i)
            img=img.subsample(int(img.width() / 300), int(img.height() / 200))
            backgroundImages.append(img)
        os.chdir("..")
        os.chdir("json")
        
        container = tk.Frame(SetBackgroundWin)
        container.pack()
        canvas = tk.Canvas(container)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        def setImageFile(imgFile):
            print(imgFile)
            print("hi")
            filename = 'Background.json' 
            with open(filename, 'r',encoding='utf-8') as k:
                data = json.load(k)
            data["background"] = imgFile
            print(data)
            os.remove("Background.json")

            with open("Background.json", 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

            setImage()
            SetBackgroundWin.destroy()

        for i in range(len(backgroundImages)):
            tk.Button(scrollable_frame, image=backgroundImages[i],command=partial(setImageFile,files[i])).pack()
            
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        SetBackgroundWin.resizable(0, 0) 
        SetBackgroundWin.mainloop()
        
        
    def DeleteBackground():
        DeleteBackgroundWin = tk.Toplevel(root)
        DeleteBackgroundWin.title("Backgrounds")
        DeleteBackgroundWin.grab_set()
        settingsWindow.destroy()

        os.chdir("..")
        os.chdir("backgrounds")
        files = os.listdir()
        backgroundImages = []
        for i in files:
            img = tk.PhotoImage(file=i)
            img=img.subsample(int(img.width() / 300), int(img.height() / 200))
            backgroundImages.append(img)
        os.chdir("..")
        os.chdir("json")
        
        container = tk.Frame(DeleteBackgroundWin)
        container.pack()
        canvas = tk.Canvas(container)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        def setImageFile(imgFile):
            os.chdir("..")
            os.chdir("backgrounds")
            os.remove(imgFile)
            print(imgFile)
            print("hi")
            os.chdir("..")
            os.chdir("json")
            filename = 'Background.json' 
            with open(filename, 'r',encoding='utf-8') as k:
                data = json.load(k)
            if(data["background"]==imgFile):
                data["background"] = ""
            print(data)
            os.remove("Background.json")

            with open("Background.json", 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

            setImage()
            DeleteBackgroundWin.destroy()

        for i in range(len(backgroundImages)):
            tk.Button(scrollable_frame, image=backgroundImages[i],command=partial(setImageFile,files[i])).pack()
            
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        DeleteBackgroundWin.resizable(0, 0) 
        DeleteBackgroundWin.mainloop()
        

    resetWeight = tk.Button(settingsWindow, text="Reset Weight", padx=10, fg="white", bg="dark blue", command=resetWeightFunc)
    resetWeight.pack()
    
    uploadCustomBackground = tk.Button(settingsWindow, text="Upload Custom Background", padx=10, pady=5, fg="white", bg="dark blue", command=UploadAction)
    uploadCustomBackground.pack()

    setBackground = tk.Button(settingsWindow, text="Set Background", padx=10, pady=5, fg="white", bg="dark blue", command= SetBackground)
    setBackground.pack()

    setBackground = tk.Button(settingsWindow, text="Destroy Background", padx=10, pady=5, fg="white", bg="dark blue", command= DeleteBackground)
    setBackground.pack()

    LimitFrame = tk.Frame(settingsWindow, pady=10)
    LimitFrame.pack()
    LimitLabel = tk.Label(LimitFrame, text="Guess Limit:")
    LimitLabel.grid(row=1, column=0)
    guess = tk.IntVar(root, "1")
    # Dictionary to create multiple buttons
    values = {"1" : 1,
            "2" : 2,
            "3" : 3,}
    
    # Loop is used to create multiple Radiobuttons
    # rather than creating each button separately
    count=1
    for (text, value) in values.items():
        tk.Radiobutton(LimitFrame, text = text, variable = guess, 
                    value = value, indicator = 0,
                    background = "light blue",fg="black").grid(row=1, column=count)
        count+=1
    def submit():
        global guessLimit
        guessLimit = guess.get()
    submitButton = tk.Button(LimitFrame, text="Submit", fg="white", bg="dark blue", command=submit)
    submitButton.grid(row=1, column=4)

    
settingsButton = tk.Button(canvas,text="Settings",image=photo, command=lambda:settingsWindow())
settingsButton.pack(anchor="ne")

# Create a frame to hold widgets
wordframe = tk.Frame(canvas)
wordframe.pack()
generatedWord = tk.Label(wordframe, text="Word", bg ="white")
generatedWord.pack()
# Create a frame to hold widgets
buttons = tk.Frame(canvas)
buttons.pack()
choices = tk.Frame(buttons)
choices.grid(row=0,column=1)
results = tk.Frame(buttons)
results.grid(row=0,column=2)
labels = tk.Frame(buttons)
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
                background = "light blue",fg="black").grid(row=0, column=count)
    count+=1
declensionTrueLabel = tk.Label(results,text="",bg="white", width=2)
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
                background = "light blue",fg="black").grid(row=1, column=count)
    count+=1
caseTrueLabel = tk.Label(results,text="",bg="white", width=2)
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
                background = "light blue",fg="black",width=int(choices.winfo_width()/len(value))).grid(row=2, column=count)
    count+=1
genderTrueLabel = tk.Label(results,text="",bg="white", width=2)
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
                background = "light blue",fg="black").grid(row=3, column=count)
    count+=1
pluralTrueLabel = tk.Label(results,text="",bg="white", width=2)
pluralTrueLabel.pack()


genWord = tk.Button(canvas, text="Generate New Word", padx=10, pady=5, fg="white", bg="dark blue", command=getLatinWord)
genWord.pack()

checkWordButton = tk.Button(canvas, text="Check Word", padx=10, pady=5, fg="white", bg="dark blue", command=checkWord)
checkWordButton.pack()


# Load the image file
def setImage():
    global bg_image_orig, bg_image,bg_image_id, initImage
    fileDecs = 'Background.json'
    with open(fileDecs, 'r',encoding='utf-8') as k:
        data = json.load(k)
    os.chdir('..')
    if(data["background"] ==""):
        print("hie")
        canvas.delete("img")
        os.chdir('json')
    else:    
        try:
            bg_image_orig = tk.PhotoImage(file="backgrounds/"+data["background"])
            bg_image = bg_image_orig
            os.chdir('json')
            if(initImage == False):
                canvas.delete(bg_image_id)
            if(initImage == True):
                initImage = False
            bg_image_id = canvas.create_image(0, 0, image=bg_image, anchor="center",tag='img')
            resize_image()
        except:
            os.chdir('json')

setImage()

# Center and fill the image
def resize_imag(event):
    resize_image()
# canvas.bind("<Configure>", resize_image)
canvas.bind("<Configure>", resize_imag)
#root.resizable(0, 0) 

# Run the Tkinter event loop
root.mainloop()
