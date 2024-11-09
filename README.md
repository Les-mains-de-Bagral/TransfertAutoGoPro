# Instructions pour réussir à transférer automatiquement ses fichiers :

## 1 - Télécharger et installer Python
[Lien cliquable Python](https://www.python.org/downloads/) \
Ne pas oublier de cocher "Add python.exe to PATH" comme sur la capture d'écran ci-dessous : \
\
![image](https://github.com/user-attachments/assets/ec9ace10-3870-48e0-bc84-8a3cd3272b8e)
\
## 2 - Installer le package "keyboard"
Ouvrez un terminal de commande en appuyant sur la touche Windows, puis en tapant : \
`cmd`  
Ensuite écrivez la ligne ci-dessous, puis tapez la touche ENTRER \
`pip install keyboard`  

## 3 - Changez la Lettre de votre carte SD
Ouvrez le gestionnaire de disque en tapant : \
`disk`
dans votre outils de recherche windows. \
Branchez votre carte SD à l'odinateur. \
Puis dans l'outil ouvert, identifiez votre carte SD dans la liste du bas, cliquez droit dessus et choisissez "Modifier la lettre de lecteur et les chemins d'accès..." \
![Changement lettre flou 10](https://github.com/user-attachments/assets/97728344-95e6-4eea-9605-fa38b0031a0a)  
Cliquez sur "Modifier..." \
Enfin attribuez la lettre Z, vous pouvez en choisir une autre mais il faudra aussi le modifier dans le programme python, à la ligne : \
`DossierVideo = "Z:/DCIM/100GOPRO" # Dossier des fichiers vidéos source` 

## 4 - Téléchargez les 2 fichiers
### Variante 1
Soit vous les laissez dans le même dossier, il peut être n'importe lequel de votre ordinateur, et tout fonctionnera tel quel.

### Variante 2
Soit vous voulez mettre le programme python (PrgmTransfertAutoGoPro.py) dans un autre dossier différent de celui du .bat. \
Et à ce moment, il faudra modifier le fichier "Exécution-TransfertAutoGopro.bat."\
Pour ce faire, glissez le fichier dans un éditeur de texte (bloc-note par exemple) et à la ligne : \
`::cd /d "G:\Programme"` supprimez le "::" et écrivez le bon chemin vers le dossier dans lequel vous avez déplacé votre programme python. \
Ça pourrait donner par exemple :
`cd /d "C:\Users\Bagral\Desktop"` dans mon cas, si je le mettais sur le bureau.

## 5 - Réglages
Il ne vous reste plus qu'à modifier le dossier de destination des transferts. \
Dans le programme python, modifiez la ligne : \
`CheminDossierVideoDest = "G:/" # Dossier vers lequel on les déplace` pour diriger vos transferts vers le bon dossier. \
Exemple dans mon cas : \
`CheminDossierVideoDest = "C:\Users\Bagral\Videos" # Dossier vers lequel on les déplace` 
