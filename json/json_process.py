import json
import os

# Get the directory of the current script
script_directory = os.path.dirname(os.path.realpath(__file__))

# Set the working directory to the script's directory
os.chdir(script_directory)
filename = 'NounDeclension1.json'
print("Current working directory:", os.getcwd())
letters =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Z']
with open(filename, 'r',encoding='utf-8') as k:
    data = json.load(k)
index = 0
for j in letters:
    sourcefile = 'ls_'+letters[index]+'.json'
    with open(sourcefile, 'r', encoding='utf-8') as f:
        source = json.load(f)
        index +=1
    for i in source:#declension 1, i still need to implement to change for masculine words
        if i["entry_type"] == "main":
            if i["part_of_speech"] == "noun":
                if i["declension"] == 1:
                    if i["gender"] == "F":
                        data["Fem"].update({i["key"]:{
                            "nom":{
                                "sing":i["title_orthography"][:-1] + data["Fem"]["FORM"]["nom"]["sing"], 
                                "plur":i["title_orthography"][:-1] + data["Fem"]["FORM"]["nom"]["plur"]},
                            "acc":{
                                "sing":i["title_orthography"][:-1] + data["Fem"]["FORM"]["acc"]["sing"], 
                                "plur":i["title_orthography"][:-1] + data["Fem"]["FORM"]["acc"]["plur"]},
                            "gen":{
                                "sing":i["title_orthography"][:-1] + data["Fem"]["FORM"]["gen"]["sing"], 
                                "plur":i["title_orthography"][:-1] + data["Fem"]["FORM"]["gen"]["plur"]},
                            "dat":{
                                "sing":i["title_orthography"][:-1] + data["Fem"]["FORM"]["dat"]["sing"], 
                                "plur":i["title_orthography"][:-1] + data["Fem"]["FORM"]["dat"]["plur"]},
                            "abl":{
                                "sing":i["title_orthography"][:-1] + data["Fem"]["FORM"]["abl"]["sing"], 
                                "plur":i["title_orthography"][:-1] + data["Fem"]["FORM"]["abl"]["plur"]},
                            "Def":i["senses"],
                            "weight":7}})

os.remove(filename)
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
