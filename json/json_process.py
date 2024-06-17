import json
import os

# Get the directory of the current script
script_directory = os.path.dirname(os.path.realpath(__file__))

# Set the working directory to the script's directory
os.chdir(script_directory)



caseum = True

while caseum:
    while caseum:
        caseum = False
        try:
            case = int(input("Declension: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            caseum = True
    caseum = True
    
    filename = 'NounDeclension'+str(case)+'.json'
    
    with open(filename, 'r',encoding='utf-8') as k:
        data = json.load(k)
    
    while caseum:
        caseum = False
        try:
            gend = int(input("Gender: F,M,N? "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            caseum = True
    caseum = True
    genders=["Fem","Masc","Neut"]

    data[genders[gend-1]].update({input("word"):{
        "nom":{
            "sing":input("Nom sing: "), 
            "plur":input("Nom plur: ")},
        "acc":{
            "sing":input("Acc sing: "), 
            "plur":input("Acc plur: ")},
        "gen":{
            "sing":input("Gen sing: "), 
            "plur":input("Gen plur: ")},
        "dat":{
            "sing":input("Dat sing: "), 
            "plur":input("Dat plur: ")},
        "abl":{
            "sing":input("abl sing: "), 
            "plur":input("abl plur: ")
        },
        "Def":"idk",
        "weight":7
        }})
    os.remove(filename)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
