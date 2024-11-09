# Programme de transfert automatique des fichiers d'une Carte SD de GoPro
# Avec réarrangement du nom des fichiers (inversion chapitre et numéro de rush)
# 
# Début le 03/11/2024
#
# Version 2 - 09/11/2024
#
# Par Bagral - LMDB
#


# -*- coding: utf-8 -*-

import os
import shutil
import threading
import keyboard # type: ignore
import time
from datetime import datetime


print("\n\n\n\t\t*** Lancement du programme de transfert automatique des fichiers GoPro *** \n")


## Nom des dossiers
DossierVideo = "Z:/DCIM/100GOPRO" # Dossier des fichiers vidéos source
CheminDossierVideoDest = "G:/" # Dossier vers lequel on les déplace


## Initialisation des variables
NbrFichiersMP4 = 0
TailleFichiersTot = 0
# Globale
GInterrompre = False 


## Fontions 
def AcquisitionClavier(): 
    global GInterrompre # Déclaration en variable globale
    print("\n\t\t==> Appuyez sur 'Espace' pour arrêter à tout moment <== \n")
    while not GInterrompre :
         if keyboard.is_pressed('Space'): #Attente d'appui sur la touche Espace
             GInterrompre = True
             print("\n\t==> Arrêt demandé. Le programme s'arretera à la fin de ce transfert. <==\n")


##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 


## Vérification de l'existence du dossier source (est-ce que la carte est branchée ?)
if  os.path.isdir(DossierVideo) : # Vérification de l'existence du dossier
    print("\n\tDossier source détecté, il contient :")
else :
    print("\n\tDossier source non détecté. Fin du programme.")
    exit()

## Première boucle dans le dossier, pour compter le nombre de fichiers .MP4 et récupérer leur taille
for NomFichier in os.listdir(DossierVideo) : # Parcoure tous les fichiers du dossier
    if NomFichier.endswith(".MP4") :
        NbrFichiersMP4 += 1 # Comptage du nombre de fichiers 
        NomFichierAvecChemin = os.path.join(DossierVideo, NomFichier) # Agrégation du chemin du fichier et de son nom
        TailleFichier = os.path.getsize(NomFichierAvecChemin) // 1024 # Récupération de la taille du fichier en traitement et conversion octets en Ko
        TailleFichier = TailleFichier / 1000 # Conversion octets en Mo
        TailleFichiersTot += TailleFichier # Somme du poids total
        print(f"\t  - {NbrFichiersMP4} :  {NomFichier} \t{TailleFichier:.1f} Mo")

## Affichage du résultat de la boucle
if NbrFichiersMP4 == 0 :
    print("\tRien à importer")
elif NbrFichiersMP4 == 1 :
    print("\t 1 seul fichier MP4 à importer")
else :
    print(f"\t{NbrFichiersMP4} fichiers MP4 à importer")

## Deuxième boucle dans le dossier, pour transferer
if NbrFichiersMP4 != 0 : # Si des fichiers .MP4 ont été détectés

    ## Création du nouveau dossier de destination
    DateHeure = datetime.now().strftime("Rush du %d-%m-%Y %Hh%M") # Obtenir la date et l'heure actuelles
    DossierVideoDestAvecChemin = os.path.join(CheminDossierVideoDest, DateHeure) # Agrégation du chemin du fichier et de son nom
    if  os.path.isdir(DossierVideoDestAvecChemin) : # Vérification de l'existence du dossier
        print("\n\t(Le dossier de destination existe déjà)\n")
    else :
        print("\n\t(Création du dossier de destination)\n")
        os.makedirs(DossierVideoDestAvecChemin) # Création du nouveau dossier

    ## Démarrage du Thread
    ThreadClavier = threading.Thread(target=AcquisitionClavier) # Démarre le thread pour surveiller l'entrée utilisateur
    ThreadClavier.daemon = True  # Permet de fermer le thread lorsque le programme principal se termine
    ThreadClavier.start()

    ## Acquisition du temps au commencement
    TempsDebut = time.time()

    ## Transfert
    for NomFichier in os.listdir(DossierVideo) : # Parcourt tous les fichiers du dossier

        if NomFichier.endswith(".MP4") : # Traitement seul des fichiers .MP4
            print("\n\n\tTraitement de : " + NomFichier)
            NomFichierMP4AvecChemin = os.path.join(DossierVideo, NomFichier) # Agrégation du chemin du fichier et de son nom  

            #Génération du nouveau Nom
            NouveauNomFichierMP4 = NomFichier[0:2] + "-" + NomFichier[4:8] + "-" + NomFichier[2:4] + ".MP4" # Format : GX-0001-01
            NouveauNomFichierMP4AvecChemin = os.path.join(DossierVideoDestAvecChemin, NouveauNomFichierMP4)  # Agrégation du chemin du fichier et de son nouveau nom

            #Déplacement du fichier
            shutil.move(NomFichierMP4AvecChemin, NouveauNomFichierMP4AvecChemin)

            #Suppression du .THM du fichier
            NomFichierTHMAvecChemin = NomFichierMP4AvecChemin.replace(".MP4",".THM")
            if  os.path.isfile(NomFichierTHMAvecChemin) : # Vérification de l'existence du fichier
                os.remove(NomFichierTHMAvecChemin)
                print("\t .THM supprimé") 
            else :
                print("\t .THM introuvable")

            #Suppression du .LRV du fichier
            NomFichierLRVAvecChemin = NomFichierMP4AvecChemin.replace("GX","GL")
            NomFichierLRVAvecChemin = NomFichierLRVAvecChemin.replace(".MP4",".LRV")
            if  os.path.isfile(NomFichierLRVAvecChemin) : # Vérification de l'existence du fichier
                os.remove(NomFichierLRVAvecChemin)
                print("\t .LRV supprimé") # Affichage sans retour à la ligne
            else :
                print("\t .LRV introuvable")

        
        ## Arrete le programme si Interrompre est True
        if GInterrompre : break

    ## Mesure et affichage de la durée
    TempsFin = time.time() # Acquisition du temps à la fin
    Durée = TempsFin - TempsDebut # Calcul de la durée
    #print(f"\tDurée : {Durée:.3f}s") # Affichage Secondes pour vérif en dév

    ## Décomposition de la durée en Heures Minutes Secondes et affichage
    DuréeH = Durée // 3600
    DuréeM = (Durée - DuréeH*3600) // 60
    DuréeS = Durée - (DuréeH*3600 + DuréeM*60)
    print("\n\n\n\tFin du transfert :")
    print("\t  Il a duré   ", end="") # Affichage sans retour à la ligne
    if DuréeH != 0 : print(f" {DuréeH:.0f}h", end="") # Affichage sans retour à la ligne
    if DuréeM != 0 : print(f" {DuréeM:.0f}m", end="") # Affichage sans retour à la ligne
    print(f" {DuréeS:.1f}s", end="") # Affichage sans retour à la ligne
    VTransfert = TailleFichiersTot/Durée # Calcul de la vitesse
    print(f"\t  pour {TailleFichiersTot:.1f} Mo \tsoit {VTransfert:.2f} Mo/s")