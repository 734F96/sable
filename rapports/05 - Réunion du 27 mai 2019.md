# R�union du 27 mai 2019

## Participants

Encadrants du projet :
* J. COUSTY : `jean.cousty@esiee.fr`
* Y. KENMOCHI : `yukiko.kenmochi@esiee.fr`

Participants du projet :
* Cl�ment CHOMICKI : `clement.chomicki@edu.esiee.fr`
* Amaury BARUZY : `amaury.baruzy@edu.esiee.fr`
* Alexandre LEBLON : `alexandre.leblon@edu.esiee.fr`
* Maylis MONTANI : `maylis.montani@edu.esiee.fr`
* Barbara PARE  : `barbara.pare@edu.esiee.fr`

## Compte-rendu de la r�union

### Partie traitement d'image 

* Cl�ment a expliqu� que nous �tions pass� dans l'analyse 3D du mouvement des grains de sable. Nous avons test� l'affichage � l'aide de l'utilitaire "ParaView". M. Cousty nous dit que c'est un bon utilitaire.
* Barbara a g�n�r� les images en 3D et les diff�rentes coupes dans les axes (x,y), (x,z) et (y,z).
* Cl�ment a montr� le gif des coupes avec les couleurs aux profs. Il y a des petites erreurs qui donnent des trous dans l'image, mais en moyenne il y a peu d'erreurs dans ce qu'il a fait.
* Cl�ment est pass� aux distances euclidiennes et a utilis� un param�tre de connexit�.
* Pour visualiser les r�sultats, M. Cousty nous recommande d'utiliser une commande "border" qui prend les bords de l'image segment�e, puis "surimp" (?) qui superpose les bords � l'image d'origine. Cela permet de voir � quoi correspond la coupe.
* M. Cousty veut que nous regardions la s�parattion des grains en 2D+T (c'est � dire regarder la m�me coupe � des temps diff�rents et les empiler). Nous devrions obtenir des genre de cylindres pour les grains qui ne bougent pas dans l'image, et sinon des genre de "rubans" pouvant s'�paissir ou diminuer dans l'image obtenue en 2D+T. REMARQUE : Ceci est une �tape interm�diaire avant d'attaquer le 3D+T, car jusque l� c'�tait relativement facile de passer du 2D au 3D car les outils de la librairie "Pink" fonctionnait de la m�me mani�re, mais quand nous allons passer en 4D, cela risque d'engendrer de nombreux bugs et nous devrons batailler avec python pour r�ussir � obtenir ce que nous voulons. Cette �tape risque de prendre beaucoup de temps.
* Cl�ment a �voqu� le diagramme de Verneuil, et M. Cousty nous a dit que c'�tait strictement �quivalent � ce que nous avions fait (Watershade avec des distances discr�tes (?)). Cependant, Cl�ment n'arrive pas � faire fonctionner l'utilitaire.
* Pour visualiser un grain, il faut faire "select comp" (?), cela permet d'avoir un grain ou plusieurs et de le visualiser en 3D avec l'outil.
* Apr�s avoir visualis� ce que l'on souhaite, on pourra peut �tre diminuer le nombre de triangles affich�s pour avoir plus de visibilit� et s'autoriser � lisser un peu la forme.


### Partie interface graphique 

* Maylis a int�gr� les diff�rents outils dont on parlait � la derni�re r�union dans l'interface. M. Cousty approuve l'interface � onglets mais sugg�re d'ajouter un menu de s�l�ction des datas que l'on souhaite utiliser, et tous les codes d'analyse fonctionnels que Cl�ment et Barbara ont produit pour qu'on puisse y acc�der directement.
* Pour le d�filement des images dans la visualisation en mille-feuille d'Amaury, il faudrait plut�t utiliser les images en niveau de gris, car les couleurs, c'est pas fou.
* Nous devons chercher comme int�grer dans PyQt une autre interface graphique de visualisation 3D (m�me si c'est pas franchement propre) � l'int�rieur d'une Frame par exemple.
* Pour la prochaine fois, il faut vraiment qu'on puisse visualiser en 3D depuis l'interface.
* Amaury se bat avec PyQt et vtk pour avoir l'affichage graphique avec "ParaView".

### Remarque

* M. Cousty ne nous a pas envoy� le code qu'il devait nous envoyer la semaine derni�re mais ne semble pas vouloir nous l'envoyer finalement.
* Sur les deux prochaines semaines, M Cousty ne sera pas l�, il n'y aura que Mme Kenmochi.
* Pour modifier une librairie de "Pink", M. Cousty nous recommande de recopier le code dans un fichier s�par�, de modifier ce que l'on souhaite et de l'appeler sous un autre nom.
