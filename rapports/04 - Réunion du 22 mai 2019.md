# R�union du 22 mai 2019

## Participants

Encadrants du projet :
* J. COUSTY : `jean.cousty@esiee.fr`

Participants du projet :
* Cl�ment CHOMICKI : `clement.chomicki@edu.esiee.fr`
* Amaury BARUZY : `amaury.baruzy@edu.esiee.fr`
* Alexandre LEBLON : `alexandre.leblon@edu.esiee.fr`
* Maylis MONTANI : `maylis.montani@edu.esiee.fr`
* Barbara PARE  : `barbara.pare@edu.esiee.fr`

## Compte-rendu de la r�union

###Partie traitement d'image

##### Cl�ment
* Cl�ment n'a pas r�ussi � utiliser la distance euclidienne pour l'int�grer � son programme. Les distances euclidiennes g�n�rent des erreurs �normes l� o� les distances discr�tes permettent de faire ce qu'il souhaite plus facilement et plus efficacement.
* M. Couosty n'est pas convaincu par les distances discr�tes et souhaite que l'on travaille sur les distances euclidiennes, comme il nous l'avait demand� pr�cedemment. Il pense que cela nous posera des probl�mes dans l'analyse des grains de sable en 3 dimensions. M. Cousty nous recommande d'avoir les distances euclidiennes sous la main et nous envoie son code afin qu'on puisse comparer nos r�sultats aux siens et qu'on essaie de l'int�grer malgr� tout.
* Cl�ment utilise une boucle while sous Python pour fusionner les formes trop proches par rapport � leur taille pour �tre des grains diff�rents. Il est entrain de r�impl�menter ce code en C pour le rendre plus rapide, car son programme fonctionne d�j� bien mais reste un peu lent. 
* M. Cousty n'y voit pas d'objections et pense que c'est bien qu'on continue sur cette voie.
* Cependant, M. Cousty pense que nous devrions d�s � pr�sent nous attaquer aux images 3D, car l'analyse des images 2D n'�tait l� que pour se faire la main sur le probl�me. Cependant, il souhaite que nous continuons � travailler sur les images 2D jusqu'� l'obtention d'un r�sultat. Techniquement, ce que nous avons impl�ment� avec la librairie 'Pink' devrait s'�tendre au probl�me en 3D. Il nous a parl� de deux type d'images 3D que nous devrons g�n�rer : 
	* Volume 3D � un temps donn�
	* Coupe 2D au cours du temps g�n�r� comme  un volume 3D
* M. Cousty est de mani�re g�n�rale convaincu que la m�thodologie classique est bien comprise et mise en oeuvre. Nous devons maintenant produire des images lisibles par les op�rateurs de la librairie 'Pink' pour voir s'il y a une chance que cela fonctionne en 3D.


#### Barbara
* Barbara voulait faire la correspondance entre les diff�rentes couches de nos images apr�s l'analyse individuelles des coupes 2D. 
* M. Cousty ne veut pas qu'on fasse le lien entre les images 2D, il veut qu'on utilise directement les images en 3D et qu'on �tende notre m�thode de s�paration des grains de sable en 3D. En effet, le probl�me de s�paration de grain de sable se retrouvera en 3D, car les grains se touchent au milieu de nos couches. Ce sera plus rapide et plus efficace de travailler directement en 3D puis 4D.
* Une fois qu'on aura une segmentation, il faudra utiliser les outils '3Dview' ou '3Dsegment' pour s�lectionner un grain � un moment donn� et v�rifier qu'il a bien une forme de 'ballon'.


### Partie interface / Repr�sentation

* Nos devrons utiliser l'ensemble de voxels pour g�n�rer une repr�sentation de la surface des grains de sable (surface renderig (?)). L'outil '3Dview' prendra les images pgm en niveau de gris et d'en extraire le format 3D puis l'affichage vtk. 
* Amaury a fait un millefeuille de l'affichage des couches. 
* Visualisation image 3D puis 4D : M. Cousty dit que c'est bien mais qu'il faudrait pousser plus que �a et faire un rendu de coupe dans les 3 dimensions, suivant les axes (x,y), (y,z) et (z,x). Il existe un outil de la librairie 'Pink' qui permet d'afficher les trois coupes simultan�ment et il veut qu'on y ajoute un curseur suivant les coupes pour voir bouger. 
* Rendu des grains de sable en 3D : M. Cousty explique qu'il faut voir les images qu'on a comme des petits cubes en 3D qui composent l'image 3d mais contenu dans les coupes 2D. Dans la librairie 'Pink', il existe une fonction '2Dto3D' permettant d'attrapper les diff�rentes couches. Il a aussi parl� de 'catpgm' qui permet � partir de plusieurs images 2D de faire une image 3D.