# RPG-Project

RPG - Project by Théophile, Alex, Lucas and William

Main Programmer : Théophile Aumont

Co-Dev/Game Designer : Alexander Grot, Lucas Marcinkowski, William Scian


Projet de rpg programmé en python avec le module pygame, pyautogui et json.

 # Explication du projet

Le but de ce projet n'était pas seulement d'offir un rpg jouable par le joueur mais aussi de le laisser créer ses propres environnements, avec un éditeur de map performant, le tout accessible avec des configurations peu performantes, spéciallement sur le micro-ordinateur RaspBerry Pi. Ainsi, il a fallut redoubler d'efforts pour créer un gestionnaire de collision performant, le tout le plus optimisé possible afin de ne pas demander trop de performances.

Ainsi, vous aurez une mini-map de base avec un mini-jeu : trouvez le moyen de tuer un petit monstre enfermé dans un enclos. Il s'agit d'un mini-exemple de ce que l'outil peut proposer. En effet, vous pouvez changer de mode de jeu et choisir l'éditeur de map. 

Vous arriverrez sur un écran noir où vous créerez tout de A à Z. Le tout divisé en 3 onglets : 
1. Vous construirez le sol, route, herbe ou encore pavés.
2. Le deuxième onglet concerne la décoration, d'une maison à un enclos, vous pouvez choisir de mettre ou vous voulez des arbres, des hautes herbes ou encore des rochers.
3. Enfin le dernier onglet sert à créer des collision afin que le joueur ne puisse pas passer par dessus les arbres ou les maisons.

Aussi, vous pouvez enregistrer la map que vous avez créer et y rejouer ou la rééditer.
Pour ce faire, vous pourrez y jouer en allant sur le mode de jeu map loader, ici vous pouvez consulter toutes les maps que vous avez enregistrer, y jouer, les éditer ou encore les supprimer, enfin vous pouvez rétablir le mode de jeu de base à l'aide d'un petit bouton en bas à gauche.


# Technologie utilisée

A l'aide de la puissance des matrices (listes de listes en réalité) vous pouvez charger des maps en un court instant et y jouer sans utiliser trop de performances. En fait, juste avant de jouer, un scanner de liste scannes toutes les listes avec des boucles for et en fonction du chiffre qu'il y à chaque case on met un bloc différent. Ainsi, l'ordinateur n'a besoin de charger la map qu'une seule fois et ensuite il a juste à afficher les sprites. Aussi, pour gérer les collisions du joueur, il y a une liste représentant les endroits où le joueur peut se déplacer ou non. Le joueur a donc un index représentant sa position dans la liste et à chaque fois qu'il veut se déplacer dans une direction, l'ordinateur vérifie que l'index suivant est accessible (différent de 3).

