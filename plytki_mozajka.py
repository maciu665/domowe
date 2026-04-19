from PIL import Image
import sys
import os
import pathlib

lista = os.listdir("/home/maciejm/PROJEKT/KONSTRUKCYJNY-200424/TEX/")
lista.sort()

images = []
for i in lista:
    if i.endswith(".webp"):
        images.append(Image.open("/home/maciejm/PROJEKT/KONSTRUKCYJNY-200424/TEX/" + i))

print(images)
#finsize = [1500, 375]
finsize = [1510, 385]

simages = []
rimages = []

for i in images:
    # reate new image with dimensions finsize
    new_image = Image.new("RGB", finsize, (0,0,0))
    # create new image in the size of the original image
    old_roughness = Image.new("RGB", i.size, (0,0,0))
    new_roughness = Image.new("RGB", finsize, (255, 255, 255))
    # crop image i to length of 1500
    ci = i.crop((0, 0, 1500, i.size[1]))
    cr = old_roughness.crop((0, 0, 1500, old_roughness.size[1]))
    # paste the image into the new image
    new_image.paste(ci, (int((finsize[0] - 1500) / 2), int((finsize[1] - ci.size[1]) / 2)))
    new_roughness.paste(cr, (int((finsize[0] - 1500) / 2), int((finsize[1] - cr.size[1]) / 2)))
    simages.append(new_image)
    rimages.append(new_roughness)

    # save the image
    #new_image.save("/home/maciejm/PROJEKT/KONSTRUKCYJNY-200424/TEX/" + pathlib.Path(i.filename).stem + ".png")
    #new_roughness.save("/home/maciejm/PROJEKT/KONSTRUKCYJNY-200424/TEX/" + pathlib.Path(i.filename).stem + "_roughness.png")
    #sys.exit()
    
# create two mosaics, one for simages and one for rimages, with 20 rows and 9 columns, choose images randomly from simages and use the corresponding rimage for the roughness mosaic
# add random rotations by 180 to the images in the mosaic, with a 50% chance for each image to be rotated
import random   
mosaic = Image.new("RGB", (finsize[0] * 9, finsize[1] * 20), (0,0,0))
roughness_mosaic = Image.new("RGB", (finsize[0] * 9, finsize[1] * 20), (255, 255, 255))
for i in range(20):
    for j in range(9):
        index = random.randint(0, len(simages) - 1)
        if random.random() < 0.5:
            simages[index] = simages[index].rotate(180)
            rimages[index] = rimages[index].rotate(180)
        mosaic.paste(simages[index], (j * finsize[0], i * finsize[1]))
        roughness_mosaic.paste(rimages[index], (j * finsize[0], i * finsize[1]))    
mosaic.save("/home/maciejm/PROJEKT/KONSTRUKCYJNY-200424/TEX/mosaic.jpg")
roughness_mosaic.save("/home/maciejm/PROJEKT/KONSTRUKCYJNY-200424/TEX/roughness_mosaic.jpg")