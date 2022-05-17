import keygen as kg
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Programme permettant la génération d'une clé privé
# à l'aide de la logistic map (fonction non linéaire)
# Cette clé privé sera testée sur une image.

# Lecture de l'image

ibijauImg = mpimg.imread('img/Loiseau-Urutau.bmp')

plt.imshow(ibijauImg) # Génération de l'image à l'aide d'une structure.
plt.show() # Permet d'afficher celle-ci.

# Génération de notre clé chaotique.

height = ibijauImg.shape[0]
width = ibijauImg.shape[1] # On récupère dans notre structure les informations t-elle que la hauteur et la largeur.


# Génération de la clé :
# 0.01 : Paramètre d'initialisation.
# 3.95 : Notre mu (ici la suite sera totalement chaotique (cycle très attractif)).
# width*height : On donne la largeur * la hauteur de l'image afin de subsituer chacun des pixels.

key = kg.keygen(0.01, 3.95, height*width)
print(key)


# Subsitution à l'aide d'un XOR

a = 0

# np.zeros va créer une liste vide (initialiser à 0) de la taille de notre image

encryptedImg = np.zeros(shape=[height, width,4], dtype = np.uint8)

for i in range(height):
    for j in range (width):
        encryptedImg[i, j] = ibijauImg[i,j] ^ key[a]
        a += 1

plt.imshow(encryptedImg)
plt.show()
plt.imsave('img/patrick.bmp', encryptedImg)

# Méthode de decryption

a = 0

decryptedImg = np.zeros(shape=[height, width,4], dtype = np.uint8)

for i in range(height):
    for j in range(width):

        # On refait un XOR par dessus afin de revenir en arrière.
        decryptedImg[i, j] = encryptedImg[i, j] ^ key[a]
        a += 1

#print(key)
plt.imshow(decryptedImg)
plt.show()
plt.imsave('img/truc.bmp', decryptedImg)
