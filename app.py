# Import module 
import tkinter as tk
import json
import os
import random
# Create object 
def getLatinWord():
    # Get the directory of the current script
    script_directory = os.path.dirname(os.path.realpath(__file__))

    # Set the working directory to the script's directory
    os.chdir(script_directory)
    os.chdir("json")
    #print(script_directory)


    key=1
    wordList=[]
    wordCount = 0
    genders=["Fem","Masc","Neut"]
    global chosenWord

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
    
    # generatedWord = tk.Label(wordframe, text=data[chosenWord[1]][chosenWord[0]][chosenCase][chosenPlural], bg ="gray")
    # generatedWord = tk.Text(wordframe)
    # generatedWord.pack()
    for widget in wordframe.winfo_children():
        widget.destroy()
    generatedWord = tk.Label(wordframe, text=data[chosenWord[1]][chosenWord[0]][chosenCase][chosenPlural], bg ="gray")
    generatedWord.pack()
    # print(wordList)
    # print(chosenWord)

# def checkWord(case,plurality,gender):
#     filename = 'NounDeclension'+str(chosenWord[2])+'.json'
#     with open(filename, 'r',encoding='utf-8') as k:
#             data = json.load(k)
#     if data[]


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

# Create the main window
root = tk.Tk()
root.title("Background Image Example")


root.geometry("1080x720")

# Load the image file
bg_image_orig = tk.PhotoImage(file="images/pomp.png")
bg_image = bg_image_orig

# Create a canvas
canvas = tk.Canvas(root, bg="#dbfcff")
canvas.pack(fill="both", expand=True)

# Create a frame to hold widgets
frame = tk.Frame(canvas, bg="")
frame.pack(expand=True, fill="both", padx=20, pady=20)

label = tk.Label(frame, text="chez")
label.pack()


# Create a frame to hold widgets
wordframe = tk.Frame(frame, bg="")
wordframe.pack()

# Create a frame to hold widgets
singular = tk.Frame(frame, bg="")
singular.pack()
nomSing = tk.Button(singular, text="Nominative singular", padx=10, pady=5, fg="white", bg="#262D42")
nomSing.grid(row=0, column=0)

accSing = tk.Button(singular, text="Accusative singular", padx=10, pady=5, fg="white", bg="#262D42")
accSing.grid(row=1, column=0)

genSing = tk.Button(singular, text="Genative singular", padx=10, pady=5, fg="white", bg="#262D42")
genSing.grid(row=2, column=0)

datSing = tk.Button(singular, text="Dative singular", padx=10, pady=5, fg="white", bg="#262D42")
datSing.grid(row=3, column=0)

ablSing = tk.Button(singular, text="Ablative singular", padx=10, pady=5, fg="white", bg="#262D42")
ablSing.grid(row=4, column=0)


nomPlur = tk.Button(singular, text="Nominative plural", padx=10, pady=5, fg="white", bg="#262D42")
nomPlur.grid(row=0, column=1)

accPlur = tk.Button(singular, text="Accusative plural", padx=10, pady=5, fg="white", bg="#262D42")
accPlur.grid(row=1, column=1)

genPlur = tk.Button(singular, text="Genative plural", padx=10, pady=5, fg="white", bg="#262D42")
genPlur.grid(row=2, column=1)

datPlur = tk.Button(singular, text="Dative plural", padx=10, pady=5, fg="white", bg="#262D42")
datPlur.grid(row=3, column=1)

ablPlur = tk.Button(singular, text="Ablative plural", padx=10, pady=5, fg="white", bg="#262D42")
ablPlur.grid(row=4, column=1)


genWord = tk.Button(frame, text="Generate Word", padx=10, pady=5, fg="white", bg="#262D42", command=getLatinWord)
genWord.pack()

# Center and fill the image
bg_image_id = canvas.create_image(0, 0, image=bg_image, anchor="center")
canvas.bind("<Configure>", resize_image)

# Run the Tkinter event loop
root.mainloop()
