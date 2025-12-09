from PIL import Image
def xorImage(imageOnePath, imageTwoPath, outPath) :

    imageOne = Image.open(imageOnePath).convert("RGB")
    imageTwo = Image.open(imageTwoPath).convert("RGB")

    if imageOne.size != imageTwo.size:
        raise ValueError("Images need to be the same size")

    width, height = imageOne.size
    outputImage = Image.new("RGB", (width, height) )
    pixelImageOne = imageOne. load()
    pixelImageTwo = imageTwo.load()
    pixelImageOutput = outputImage . load ()

    for y in range(height) :
        for x in range(width) :
            redOne, greenOne, blueOne = pixelImageOne[x, y]
            redTwo, greenTwo, blueTwo = pixelImageTwo[x, y]

            pixelImageOutput[x, y] = (
                redOne ^ redTwo,
                greenOne ^ greenTwo,
                blueOne ^ blueTwo,
            )
    outputImage.save(outPath)
    print(f"Saved XOR image to {outPath}")
xorImage("C:\Users\M2500579\Downloads\image.jpg", 
         "C:\Users\M2500579\Downloads\image.jpg", 
         "C:/Users/M2500579/OneDrive - Middlesbrough College/Documents/GitHub/dsd-y1/Random Test Stuff/chaos.jpg")