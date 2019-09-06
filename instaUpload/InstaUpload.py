from instapy_cli import client
import sys,io
from pathlib import Path
import os,random,shutil
direc="path"
folder_path=[]
dest=""
#get the paths which contains the .jpg files
for subdir, dirs, files in os.walk(direc):
    
    if any(File.endswith(".JPG") and not subdir.endswith("done") for File in os.listdir(subdir)):
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
username="USERNAME"
password="PASSWORD"
cookie_file="USERNAME.json"
test="test"



try:
   
    with client(username,password,cookie_file=cookie_file) as cli:
        
        cookies=cli.get_cookie()
        
        msg=cli.upload(file_path,test)
        
        #    print("successfully loaded")
        
        
        ig=cli.api()
        
except :
    
    print("error while uploading: ",len(output))
else:
    print("seccessfully uploaded")
    #create directory if exists
    if not (os.path.isdir(dest)): 
        os.mkdir(dest)
    #move the file
    shutil.move(selected_dir+"/"+selected_file,dest)
    print("success moved the file!")


            


            
