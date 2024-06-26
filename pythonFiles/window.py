import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import json
import os
import random
import shutil
from functools import partial

initImage = True

class Window(tk.Frame):

        def __init__(self, master=None, **kwargs):

            tk.Frame.__init__(self, master, **kwargs)
            
            guessLimit = 1 #the limit for guesses
            self.guessLimit = guessLimit
            self.master = master
            master.title("Latin Noun Tester") #sets the title of the app       
            

            def settingsWindow():#creates settings window and contains settings functions
                settingsWindow = tk.Toplevel(self)
                settingsWindow.title("Settings")
                settingsWindow.geometry("280x280")
                settingsWindow.grab_set()
                def resetWeightFunc(): #function to reset the weightings of the noun and part tester
                    key=1
                    while key<6:
                        filename = 'json/NounDeclension'+str(key)+'.json'
                        filenameP = 'json/PartTester/NounDeclension'+str(key)+'.json'
                        filenameO = 'json/base/NounDeclension'+str(key)+'.json'
                        with open(filenameO, 'r',encoding='utf-8') as k:
                            dataOrigin = json.load(k)
                        key+=1
                        os.remove(filename)
                        with open(filename, 'w', encoding='utf-8') as f:
                            json.dump(dataOrigin, f, indent=4, ensure_ascii=False)
                        os.remove(filenameP)
                        with open(filenameP, 'w', encoding='utf-8') as f:
                            json.dump(dataOrigin, f, indent=4, ensure_ascii=False)
                    filename = 'json/NounDeclensions.json'
                    filenameP = 'json/PartTester/NounDeclensions.json'

                    filenameO = 'json/base/NounDeclensions.json'
                    with open(filenameO, 'r',encoding='utf-8') as k:
                        dataOrigin = json.load(k)
                    key+=1
                    os.remove(filename)
                    with open(filename, 'w', encoding='utf-8') as f:
                        json.dump(dataOrigin, f, indent=4, ensure_ascii=False)
                    os.remove(filenameP)
                    with open(filenameP, 'w', encoding='utf-8') as f:
                        json.dump(dataOrigin, f, indent=4, ensure_ascii=False)
                def UploadAction(): #function to upload a png background
                    try:
                        filename = filedialog.askopenfilename(filetypes=[('image files', '.png')])
                        print('Selected:', filename)
                        file = filename[filename.rindex("/")+1:]
                        shutil.copyfile(filename, 'backgrounds/'+file)
                    except:
                        print("Upload error")
                
                def SetBackground():
                    SetBackgroundWin = tk.Toplevel(self)
                    SetBackgroundWin.title("Backgrounds")
                    SetBackgroundWin.grab_set()
                    settingsWindow.destroy()

                    os.chdir("backgrounds")
                    files = os.listdir()
                    backgroundImages = []
                    for i in files:
                        img = tk.PhotoImage(file=i)
                        img=img.subsample(int(img.width() / 300), int(img.height() / 200))
                        backgroundImages.append(img)
                    os.chdir("..")
                    
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
                        filename = 'json/Background.json' 
                        with open(filename, 'r',encoding='utf-8') as k:
                            data = json.load(k)
                        data["background"] = imgFile
                        print(data)
                        os.remove("json/Background.json")

                        with open("json/Background.json", 'w', encoding='utf-8') as f:
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
                    DeleteBackgroundWin = tk.Toplevel(self)
                    DeleteBackgroundWin.title("Backgrounds")
                    DeleteBackgroundWin.grab_set()
                    settingsWindow.destroy()

                    os.chdir("backgrounds")
                    files = os.listdir()
                    backgroundImages = []
                    for i in files:
                        img = tk.PhotoImage(file=i)
                        img=img.subsample(int(img.width() / 300), int(img.height() / 200))
                        backgroundImages.append(img)
                    os.chdir("..")
                    
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
                        os.chdir("backgrounds")
                        os.remove(imgFile)
                        print(imgFile)
                        print("hi")
                        os.chdir("..")
                        filename = 'json/Background.json' 
                        with open(filename, 'r',encoding='utf-8') as k:
                            data = json.load(k)
                        if(data["background"]==imgFile):
                            data["background"] = ""
                        print(data)
                        os.remove("json/Background.json")

                        with open("json/Background.json", 'w', encoding='utf-8') as f:
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
                guess = tk.IntVar(self, "1")
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
                    self.guessLimit = guess.get()
                    
                submitButton = tk.Button(LimitFrame, text="Submit", fg="white", bg="dark blue", command=submit)
                submitButton.grid(row=1, column=4)
            
            canvas = tk.Canvas(self.master, bg="#dbfcff")#canvas on which UI elements are placed
            canvas.pack(fill="both", expand=True)


            settingsButton = tk.Button(canvas,text="⚙Settings", command=lambda:settingsWindow(),font=("TkDefaultFont",10))
            settingsButton.pack(side="right", anchor="ne")
            def OpenPage(x):#changes the page by switching which class is the frame
                self.master.change(x)
            NounTestButton = tk.Button(canvas ,text="Noun Tester",command=lambda:OpenPage(GuessNoun))#opens Noun tester
            NounTestButton.pack(side="left", anchor="nw")
            PartTestButton = tk.Button(canvas ,text="Part Tester",command=lambda:OpenPage(GuessPart))#opens Part tester
            PartTestButton.pack(anchor="nw")
            self.master.canvas = canvas

            
            def setImage():#sets the background of the page
                global bg_image_orig, bg_image,bg_image_id, initImage
                fileDecs = 'json/Background.json'
                with open(fileDecs, 'r',encoding='utf-8') as k:
                    data = json.load(k)

                try:    
                    bg_image_orig = tk.PhotoImage(file="backgrounds/"+data["background"])
                    bg_image = bg_image_orig
                    if(initImage == False):
                        canvas.delete(bg_image_id)
                    if(initImage == True):
                        initImage = False
                    bg_image_id = canvas.create_image(0, 0, image=bg_image, anchor="center",tag='img')
                    resize_image()
                except:
                    print("Error Loading Background")
                    canvas.delete("img")

            
            
            def resize_image():

                global bg_image, bg_image_id
                window_width = self.master.winfo_width()
                window_height = self.master.winfo_height()

                # Calculate the scaling factors for width and height
                scale_width = window_width / bg_image_orig.width()
                scale_height = window_height / bg_image_orig.height()

                # Choose the minimum of the two scaling factors
                scale_factor = min(scale_width, scale_height)

                # Use the scaling factor to resize the image
                new_width = int(bg_image_orig.width() * scale_factor)
                new_height = int(bg_image_orig.height() * scale_factor)
                try:
                    bg_image = bg_image_orig.subsample(int(bg_image_orig.width() / new_width), int(bg_image_orig.height() / new_height))
                except:
                    print("wu oh")
                canvas.itemconfig(bg_image_id, image=bg_image)
                canvas.coords(bg_image_id, window_width/2, window_height/2)
            
            def resize_imag(event):#function to call resize_image()
                resize_image()
            
            canvas.bind("<Configure>", resize_imag)#whenever canvas is resized it runs the resize image function
            setImage()        
        
        def genLatinWord(self,path):#generates latin word
                genders=["Fem","Masc","Neut"]
                cases= ["nom","acc","gen","dat","abl"]


                key=1
                wordList=[]
                wordCount = 0
                
                

                fileDecs = path+'NounDeclensions.json'
                with open(fileDecs, 'r',encoding='utf-8') as k:
                    dataDecs = json.load(k)

                while key<6:
                    filename = path+'NounDeclension'+str(key)+'.json'
                    with open(filename, 'r',encoding='utf-8') as k:
                        data = json.load(k)
                    for k in range(3):
                        for i in data[genders[k]]:
                            for j in range(data[genders[k]][i]["weight"]*dataDecs["Declension"+str(key)]*data["weight"][genders[k]]):
                                wordList.append([])
                                wordList[wordCount].append(i)#word
                                wordList[wordCount].append(genders[k])#gender
                                wordList[wordCount].append(key)#declension
                                wordCount+=1
                    key+=1
                ranChosenWord=random.choice(wordList)
                
                caseNoun =[]
                cases= ["nom","acc","gen","dat","abl"]                
                for l in range(len(cases)):
                    for m in range(data[cases[l]]):
                        caseNoun.append(cases[l])
                ranChosenCase =random.choice(caseNoun)
                
                plurality =[]
                pluralOptions = ["sing","plur"]
                for n in range(2):
                    for o in range(data[pluralOptions[n]]):
                        plurality.append(pluralOptions[n])
                ranChosenPlural =random.choice(plurality) 

                filename = path+'NounDeclension'+str(ranChosenWord[2])+'.json'
                with open(filename, 'r',encoding='utf-8') as k:
                        data = json.load(k)
                 
                ranWord = data[ranChosenWord[1]][ranChosenWord[0]][ranChosenCase][ranChosenPlural]
                
                
                ranChosenGender = ranChosenWord[1]
                # print(key)

                return [ranWord,ranChosenWord,ranChosenCase,ranChosenPlural,ranChosenGender,ranChosenWord[2]]
        def crement(self,path,mode,chosenWord,chosenCase,chosenPlural):
            cases= ["nom","acc","gen","dat","abl"]
            pluralOptions = ["sing","plur"]
            filename = path+'NounDeclension'+str(chosenWord[2])+'.json' 
            with open(filename, 'r',encoding='utf-8') as k:
                data = json.load(k)
            
            word = data[chosenWord[1]][chosenWord[0]][chosenCase][chosenPlural]
            if(mode == 0):#decrement the noun & gender weight
                if(data[chosenWord[1]][chosenWord[0]]["weight"] > 1):
                    data[chosenWord[1]][chosenWord[0]]["weight"] -=1
                if(data["weight"][chosenWord[1]] > 1):
                    data["weight"][chosenWord[1]] -= 1
            if(mode == 1):#increment the noun & gender weight
                if(data[chosenWord[1]][chosenWord[0]]["weight"] < 50):
                    data[chosenWord[1]][chosenWord[0]]["weight"] +=1
                if(data["weight"][chosenWord[1]] < 50):
                    data["weight"][chosenWord[1]] += 1
            
            attriubutes = set()#stores the attributes of the word without any duplicates
            
            for i in cases:#adding each attribute found in the word to the set
                for j in pluralOptions:
                    if(data[chosenWord[1]][chosenWord[0]][i][j] == word):
                        attriubutes.add(i)
                        attriubutes.add(j) 
            for k in attriubutes:
                if(mode==0):#decrement the attribute weight
                    if(data[k] > 1):
                        data[k] -=1
                if(mode ==1):#increment the attribute weight
                    if(data[k] < 50):
                        data[k] +=1
                
            os.remove(filename)
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            
            
            fileDecs = path+'NounDeclensions.json'
            with open(fileDecs, 'r',encoding='utf-8') as k:
                dataDecs = json.load(k)
            
            if(mode==0):#decrement the declension weighting
                if(dataDecs["Declension"+str(chosenWord[2])] > 1):
                    dataDecs["Declension"+str(chosenWord[2])] -= 1
            if(mode==1):#increment the declension weighting
                if(dataDecs["Declension"+str(chosenWord[2])] < 50):
                    dataDecs["Declension"+str(chosenWord[2])] += 1
            
            os.remove(fileDecs)
            with open(fileDecs, 'w', encoding='utf-8') as f:
                json.dump(dataDecs, f, indent=4, ensure_ascii=False)
           

from pythonFiles.GuessPart import GuessPart  
from pythonFiles.GuessNoun import GuessNoun