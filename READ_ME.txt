Introduction :
ce projet c'est un tp qui represent une algorithme chang et robert v1
c'est une algorithme de l'election

Comment Travaille :
on as besoin d'un reseau on anneau chaque noeud connait sont voisin gauche on as realiser cette topologie on TP N06
tout les noud participe dans l'election
chaque noud env sont id a son voisin c'est l'id du node < a l'id recever le noud envoier sont id et sont port sinon
envoier l'id est le port recever
cette algorithme termine quand l'id et port du node et le meme quand l'id et port du message recever
et a la fin devenir le mettre du reseau

comment executer : 
on as bessoin du noud connecter
on auvre au moins 2 terminaux est on ecrit le code suivant

..\Election\> pythone Node.py [numPort] [token] 

[numPort] : numero du port est de type entier 
[token] : si egal a 1 : le node declanche une election est le processuse commence 0 : sinon

le dossier images contient example d'execution

Gestion des Erreur :
tous les optimisation est les perfermance du TP 06 est realiser on ce projet le module [Checking.py] il contien du methode pour garenti 
le type du port est nombre de parametre passer et ausser si le port est disponible au deja pris par notre noud
