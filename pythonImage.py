from PIL import Image
import os

def tileCreator(src, dest, sizeW, sizeH):
    # open the image
    try:
        srcImg = Image.open(src)
        # if src is bigger than requested size then resize
        srcImg = resize(srcImg, sizeW, sizeH)
    
        # get source image size
        srcW, srcH = srcImg.size
    
        # get the points to paste the picture
        tileList = []
        tileList = tileMatrix(srcW, srcH, sizeW, sizeH)
    
        # make the blank image
        blank = Image.new("RGBA", (sizeW, sizeH))
    
        # paste the tiles
        for x in tileList:
            blank.paste(srcImg, x)

        blank.save(dest)

    except IOError:
        print("Cannot open image")

def tileMatrix(sW, sH, w, h):
    # return the points to place the images to create the tile\
    tileList = []
    wL = []
    hL = []
    for x in range(0, w, sW):
        wL.append(x)
    for x in range(0, h, sH):
        hL.append(x)

    for w2 in wL:
        for h2 in hL:
            tileList.append((w2, h2))

    return tileList


def resize(img, w, h):
    # resizes the image until both width and height are smaller than requested
    srcW, srcH = img.size

    # resize proportionally
    ratio = 1.0
    if (srcW > w):
        ratio = srcW/w
    elif (srcH > h):
        ratio = srcH/h

    # resize
    img = img.resize((srcW/ratio, srcH/ratio))

    # check if it's done resizing
    if (srcW <= w and srcH <= h):
        return img
    else:
        img = resize(img, w, h)

    return img

def massTile(src, dest, w, h):
    # takes all image in a folder and create tiles for them
    images = []
    for file in os.listdir(src):
        newFile = file[:len(file)-4]
        newD = dest+"\\"+file+".png"
        tileCreator(src+"\\"+file, newD, w, h)
