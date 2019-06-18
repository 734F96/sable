# CE QU'ON A FAIT
* On a r�uni interface et traitement d'images


* Maylis a am�lior� le syst�me d'affichage des coupes 


* On peut visualiser les diff�rentes �tapes du traitement et afficher la trajectoire du grain cliqu�





# � FAIRE 


* Il serait pas mal d'indiquer o� se situent les coupes par rapport aux autres (mais nous n'avons pas le temps

)
* Changer les couleurs de la carte des distances pour l'adapter aux daltoniens, colorblind...
* Donner une couleur qui serait en rapport avec le temps (gradiant de couleur)


* Simplifier les maillages (utiliser decimate (in, r�duction, out) qui supprime des triangles) pour acc�l�rer le temps de process (on peut faire avec ou sans perte d'info selon si c'est important ou non)


* Utiliser meshregul pour avoir des grains comportements sph�riques (pas tr�s utile vu les grains qu'on a deja (mcubes fait d�j� un lissage des grains))


* Mentionner au jury (au jdp) et dans le rapport qu'on peut avoir acc�s � la vitesse des grains au cours du temps et � leur acc�l�ration vu qu'on a leur position (on peut aussi avoir la vitesse moyenne,...). Tout �a est utile pour l'analyse du mouvement des grains. Regarder toutes ces valeurs avant le jdp.

* On peut extraire les grains qui touchent le bord ou examiner les trajectoires pour voir s'il y en a des bizarres (qu'on ne connais pas, etc)
* Virer les grains sur les bords pour avoir des jolies images 3D (utiliser enframe ou frame et geodilate(binaire, marqueur, -1)). Dans geodilate -1 est le nombre d'it�ration pour dire qu'on le fait � l'infini. �a va extraire les composantes connexes blanches qui sont marqu�es par chacun des coins du bord


* Changer le nom de l'onglet VTK et l'onglet visualisation graphique ainsi que le mille feuilles (Visualisation 3D, Trajectoire des grains, Visualisation mille feuilles par ex)


* Dans l'onglet aide ou dans un onglet "� propos"/"Objectifs" remettre en contexte le projet en reprenant ce qu'avait �crit Yukiko dans la page de pr�sentation du projet 





# ON EST EN TRAIN DE 

* V�rifier si les trajectoires des grains que l'on a sont les bonnes en superposant des images g�n�r�es a partir des r�sultats aux images 3D g�n�r�es a partir des coupes originales


* Changer le contenu des onglets d'aide pour y expliquer comment on a obtenu telle ou telle image





# POUR LA PR�SENTATION 
* On peut pas tout d�tailler donc aborder de fa�on globale et valoriser le projet en montrant que ce qu'on a r�alis� est important dans son contexte (en quoi �a va aider d'autres personnes que nous pour faire du traitement d'images dans le cadre de notre cursus a l'ESIEE,...) 
* Rafraichir la m�moire du jury en rappelant le contexte tout en restant le plus simple possible (ne pas �tre trop technique) 
* Ne pas s'interdire de faire une descente technique (c'est important) mais ne pas s'y perdre et dire pourquoi c'est important 


* Identifier et mettre en valeur ce qui est le plus int�ressant pour nous dans ce projet (ce qu'on a le plus aim� apprendre/faire dans le projet)

* Avoir une r�flexion sur comment on a fonctionn� en r�u, comment on s'est organis� (r�partition des taches, etc)


* R�p�ter la pr�sentation, se chronometrer