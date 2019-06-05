import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from parametres import *


"""
Classe TabAffichageCoupes, hérite de la classe QWidget uniquement pour pouvoir l'exécuter indépendemment
Cette classe permet de gérer la fenêtre Qt, mais elle peut aussi être utilisée comme un onglet dans une autre fenêtre
@author Maylis et Alexandre
"""
class TabAffichageCoupes(QWidget) :
    """
    Constructeur, crée le contenu de l'onglet
    """
    def __init__(self, parent=None) :
        if __name__ == '__main__' :
            super(TabAffichageCoupes, self).__init__(parent) # Appel du constructeur de QWidget, uniquement pour pouvoir l'exécuter indépendemment
        
        # Création d'un contenant de l'onglet
        self.grille=QGridLayout()
        
########### Barres de scroll
        
        label_temps = QLabel("Temps")
        
        # Défilement de la couche X
        self.barreScrollAxeX = QScrollBar()
        self.barreScrollAxeX.setMaximum( INTERVALLE_YZ - 1 )
        self.barreScrollAxeX.valueChanged.connect( self.changeImages )
        
        # Défilement de la couche Y
        self.barreScrollAxeY = QScrollBar()
        self.barreScrollAxeY.setMaximum( INTERVALLE_XZ - 1 )
        self.barreScrollAxeY.valueChanged.connect( self.changeImages )
        
        # Défilement de la couche Z
        self.barreScrollAxeZ = QScrollBar()
        self.barreScrollAxeZ.setMaximum( INTERVALLE_XY - 1 )
        self.barreScrollAxeZ.valueChanged.connect( self.changeImages )
        
        # Défilement temporel
        self.barreScrollTemps = QScrollBar(Qt.Horizontal)
        self.barreScrollTemps.setMaximum( NB_IMGS / INTERVALLE_XY - 1 )
        self.barreScrollTemps.valueChanged.connect( self.changeImages )
        
        # Scroll Bar des axes
        label_axex=QLabel("X")
        label_axey=QLabel("Y")
        label_axez=QLabel("Z")
        
        # Ajout des barres de scroll 
        self.grille.addWidget(self.barreScrollTemps,3,1)
        self.grille.addWidget(self.barreScrollAxeX,2,2)
        self.grille.addWidget(self.barreScrollAxeY,2,3)
        self.grille.addWidget(self.barreScrollAxeZ,2,4)
        
######## Images

        # Création d'un contenant pour les images 
        contenant_widget=QWidget()
        contenant_grille=QGridLayout()
        
        
        self.label_image_xy = QLabel()
        self.label_image_yz = QLabel()
        self.label_image_zx = QLabel()
        
        self.label_image_xy.setFixedSize(240,240)
        self.label_image_yz.setFixedSize(240,500)
        self.label_image_zx.setFixedSize(240,500)
        

        self.valeur_temps=QLabel("Temps : 0")
        self.valeur_X=QLabel("X : 0")
        self.valeur_Y=QLabel("Y : 0")
        self.valeur_Z=QLabel("Z : 0")


        self.changeImages(0)
        
        # Ajout des images dans le contenant à images
        contenant_grille.addWidget(self.label_image_xy,5,2)
        contenant_grille.addWidget(self.label_image_yz,2,3)
        contenant_grille.addWidget(self.label_image_zx,2,1)
        contenant_widget.setLayout(contenant_grille)
        
        # Textes correspondant aux images
        texte_xy=QLabel("Image (x,y)")
        texte_yz=QLabel("Image (y,z)")
        texte_zx=QLabel("Image (z,x)")
        contenant_grille.addWidget(texte_xy,3,2)
        contenant_grille.addWidget(texte_yz,1,3)
        contenant_grille.addWidget(texte_zx,1,1)

        # Image des axes
        image_axes = "axesxyz.png"
        label_image_axes = QLabel()
        label_image_axes.setPixmap(QPixmap(image_axes))
        contenant_grille.addWidget(label_image_axes,2,2)
        
        
        # Ajout du contenant d'images dans la grille globale
        self.grille.addWidget(contenant_widget,2,1)

######## Positions actuelles x,y,z et temps
        horizontal_layout=QHBoxLayout()
        
        
        horizontal_layout.addWidget(self.valeur_temps)
        horizontal_layout.addWidget(self.valeur_X)
        horizontal_layout.addWidget(self.valeur_Y)
        horizontal_layout.addWidget(self.valeur_Z)
        

        self.grille.addLayout(horizontal_layout,1,1)
        
        if __name__ == '__main__' :
            self.setLayout(self.grille) # Definit notre grille comme grille à utiliser, uniquement pour pouvoir l'exécuter indépendemment
    
    """
    Accesseur à la grille de l'onglet
    @return La grille de l'onglet, c'est à dire sont contenu
    Cette grille est utilisable par : onglet.setLayout( grille )
    """
    def getGrille(self) :
        return self.grille
    
    """
    Gère l'affichage et son actualisatin
    """    
    def changeImages(self, value) :
        print ( "[Debug Imgs] " + str(self.barreScrollTemps.value()) + ", "
                                + str(self.barreScrollAxeX.value()) + ", "
                                + str(self.barreScrollAxeY.value()) + ", "
                                + str(self.barreScrollAxeZ.value()) )
        
        coucheXFormate = format(self.barreScrollAxeX.value(), '04d') # String sur 4 digits
        coucheYFormate = format(self.barreScrollAxeY.value(), '04d') # String sur 4 digits
        coucheZFormate = format(self.barreScrollAxeZ.value(), '04d') # String sur 4 digits
        tempsFormate = format(self.barreScrollTemps.value(), '02d') # String sur 2 digits
        
        # Image axe (x,y)
        image_xy = URL_POUR_IRM + "x_y/" + tempsFormate + "/t_" + tempsFormate + "coupe_xy_" + coucheZFormate + ".pgm"
        width=self.label_image_xy.width()
        height=self.label_image_xy.height()
        self.label_image_xy.setPixmap(QPixmap(image_xy).scaled(width,height,Qt.KeepAspectRatio))

        # Image axe (y,z)
        image_yz = URL_POUR_IRM + "y_z/" + tempsFormate + "/t_" + tempsFormate + "coupe_yz_" + coucheXFormate + ".pgm" 
        width=self.label_image_yz.width()
        height=self.label_image_yz.height()
        self.label_image_yz.setPixmap(QPixmap(image_yz).scaled(width,height,Qt.KeepAspectRatio))
        
        # Image axe (z,x)
        image_zx = URL_POUR_IRM + "x_z/" + tempsFormate + "/t_" + tempsFormate + "coupe_xz_" + coucheYFormate + ".pgm" 
        width=self.label_image_zx.width()
        height=self.label_image_zx.height()
        self.label_image_zx.setPixmap(QPixmap(image_zx).scaled(width,height,Qt.KeepAspectRatio))
        
        
        self.valeur_temps.setText("Temps : " + str(self.barreScrollTemps.value()))
        self.valeur_X.setText("X : " + str(self.barreScrollAxeX.value()))
        self.valeur_Y.setText("Y : " + str(self.barreScrollAxeY.value()))
        self.valeur_Z.setText("Z : " + str(self.barreScrollAxeZ.value()))


"""
Code principal pour démonstration
"""
# Si on est le script principal
# Cela permet de ne pas exécuter ce bloc de codes lorsque ce script est importé par un autre
# Source : https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__' :
    application = QApplication(sys.argv) # Crée un objet de type QApplication (Doit être fait avant la fenêtre)
    fenetre = TabAffichageCoupes() # Crée un objet de type TabAide
    fenetre.setWindowTitle("MODE DÉMONSTRATION") # Définit le nom de la fenêtre
    fenetre.show() # Affiche la fenêtre
    application.exec_() # Attendre que tout ce qui est en cours soit exécuté