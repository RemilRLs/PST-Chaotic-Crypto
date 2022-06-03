from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os
from turtle import width
import keygen as kg
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np



def encrypt_file(filename, yesorno, encryptFile):

    if(yesorno):
        imgToEncrypt = mpimg.imread(filename)
        plt.imshow(imgToEncrypt) # Génération de l'image à l'aide d'une structure.
        plt.show() # Permet d'afficher celle-ci.


        height = imgToEncrypt.shape[0]
        width = imgToEncrypt.shape[1] # On récupère dans notre structure les informations t-elle que la hauteur et la largeur.


        # Génération de la clé :
        # 0.01 : Paramètre d'initialisation.
        # 3.95 : Notre mu (ici la suite sera totalement chaotique (cycle très attractif)).
        # width*height : On donne la largeur * la hauteur de l'image afin de subsituer chacun des pixels.

        key = kg.keygen(0.01, 3.95, height*width)
        print(key)

        a = 0

        # np.zeros va créer une liste vide (initialiser à 0) de la taille de notre image

        encryptedImg = np.zeros(shape=[height, width,4], dtype = np.uint8)

        for i in range(height):
            for j in range (width):
                encryptedImg[i, j] = imgToEncrypt[i,j] ^ key[a]
                a += 1


        plt.imsave('image/encrypt.bmp', encryptedImg)
        
        encryptFile = encryptedImg
        plt.imshow(encryptFile)
        plt.show()

        return encryptedImg
    
    else:
            
        plt.imshow(encryptFile)
        plt.show()

        height = encryptFile.shape[0]
        width = encryptFile.shape[1] # On récupère dans notre structure les informations t-elle que la hauteur et la largeur.

        print(height, width)

        key = kg.keygen(0.01, 3.95, height*width)
        print(key)
        
        # Génération de la clé :
        # 0.01 : Paramètre d'initialisation.
        # 3.95 : Notre mu (ici la suite sera totalement chaotique (cycle très attractif)).
        # width*height : On donne la largeur * la hauteur de l'image afin de subsituer chacun des pixels.

        a = 0

        
        decryptedImg = np.zeros(shape=[height, width,4], dtype = np.uint8)

        for i in range(height):
            for j in range(width):

                # On refait un XOR par dessus afin de revenir en arrière.
                decryptedImg[i, j] = encryptFile[i, j] ^ key[a]
                a += 1

        plt.imshow(decryptedImg)
        plt.show()
        plt.imsave('image/decrypt.bmp', decryptedImg)







def select_fileEncrypt():
    filetypes = (
        ('text files', '*.bmp'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )


    global encryptFile 
    encryptFile = 1
    encryptFile = encrypt_file(filename, 1, encryptFile)



def select_fileDecrypt():
    filetypes = (
        ('text files', '*.bmp'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )
    
    encrypt_file(filename, 0, encryptFile)


# Creation of the interface.

window = Tk()

# Window Customization.

window.title("Encrypt Chaos")
window.geometry("1080x720") 
window.minsize(480, 360)
window.resizable(False, False)
window.iconbitmap("image/800px-Lorenz_attractor_boxed.ico")
window.config(background="white")

# Encrypt file with chaos.

label_title = Label(window, text= "File Encryption", font=("Arrial bold", 17), bg='white', fg='#0070FF')
label_title.pack(side=TOP)

# Open file encrypt button.

open_buttonEncrypt = Button(
    window,
    text= "Encrypt file",
    command= select_fileEncrypt
    
)

# Decrypt button.

open_buttonDecrypt = Button(
    window,
    text= "Decrypt file",
    command= select_fileDecrypt
    
)


open_buttonEncrypt.pack(expand=True)
open_buttonDecrypt.pack(expand=True)




# Run the application.

window.mainloop()