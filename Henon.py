from PIL import Image

import os
import numpy
import math

from PIL import Image

def imageMatrix(imgToEncrypt):
  
  height = imgToEncrypt.shape[0]
  width = imgToEncrypt.shape[1] # On récupère dans notre structure les informations t-elle que la hauteur et la largeur.

  image_matrix = []

  for w in range(width):
    row = []

    for h in range(height):

      try:
        row.append(imgToEncrypt[w,h])
      except:
        row = imgToEncrypt[w,h]
    try: 
      image_matrix.append(row)
    except:
      image_matrix = [row]
  

  return image_matrix


def dec(bitSequence):
  decimal = 0

  for bit in bitSequence:
    decimal = decimal * 2 + int(bit)

  return decimal


def generateHenonMap(size):

  x = 0.1
  y = 0.1

  sequenceSize = size * size * 8

  bitSequence = []
  byteArray = []
  TImageMatrix = []

  for i in range(sequenceSize):

    xN = y + 1 - 1.4 * x**2 # Formule Henon Map.
    yN = 0.3 * x


    x = xN
    y = yN 

    if(xN <= 0.3992): # On convertit les valeurs des x en 0 ou 1
      bit = 0
    else:
      bit = 1



    try: 
      bitSequence.append(bit)
    except:
      bitSequence = [bit]

    if i % 8 == 7:
      decimal = dec(bitSequence)

      try:
        byteArray.append(decimal)
      except:
        byteArray = [decimal]

      print(bitSequence, decimal)

      bitSequence = []

      byteArraySize = size * 8

      if(i % byteArraySize == byteArraySize - 1):
        print(byteArray)
        
        try:
          TImageMatrix.append(byteArray)
        except:
          TImageMatrix = [byteArray]
        print(len(byteArray), byteArray)

        byteArray = []

  return TImageMatrix

# Merci à sathwikaileneni.

def pixelManipulation(size, imageName):
    imageMatrixs = imageMatrix(imageName)
    print("ImageMatrix Rows : %d Cols : %d " % (len(imageMatrixs), len(imageMatrixs[0])))
    transformationMatrix = generateHenonMap(size)
    print("Transformation Matrix Rows : %d Cols : %d" %(len(transformationMatrix),len(transformationMatrix[0])))

    resultantMatrix = []
    for i in range(size):
        row = []
        for j in range(size):
            try:
                row.append(transformationMatrix[i][j] ^ imageMatrixs[i][j])
            except:
                row = [transformationMatrix[i][j] ^ imageMatrixs[i][j]]
        try:
            resultantMatrix.append(row)
        except:
            resultantMatrix = [row]

    print("Pixel Manipulated Values : ")
    for rows in resultantMatrix:
         print(rows)

    im = Image.new("L", (size, size))
    pix = im.load()
    for x in range(size):
        for y in range(size):
            pix[x, y] = int(resultantMatrix[x][y])
    im.save("HenonTransformedImage.bmp", "BMP")
    absPath = os.path.abspath("image/HenonTransformedImage.bmp")
    return absPath