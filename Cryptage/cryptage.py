from PIL import Image
import os, random

def creer_masque():

    """
    Créer un masque pour une image donnée. 

    Paramètre : 
    None

    Retourne : 
    ImageObject
    """

    for file in os.listdir("Input"):
        if file.endswith(".jpg") or file.endswith(".png"):
            img = Image.open("Input/"+file)
            taille = img.size
            
            masque = Image.new("RGB", taille, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            largeur, hauteur = masque.size
            for x in range(largeur):
                for y in range(hauteur):
                    couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    masque.putpixel((x, y), couleur)

            masque.save("Masque/masque_"+file, "PNG")



def crypter():

    """
    Décrypte une image donnée avec un masque donnée.

    Paramètre : 
    None

    Retourne : 
    ImageObject
    """

    for file in os.listdir("Input"):
        if file.endswith(".jpg") or file.endswith(".png"):
            img = Image.open("Input/"+file)
            masque = Image.open("Masque/masque_"+file)
            taille = img.size
            img_crypt = Image.new("RGB", taille, (0, 0, 0))
            largeur, hauteur = img_crypt.size
            for x in range(largeur):
                for y in range(hauteur):
                    pixel = img.getpixel((x, y))
                    pixel_masque = masque.getpixel((x, y))
                    pixel_crypt = (pixel[0] ^ pixel_masque[0], pixel[1] ^ pixel_masque[1], pixel[2] ^ pixel_masque[2])
                    img_crypt.putpixel((x, y), pixel_crypt)
            img_crypt.save("Output/crypt_"+file, "PNG")
            print("Votre image a bien été cryptée ! Utilisez le masque et la fonction décrypter du programme pour décrypter votre image.")

        else : 
            print("Vous avez des fichiers non pris en charge par le programme.\nCe programme prend uniquement des fichiers au format PNG ou JPG")
            exit()



def decrypter():
   
    """
    Créer une image cryptée avec des pixels "aléatoire".

    Paramètre : 
    None

    Retourne : 
    ImageObject
    """

    for file in os.listdir("Input"):
        if file.endswith(".jpg") or file.endswith(".png"): 
            if file.startswith("crypt_"):
                img_crypt = Image.open("Input/"+file)
                masque = Image.open("Masque/masque_"+file[6:])
                taille = img_crypt.size
                img_decrypt = Image.new("RGB", taille, (0, 0, 0))
                largeur, hauteur = img_decrypt.size
                for x in range(largeur):
                    for y in range(hauteur):
                        pixel_crypt = img_crypt.getpixel((x, y))
                        pixel_masque = masque.getpixel((x, y))
                        pixel_decrypt = (pixel_crypt[0] ^ pixel_masque[0], pixel_crypt[1] ^ pixel_masque[1], pixel_crypt[2] ^ pixel_masque[2])
                        img_decrypt.putpixel((x, y), pixel_decrypt)
                img_decrypt.save("Output/decrypt_"+file[6:], "PNG")
                print("L'image a été decryptée avec succés !")
        else : 
            print("Vous avez des fichiers non pris en charge par le programme.\nCe programme prend uniquement des fichiers au format PNG ou JPG")
            exit()



os.system("cls")
print("Bienvenue dans le programme de cryptage d'image !")
print("Veuillez placer vos images à crypter ou à decrypter dans le dossier Input.")
print("Pour le cryptage, des masques seront créés dans le dossier Masque\nPour le décryptage, placez manuellement vos/votre masque/s dans le dossier Masque.")

mode = int(input("\n\n1. Crypter une image \n2. Décrypter une image \n3. Quitter \n\nChoix : "))
match mode:
    case 1: 
        creer_masque()
        crypter()
    case 2:
        decrypter()
    case 3:
        print("Au revoir !")
        exit()
    

#TODO 
# Gérer l'expetion ou il n'y a aucun masque ou le masque ne correspond pas 
# Sélection des fichers à crypter/décrypter ?
# Gérer l'exception ou il n'y a pas d'image à décrypter/à crypter
# Pixel art ? 
