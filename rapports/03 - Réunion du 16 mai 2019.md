# R�union du 16 mai 2019

## Participants 

Encadrants du projet :
* J. COUSTY : `jean.cousty@esiee.fr`
* Y. KENMOCHI : `yukiko.kenmochi@esiee.fr`

Participants du projet :
* Cl�ment CHOMICKI : `clement.chomicki@edu.esiee.fr`
* Amaury BARUZY : `amaury.baruzy@edu.esiee.fr`
* Alexandre LEBLON : `alexandre.leblon@edu.esiee.fr`
* Maylis MONTANI : `maylis.montani@edu.esiee.fr`

## Compte-rendu de la r�union

### Ce que nous avons fait
* Cl�ment et Barbara ont appliqu�s le watershade et corrig� certains d�fauts de s�paration des grains de sable. Ils ont aussi cherch� de nouveaux outils pour r�gler les probl�mes g�n�r�s par le watershade pour obtenir une qualit� optimale. 
* Amaury s'est charg� de la visualisation graphique de points dans un espace 3D. 
* Maylis a cr�� une interface graphique permettant d'afficher plusieurs onglets et de g�n�rer une aide sp�cifique � chaque onglet. 
* Alexandre a fait la liste des outils restant � impl�menter pour les rendre accessibles depuis l'interface et a aid� Maylis � trouver les bons outils pour l'interface graphique. 

### Partie traitement d'image

Cl�ment nous a expliqu� qu'il avait fini d'utiliser l'outil du watershade, mais qu'un probl�me subsistait : certains grains de sables ne sont pas parfaitement sph�rique ce qui engendre sur certaines coupes 2D une s�paration innexistante. Sa solution consiste � r�cup�rer les barycentres des cercles et de comparer l'aire sur diff�rentes images pour voir si celle-ci est coh�rente. Cela permettrait de r�assembler les grains qui n'auraient pas d� �tre s�par�s.

M. Cousty nous a dit qu'il ne fallait pas s'int�resser aux grains tronqu�s aux extr�mit�s des images car une image compl�te ne comporterait aucun grain de sable tronqu�.

Nous avons montr� aux professeurs encadrants des images de s�paration et de rep�rage des barycentres. Les donn�es n'�tant pas parfaitement sph�riques, nous obtenons deux minimas sur la carte des distances. M. Cousty nous a expliqu� un autre moyen que celui de Cl�ment qui consiste � reboucher les minimas qui ne correspondent pas � ce qu'on attend en supprimant les minimas les moins significatifs en fonction de leur pertinence selon leur taille (en pixels), profondeur, ou volume. Diff�rents outils sur 'Pink' permettent de faire du filtrage morphologique comme la fermeture par aire de param�tre 'x' ou en anglais 'area opening' ; la fermeture par volume avec l'outil 'vol minima' ou 'vol maxima'. De mani�re g�n�rale, les outils de la librairie 'Pink' sont lin�aires et sont donc tr�s efficaces.

D'autre part, M. Cousty nous a demand� d'aller voir l'outil 'pgmtolist' du module 'geometry complenator' pour �tablir une liste de centres des grains de sables et ne plus avoir besoin de repasser plusieurs fois sur la m�me image, car notre programme met du temps � s'ex�cuter.

Pour �tablir les distances, nous avons utilis� '4-dist' (?) mais M. Cousty nous recommande d'utiliser '3-dist' car m�me si les distances ne sont pas enti�res, leur distances euclidiennes quadratiques le sont. Pour le probl�me de format qu'engendre l'utilisation de l'outil '3-dist', il nous est recommand� d'aller chercher un outil dans la librairie 'Pink' qui nous permettrait de passer d'une image de carte de distance � une image dans laquelle les pixels sont cod�s en 'long to byte'. M. Cousty nous dit que la param�tre qu'il a utilis� �tait '0'.

Pour le moment, Cl�ment a utilis� l'outil 'select' pour selectionner un grain. M. Cousty nous recommande d'utiliser des labels qui rep�reront de mani�re unique un grain dans une image 2D ou 3D, ce qui permettrait d'am�liorer l'efficacit� de notre programme.

Nous n'avons pas encore commenc� � travailler sur les images 3D mais uniquement sur l'analyse des images 2D. Nous devons donc pour la prochaine fois avoir r�ussi � repr�senter en 3D les grains de sable, gr�ce notamment � l'outil '3D view' qui pourrait nous �tre utile par ailleurs dans l'interface.


### Partie Interface graphique

M. Cousty nous demande de g�n�rer le maillage de nos donn�es extraire la surface de la structure � partir d'une image 3D binaire. Le format utilis� dans 'Pink' pour ce genre d'outil est 'vtk' qui correspond � une liste de points de triangles d�finissant la surface d'un grain de sable. Dans la librairie 'Pink' nous pouvons utiliser 'mcube' qui permet de g�n�rer un maillage � partir d'images en niveau de gris.


### Questions

**Quels outils vous semblent n�cessaires dans l'interface ?**
* Visualisation des coupes des images
* Cliquer et r�cup�rer les caract�ristiques du grain (coordonn�es dans l'espace, taille...) 
* Avoir acc�s � des informations g�n�rales (nombre de grains, taille moyenne, mouvement global...)
* Pouvoir zoomer dans l'espace 3D
* Pouvoir sauvegarder les r�sultats (caract�ristiques, vid�os du mouvement dans un format classique)
* Pour la repr�sentation du mouvement, avoir l'interpolation (on force le mod�le � passer � travers un certain nombre de points de contr�le)
* Ce serait bien de pouvoir visualiser la trajectoire et l'orientation/la rotation des grains (mais pour des grains sph�riques, c'est compliqu�) � l'aide de fl�ches sur les grains
