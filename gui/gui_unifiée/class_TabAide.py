import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import codecs


"""
PARAMETRES
"""
FICHIER_CONTENU_AIDE = 'contenu_aide/'


"""
Classe TabAide, hérite de la classe QWidget uniquement pour pouvoir l'exécuter indépendemment
Cette classe permet de gérer la fenêtre Qt, mais elle peut aussi être utilisée comme un onglet dans une autre fenêtre
@author Maylis et Alexandre
"""
class TabAide(QWidget) :
    """
    Constructeur, crée le contenu de l'onglet
    """
    def __init__(self, parent=None) :
        if __name__ == '__main__' :
            super(TabAide, self).__init__(parent) # Appel du constructeur de QWidget, uniquement pour pouvoir l'exécuter indépendemment
        
        # Création d'un layout
        self.layout = QGridLayout()

        # Création d'onglets dans la page d'aide
        onglets = QTabWidget()
        onglets.setTabPosition(2)
        onglets.setTabShape(1)

        aide_ongl = QWidget()
        aide_onglet1 = QWidget()
        aide_onglet2 = QWidget()
    
        # Dictionnaire des onglets de la page d'aide
        self.ongl_aide = { 'aide_ongl' :    [aide_ongl,     "Introduction", 'Aide_generale.html'] , 
                           'aide_onglet1' : [aide_onglet1 , "Aide Onglet1", 'coucou.html'       ] , 
                           'aide_onglet2' : [aide_onglet2 , "Aide_Onglet2", 'salut.html'        ] }
        
        # Ajout dynamique des onglets à la page d'aide
        for ongl in self.ongl_aide :
            onglets.addTab(self.ongl_aide[ongl][0], self.ongl_aide[ongl][1])
            self.contenuOngletAide(ongl)
        
        # Ajout du conteneur d'onglets dans la grille et du layout dans l'onglet Aide de la fenêtre
        self.layout.addWidget(onglets)
        
        if __name__ == '__main__' :
            self.setLayout(self.layout) # Definit notre grille comme grille à utiliser, uniquement pour pouvoir l'exécuter indépendemment
    
    """
    Accesseur à la grille de l'onglet
    @return La grille de l'onglet, c'est à dire sont contenu
    Cette grille est utilisable par : onglet.setLayout( grille )
    """
    def getGrille(self) :
        return self.layout
    
    """
    Affiche dans l'onglet indiqué le contenu du fichier .html associé
    """    
    def contenuOngletAide(self, nom_onglet) :  
        # Contenant avec barre de scroll
        zone_de_texte = QHBoxLayout()
        scroll_area = QScrollArea()
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setWidgetResizable(True)
        
        # Ouverture du fichier contenant l'aide écrite au format HTML
        lien_fichier = FICHIER_CONTENU_AIDE + self.ongl_aide[nom_onglet][2]
        if os.path.isfile( lien_fichier ) : # Si le chemin d'accès existe
            fichier = codecs.open(lien_fichier, 'r', encoding='utf-8')
            texte = QLabel(fichier.read())
        else :
            texte = QLabel("Le fichier suivant est manquant : " + lien_fichier)
        
        # Ajutement de la forme du texte à la taille de la fenêtre
        texte.adjustSize()
        texte.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        texte.setWordWrap(True)
        texte.setAlignment(Qt.AlignJustify)
        scroll_area.setWidget(texte)
        
        # Ajout dans le contenant et dans l'onglet correspondant
        zone_de_texte.addWidget(scroll_area)
        self.ongl_aide[nom_onglet][0].setLayout(zone_de_texte)


"""
Code principal pour démonstration
"""
# Si on est le script principal
# Cela permet de ne pas exécuter ce bloc de codes lorsque ce script est importé par un autre
# Source : https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__' :
    application = QApplication(sys.argv) # Crée un objet de type QApplication (Doit être fait avant la fenêtre)
    fenetre = TabAide() # Crée un objet de type TabAide
    fenetre.setWindowTitle("MODE DÉMONSTRATION") # Définit le nom de la fenêtre
    fenetre.show() # Affiche la fenêtre
    application.exec_() # Attendre que tout ce qui est en cours soit exécuté