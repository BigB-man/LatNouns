import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import json
import os
import random
import shutil
from functools import partial
from window import Window

class GuessNoun(Window):
        def __init__(self, master, **kwargs):
            super().__init__(master, **kwargs)
            
            global currentGuesses
            
            
            currentGuesses = 0

            

            def decrementWeight():#remember to add edit to declension weight
                self.crement("json/",0,chosenWord,chosenCase,chosenPlural)  
                
            def incrementWeight():#remember to add edit to declension weight
                self.crement("json/",1,chosenWord,chosenCase,chosenPlural)    
                
                
            def getLatinWord():
                genWord.pack_forget()
                checkWordButton.pack()
                global chosenWord,chosenCase,chosenPlural, word
                output=self.genLatinWord("json/")
                word = output[0]
                chosenWord = output[1]
                chosenCase = output[2]
                chosenPlural = output[3]

                for widget in wordframe.winfo_children():
                    widget.destroy()
                generatedWord = tk.Label(wordframe, text=word, bg ="white")
                generatedWord.pack()
                # print(wordList)
                # print(chosenWord)
                declensionTrueLabel.config(text="",bg="white")
                caseTrueLabel.config(text="",bg="white")
                genderTrueLabel.config(text="", bg="white")
                pluralTrueLabel.config(text="",bg="white")
                checkWordButton.pack()

            def checkWord():
                filename = 'json/NounDeclension'+str(chosenWord[2])+'.json'
                with open(filename, 'r',encoding='utf-8') as k:
                        data = json.load(k)
                options = [gender.get(),declension.get(),case.get(),plural.get]
                selected = True
                for i in options:
                    print(i)
                    if i == "0":
                        selected = False
                print(selected)
                if (selected == True):
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
                        print("wrongeeee")
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
                    print("Limit"+str(self.guessLimit))
                    if(genderColor==caseColor and caseColor == pluralColor and pluralColor == declensionColor and declensionColor == "green"):
                        currentGuesses = 0
                        checkWordButton.pack_forget()
                        genWord.pack()
                    if(currentGuesses >= self.guessLimit):
                        currentGuesses = 0
                        checkWordButton.pack_forget()
                        genWord.pack()

            # Create a frame to hold widgets
            wordframe = tk.Frame(master.canvas)
            wordframe.pack()
            generatedWord = tk.Label(wordframe, text="Word", bg ="white", fg="black")
            generatedWord.pack()
            # Create a frame to hold widgets
            buttons = tk.Frame(master.canvas)
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
            declension = tk.StringVar(self, "0")
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
            case = tk.StringVar(self, "0")
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
                tk.Radiobutton(caseButtons, text = text, variable = case, value = value, indicator = 0,background = "light blue",fg="black").grid(row=1, column=count)
                count+=1
            caseTrueLabel = tk.Label(results,text="",bg="white", width=2)
            caseTrueLabel.pack()
            #Declension words
            genderButtons = tk.Frame(choices, bg="")
            genderButtons.pack()
            GenderText = tk.Label(labels, text = "Gender:")
            GenderText.pack()
            gender = tk.StringVar(self, "0")
            
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
            plural = tk.StringVar(self, "0")
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


            genWord = tk.Button(self.master.canvas, text="Generate New Word", padx=10, pady=5, fg="white", bg="dark blue", command=getLatinWord)
            genWord.pack()

            checkWordButton = tk.Button(self.master.canvas, text="Check Word", padx=10, pady=5, fg="white", bg="dark blue", command=checkWord)
        
            
