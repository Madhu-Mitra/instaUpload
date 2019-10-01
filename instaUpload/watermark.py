import imutils
from PIL import Image
def watermark_photo(waterpark_path,input_path,Output_path):
   
    img=Image.open(waterpark_path)
    
    Base=Image.open(input_path) 
    position=((Base.width-img.width),0)
    img = img.convert("RGBA")
    datas = img.getdata()
    
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    Base.paste(img,position,img)
    Base.save(Output_path)
    # img.save()

