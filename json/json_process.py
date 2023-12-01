import json
import os

# Get the directory of the current script
script_directory = os.path.dirname(os.path.realpath(__file__))

# Set the working directory to the script's directory
os.chdir(script_directory)

sourcefile = 'ls_A.json'
#sourcefile = input()
filename = 'NounDeclension1.json'
print("Current working directory:", os.getcwd())

with open(sourcefile, 'r', encoding='utf-8') as f:
    source = json.load(f)

with open(filename, 'r') as k:
    data = json.load(k)
    data['id'] = 134 # <--- add `id` value.

for i in source:#declension 1, i still need to implement to change for masculine words
    if i["entry_type"] == "main":
        if i["part_of_speech"] == "noun":
            if i["declension"] == 1:
                if i["gender"] == "F":
                    data.update({i["key"]:{"nom":{"sing":i["key"][:-1] + data["FORM"]["nom"]["sing"], "plur":i["key"][:-1] + data["FORM"]["nom"]["plur"]},
                                            "acc":{"sing":i["key"][:-1] + data["FORM"]["acc"]["sing"], "plur":i["key"][:-1] + data["FORM"]["acc"]["plur"]},
                                            "gen":{"sing":i["key"][:-1] + data["FORM"]["gen"]["sing"], "plur":i["key"][:-1] + data["FORM"]["gen"]["plur"]},
                                            "dat":{"sing":i["key"][:-1] + data["FORM"]["dat"]["sing"], "plur":i["key"][:-1] + data["FORM"]["dat"]["plur"]},
                                            "abl":{"sing":i["key"][:-1] + data["FORM"]["abl"]["sing"], "plur":i["key"][:-1] + data["FORM"]["abl"]["plur"]}}})
                # data[i["key"]]["gen"]["sing"] = i["key"][:-1] + data["FORM"]["gen"]["sing"]
                # data[i["key"]]["gen"]["plur"] = i["key"][:-1] + data["FORM"]["gen"]["plur"]
                # data[i["key"]]["dat"]["sing"] = i["key"][:-1] + data["FORM"]["dat"]["sing"]
                # data[i["key"]]["dat"]["plur"] = i["key"][:-1] + data["FORM"]["dat"]["plur"]
                # data[i["key"]]["abl"]["sing"] = i["key"][:-1] + data["FORM"]["abl"]["sing"]
                # data[i["key"]]["abl"]["plur"] = i["key"][:-1] + data["FORM"]["abl"]["plur"]

os.remove(filename)
with open(filename, 'w') as f:
    json.dump(data, f, indent=4)

