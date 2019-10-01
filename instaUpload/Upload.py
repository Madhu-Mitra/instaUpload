from instapy_cli import client
import sys,io
from pathlib import Path
from PIL import Image
import os,random,shutil
from watermark import watermark_photo
direc=[directory]
folder_path=[]
dest=""

#get the paths which contains the .jpg files
for subdir, dirs, files in os.walk(direc):
    
    if any(File.endswith(".JPG") and not (subdir.endswith("done") or "done" in subdir )for File in os.listdir(subdir)):
         folder_path.append(subdir)
         
    elif (subdir.endswith("done")):
            dest=subdir
#select random folder, file to upload and dest
index=random.randint(0,len(folder_path)-1)
selected_dir=folder_path[index]
selected_file=random.choice(os.listdir(selected_dir))
dest+=selected_dir[selected_dir.rfind("/"):]+"/"
file_path=selected_dir+"/"+selected_file
#upload in instagram
username=[username]
password=[password]
cookie_file="[username].json"
tag_file=open([tags filepath]'r')
tags=tag_file.readlines()

watermark_photo([watermark_path],file_path,file_path)

try:
   
    with client(username,password,cookie_file=cookie_file) as cli:
        
        cookies=cli.get_cookie()
        
        msg=cli.upload(file_path,tags)
        
        #    print("successfully loaded")
        
        
        ig=cli.api()
        
except :
    
    print("error while uploading: ")
else:
    print("seccessfully uploaded")
    #create directory if exists
    if not (os.path.isdir(dest)): 
        os.mkdir(dest)
    #move the file
    shutil.move(selected_dir+"/"+selected_file,dest)
    print("success moved the file!")


            


            
