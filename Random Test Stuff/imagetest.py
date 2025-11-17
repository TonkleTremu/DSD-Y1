from PIL import Image
with Image.open("hop.jpg") as im:
    im.rotate(45).show()