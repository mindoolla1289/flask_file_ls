import os


for file in os.listdir("./uploads"):
    if file.endswith(".bin"):
        os.remove("./uploads/"+file)
        print("there is a fime")