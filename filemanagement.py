import os
import shutil
source_path=input("Enter source path")
destination_path = input("Enter Destination path")
Extensions = [".py",".php",".png",".jpg",".pdf",".ppt",".mp3",".mp4",".exe",".zip",".docx",".txt",".pptx"]
list_path = os.listdir(source_path)
os.chdir(destination_path) 
if not os.path.isdir('mainfolder'):
    os.mkdir("mainfolder")
files = os.path.join(destination_path,"mainfolder")
os.chdir(files)
for i in list_path:
    for j in Extensions:
        if i.endswith(j[1:]):
            if not os.path.isdir(j[1:]):
                folder = os.path.join(files,j[1:])
                os.mkdir(folder)            
                shutil.move(os.path.join(source_path,i),folder)
                break
            else:
                 shutil.move(os.path.join(source_path,i),os.path.join(j[1:]))
                 break