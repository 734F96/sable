import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import numpy

from class_TabGraphique3D import TabGraphique3D
from class_TabMilleFeuille3D import TabMilleFeuille3D
from class_TabMilleFeuilleIRM import TabMilleFeuilleIRM
from class_TabAffichageCoupes import TabAffichageCoupes
from class_TabAide import TabAide

from parametres import *
from parametres_pour_demo import grapheDeDemonstration
    

"""
Classe Fenetre, hérite de la classe QTabWidget (Et plus QWidget vu qu'on veut faire des onglets)
Cette classe permet de gérer la fenêtre Qt avec onglets (Appel de la procédure "addTab()")
"""
class Fenetre(QTabWidget) :
    """
    Constructeur
    """
    def __init__(self, grapheDonne, parent=None) :
        super(Fenetre, self).__init__(parent) # Appel du constructeur de QTabWidget
        
        # Taille minimale de la fenêtre, en pixels
        self.setMinimumSize( QSize(400, 400) );
        
        # Création des onglets de la fenêtre
        self.onglet1 = QWidget()
        self.onglet2 = QWidget()
        self.onglet3 = QWidget()
        self.onglet4 = QWidget()
        self.onglet5 = QWidget() 
        
        # Ajout des onglets à la fenêtre
        self.addTab( self.onglet1, "Visualisation du Graphique" ) 
        self.addTab( self.onglet2, "Mille-feuilles" )
        self.addTab( self.onglet3, "Vision IRM" )
        self.addTab( self.onglet4, "Coupes" )
        self.addTab( self.onglet5, "Aide" )
        
        # Création des objets contenant le contenu de chaque onglet
        grilleOnglet1 = TabGraphique3D(grapheDonne)
        grilleOnglet2 = TabMilleFeuille3D()
        grilleOnglet3 = TabMilleFeuilleIRM()
        grilleOnglet4 = TabAffichageCoupes()
        grilleOnglet5 = TabAide()
        
        # Remplissage des onglets avec les objets ci-dessus
        self.onglet1.setLayout( grilleOnglet1.getGrille() )
        self.onglet2.setLayout( grilleOnglet2.getGrille() )
        self.onglet3.setLayout( grilleOnglet3.getGrille() )
        self.onglet4.setLayout( grilleOnglet4.getGrille() )
        self.onglet5.setLayout( grilleOnglet5.getGrille() )


"""
Code principal pour démonstration
"""
# Si on est le script principal
# Cela permet de ne pas exécuter ce bloc de codes lorsque ce script est importé par un autre
# Source : https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__' :
    application = QApplication(sys.argv) # Crée un objet de type QApplication (Doit être fait avant la fenêtre)
    fenetre = Fenetre( grapheDeDemonstration ) # Crée un objet de type Fenetre
    fenetre.setWindowTitle("MODE DÉMONSTRATION") # Définit le nom de la fenêtre
    fenetre.show() # Affiche la fenêtre
    application.exec_() # Attendre que tout ce qui est en cours soit exécuté
