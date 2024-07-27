# Although in previous classes we have already imported libraries, in this code, let's go into some details

# OS provide a way to interact with the operating system in a platform-independent manner.
import os
path = r"C:\Users\luisg\OneDrive\Project Dev\GitHub\LearningPython"
print(os.listdir(path))

# Working with datetime librarie
import datetime
today_date = datetime.date.today()
print(today_date)
right_now_time = datetime.datetime.now().time()
print(right_now_time)

# Renaming files and changing the path
folder_path = r"C:\Users\luisg\OneDrive\Project Dev\GitHub\LearningPython\Filles-8Modules-And-Libraries"
files_list = os.listdir(folder_path)
print(files_list)

for file in files_list:
    if ".txt" in file:
        if "22" in file:
            print("Move to folder 22", file)
            origin_path = os.path.join(folder_path,file)
            destiny_path = os.path.join(folder_path,"22",file)
            os.rename(origin_path,destiny_path)
        elif "23" in file:
            print("Move to folder 23", file)
            origin_path = os.path.join(folder_path,file)
            destiny_path = os.path.join(folder_path,"23",file)
            os.rename(origin_path,destiny_path)
        else:
            print("No files to move")
