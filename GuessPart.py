import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import json
import os
import random
import shutil
from functools import partial
from window import Window

class GuessPart(Window):
    def __init__(self, master, **kwargs):
            super().__init__(master, **kwargs)
            genders=["Fem","Masc","Neut"]
            global currentGuesses
            currentGuesses = 0
            cases= ["nom","acc","gen","dat","abl"]
            pluralOptions = ["sing","plur"]
            master.title("Latin Noun Tester")

            def decrementWeight():#remember to add edit to declension weight
                filename = 'json/PartTester/NounDeclension'+str(chosenWord[2])+'.json' 
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
                
                
                fileDecs = 'json/PartTester/NounDeclensions.json'
                with open(fileDecs, 'r',encoding='utf-8') as k:
                    dataDecs = json.load(k)
                
                if(dataDecs["Declension"+str(chosenWord[2])] > 1):
                    dataDecs["Declension"+str(chosenWord[2])] -= 1
                os.remove(fileDecs)
                with open(fileDecs, 'w', encoding='utf-8') as f:
                    json.dump(dataDecs, f, indent=4, ensure_ascii=False)
                
            def incrementWeight():#remember to add edit to declension weight
                filename = 'json/PartTester/NounDeclension'+str(chosenWord[2])+'.json' 
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
                
                
                fileDecs = 'json/PartTester/NounDeclensions.json'
                with open(fileDecs, 'r',encoding='utf-8') as k:
                    dataDecs = json.load(k)
                
                if(dataDecs["Declension"+str(chosenWord[2])] < 50):
                    dataDecs["Declension"+str(chosenWord[2])] += 1
                os.remove(fileDecs)
                with open(fileDecs, 'w', encoding='utf-8') as f:
                    json.dump(dataDecs, f, indent=4, ensure_ascii=False)    
            
            
                
            def getLatinWord():
                global word, chosenPlural, chosenCase, chosenGender, chosenWord, chosenKey
                output = self.genLatinWord("json/PartTester/")
                print(output)
                word = output[0]
                chosenGender = output[4]
                chosenCase = output[2]
                chosenPlural = output[3]
                chosenWord = output[1]
                chosenKey = output[5]
                for widget in wordframe.winfo_children():
                    widget.destroy()
                generatedWord = tk.Label(wordframe, text=chosenGender+", "+chosenCase+", "+chosenPlural, bg ="white")
                generatedWord.pack()
                wordChoice = []

                for i in range(6):
                    # wordChoice.append(word)
                    wordChoice.append(self.genLatinWord("json/og/"))
                wordChoice[random.randrange(0, 6, 1)] = output
                print("answer:"+word)


                for i in choices.grid_slaves():
                    i.grid_forget()
                for i in range(3):
                    tk.Button(choices, text = wordChoice[i][0], background = "light blue",fg="black", width= 20, command=partial(checkWord,wordChoice[i])).grid(column=0, row=i)
                for i in range(3,6):
                    tk.Button(choices, text = wordChoice[i][0], background = "light blue",fg="black", width=20, command=partial(checkWord,wordChoice[i])).grid(column=1, row=(i-3))
                genWord.pack_forget()

            def nuuh():
                print("you've already chosen")

            def checkWord(selecWord):
                genWord.pack()
                print(word)
                print(selecWord)
                filename = 'json/NounDeclension'+str(selecWord[1][2])+'.json'
                with open(filename, 'r',encoding='utf-8') as k:
                        data = json.load(k)
                for i in choices.grid_slaves():
                    i.configure(command=nuuh)
                    if (i.cget('text')==selecWord[0]):
                        
                        i.configure(bg="grey")
                    
                try:
                    if(selecWord[0]==data[chosenGender][selecWord[1][0]][chosenCase][chosenPlural]):
                        print("true")
                        decrementWeight()
                        titleLabel = tk.Label(choices, text="✓", bg="green",fg="white", font=("Arial", 25))
                        titleLabel.grid(columnspan=2)
                    else:
                        print("wrong")
                        incrementWeight()
                        titleLabel = tk.Label(choices, text="❌",bg="red",fg="white",font=("Arial", 25))
                        titleLabel.grid(columnspan=2)
                except:
                    print("wrong")
                    incrementWeight()
                    titleLabel = tk.Label(choices, text="❌",bg="red",fg="white",font=("Arial", 25))
                    titleLabel.grid(columnspan=2)
            
                
                
            # Create a frame to hold widgets
            wordframe = tk.Frame(master.canvas)
            wordframe.pack()
            generatedWord = tk.Label(wordframe, text="Word", bg ="white")
            generatedWord.pack()
            # Create a frame to hold widgets

            choices = tk.Frame(master.canvas, bg="")
            choices.pack()


                

            genWord = tk.Button(self.master.canvas, text="Generate New Word", padx=10, pady=5, fg="white", bg="dark blue", command=getLatinWord)
            genWord.pack(anchor="s")
