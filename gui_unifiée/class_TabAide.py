import os
import sys

#from PyQt5.QtCore import *
#from PyQt5.QtGui import *
#from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QTabWidget, QHBoxLayout, QScrollArea, QLabel, QSizePolicy

from class_Parametres import Parametres # Ne sert que si est exécuté séparemment


"""
PARAMETRES
"""
FICHIER_CONTENU_AIDE = './contenu_aide/'
from parametres import DISABLE_IRM


"""
Classe TabAide, hérite de la classe QGridLayout, c'est donc une grille
Cette classe représente le contenu d'une fenêtre PyQt
Elle peut donc aussi être utilisée comme un onglet dans une fenêtre
@author Maylis et Alexandre
"""
class TabAide(QGridLayout) :
    """
    Constructeur, crée le contenu de l'onglet
    """
    def __init__(self, objParams, parent=None) :
        super(TabAide, self).__init__(parent) # Appel du constructeur de QGridLayout
        
        self.objParams = objParams # Ne sert à rien pour le moment
        
        # Création d'onglets dans la page d'aide
        onglets = QTabWidget()
        onglets.setTabPosition(2)
#        onglets.setTabShape(1) # C'est très moche quand même

        aide_ongl = QWidget()
        aide_onglet1 = QWidget()
        aide_onglet2 = QWidget()
        if not DISABLE_IRM : aide_onglet3 = QWidget()
        aide_onglet4 = QWidget()
        aide_onglet5 = QWidget()
        
    
    
        # Dictionnaire des onglets de la page d'aide
        self.ongl_aide1 = { 'aide_ongl' :    [aide_ongl,     "Introduction",                     'aide_generale.html'] , 
                            'aide_onglet1' : [aide_onglet1,  "Aide Trajectoires",                'aide_visu_graph.html'] ,
                            'aide_onglet2' : [aide_onglet2,  "Aide Vue Mille-feuilles",          'aide_millefeuille.html'] }
        if not DISABLE_IRM : self.ongl_aide2 = { 'aide_onglet3' : [aide_onglet3,  "Aide Vue IRM",                     'aide_vision_IRM.html'] }
        self.ongl_aide3 = { 'aide_onglet4' : [aide_onglet4,  "Aide vue Coupes",                  'aide_coupes.html'] ,
                            'aide_onglet5' : [aide_onglet5,  "Aide vue 3D",                      'aide_VTK.html'] }
        
        if not DISABLE_IRM : self.ongl_aide = {**self.ongl_aide1, **self.ongl_aide2, **self.ongl_aide3}
        else : self.ongl_aide = {**self.ongl_aide1, **self.ongl_aide3}
        
        # Ajout dynamique des onglets à la page d'aide
        for ongl in self.ongl_aide :
            onglets.addTab(self.ongl_aide[ongl][0], self.ongl_aide[ongl][1])
            self.contenuOngletAide(ongl)
        
        # Ajout du conteneur d'onglets dans la grille et du layout dans l'onglet Aide de la fenêtre
        self.addWidget(onglets)
    
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
            fichier = open(lien_fichier, 'r', encoding='utf-8')
            texte = QLabel(fichier.read())
            texte.setStyleSheet("QLabel { padding: 20px; margin-top: -40px; }"); # CSS
        else :
            texte = QLabel("Le fichier suivant est manquant : " + lien_fichier)
            texte.setStyleSheet("QLabel { padding: 20px; }"); # CSS
            print( "[Erreur TabAide] " + lien_fichier + " n'existe pas !" )
        
        # Ajutement de la forme du texte à la taille de la fenêtre
        texte.adjustSize()
        texte.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
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
    fenetre = QWidget() # Crée un objet de type QWidget
    fenetre.setWindowTitle("MODE DÉMONSTRATION") # Définit le nom de la fenêtre
    fenetre.setLayout( TabAide( Parametres() ) )
    fenetre.show() # Affiche la fenêtre
    application.exec_() # Attendre que tout ce qui est en cours soit exécuté
