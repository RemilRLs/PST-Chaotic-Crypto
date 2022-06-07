from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os
from turtle import width
import keygen as kg
import Henon as hn
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from tkinter import Menu

from PIL import ImageTk, Image

def callbackLogistic(menu):
    global chooseUser
    chooseUser = menu.entrycget(0, "label")
    print(chooseUser)

def callbackHenon(menu):
    global chooseUser
    chooseUser = menu.entrycget(1, "label")
    print(chooseUser)

def callbackLorenz(menu):
    global chooseUser
    chooseUser = menu.entrycget(2, "label")
    print(chooseUser)
    

def encrypt_file(filename, yesorno, encryptFile):

    global imageHenon

    if(yesorno):

        if(chooseUser == 'Logistic Map'):
    
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
            #key = kg.Henonmap(0.001, 0.2, 1.4, 0.3, height*width)
            #print(key)

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

        if(chooseUser == 'Henon Map'):
            imgToEncrypt = mpimg.imread(filename)
            plt.imshow(imgToEncrypt) # Génération de l'image à l'aide d'une structure.
            plt.show() # Permet d'afficher celle-ci.


            height = imgToEncrypt.shape[0]
            width = imgToEncrypt.shape[1] # On récupère dans notre structure les informations t-elle que la hauteur et la largeur.

            imageHenon = hn.pixelManipulation(width, imgToEncrypt)
 
    else:
        if(chooseUser == 'Logistic Map'):
            plt.imshow(encryptFile)
            plt.show()

            height = encryptFile.shape[0]
            width = encryptFile.shape[1] # On récupère dans notre structure les informations t-elle que la hauteur et la largeur.

            print(height, width)

            key = kg.keygen(0.01, 3.95, height*width)
            
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

        if(chooseUser == 'Henon Map'):
            plt.imshow(imageHenon)
            plt.show()

            height = imageHenon.shape[0]
            width = imageHenon.shape[1] # On récupère dans notre structure les informations t-elle que la hauteur et la largeur.
            print(height, width)

            hn.decryptHenonImage(imageHenon)





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

# Create a menu

menubar = Menu(window)
window.config(menu=menubar)

file_menu = Menu(menubar)

file_menu = Menu(
    menubar,
    tearoff=0
)

file_menu.add_command(label='New')
file_menu.add_command(label='Open...')
file_menu.add_command(label='Close')
file_menu.add_separator()


sub_menu = Menu(file_menu, tearoff=0)
sub_menu.add_command(label='Logistic Map', command=lambda: callbackLogistic(sub_menu)) # On retourne la valeur de notre menu afin de savoir le choix de l'utilisateur.
sub_menu.add_command(label='Henon Map' , command=lambda: callbackHenon(sub_menu))
sub_menu.add_command(label='Lorenz Map' , command=lambda: callbackLorenz(sub_menu))

file_menu.add_cascade(
    label="Choose a Chaotic Map",
    menu=sub_menu
)

file_menu.add_command(
    label='Exit',
    command=window.destroy
)


menubar.add_cascade(
    label="File",
    menu=file_menu
    
)

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