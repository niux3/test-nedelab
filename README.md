# test-nedelab

## glob

Pas besoin d'écrire de code Python dans ce mini-cas, du pseudo-code clair suffit.
Vous voulez écrire un interpréteur d'expressions glob.
Une expression glob est une chaine de caractères utilisée pour retrouver les fichiers d'un filesystem qui répondent à certains critères. Par exemple, pour l'expression glob "/home/me/*2022*/*.log", l'interpréteur doit renvoyer tous les fichiers du filesystem dont le nom finit pas ".log" et qui sont situés à la racine d'un dossier qui contient la chaîne de caractères "2022" et qui lui-même se situe dans /home/me/. Vous l'aurez peut-être deviné, le symbole "*" signifie "n'importe quel caractère sauf '/'". "*" est le seul caractère spécial du langage glob que l'on utilisera dans ce mini-cas (oublions "?" et "[]").
Pour vous aider, vous avez à votre disposition la fonction fnmatch(path, pattern) qui renvoie True si le chemin d'accès "path" répond au critère décrit par "pattern" (par exemple, fnmatch("2022-12-03", "*2022*") == True parce que "2022-12-03" contient "2022", mais fnmatch("2022-12-03", "*2022") == False car "2022-12-03" ne finit pas par "2022").
Donnez l'algorithme qui prend en entrée une expression glob, et renvoie la liste de fichiers du filesystem qui correspondent à l'expression glob.

## archivage

Le code de l'API est dans le fichier app.py.
L'API a été développée en interne par votre entreprise et tourne sur l'un de ses serveurs. Elle permet à un utilisateur distant de déposer des fichiers sur le serveur sur lequel tourne l'API, et de les télécharger plus tard.
L'API contient 2 routes :

une route qui renvoie le contenu d'un fichier (GET /file)
une route qui dépose un fichier (PUT /file)

L'URL de l'API a été donnée au comptable de l'entreprise pour lui permettre d'archiver les factures de l'entreprise et de les retrouver plus tard. Pour simplifier, supposons que le comptable est le seul à avoir accès à l'API (il n'y a donc pas de système d'authentification, et nous n'attendons pas dans ce mini-cas que soit développé un tel système).
Mais nous avons un problème : le comptable est aussi un bon informaticien et n'est pas toujours digne de confiance.
Analyser le code de l'API et décrivez en quelques phrases une ou deux failles de sécurité béantes.
En particulier, dites comment le comptable pourraient les exploiter pour sérieusement embêter votre entreprise.
Ensuite, réécrivez le code en corrigeant les failles de sécurité.

## distant shell

Le code de l'API est dans le fichier app.py.
L'API a été développée en interne par votre entreprise et tourne sur l'un de ses serveurs. Elle permet de lancer à distance n'importe quelle commande shell sur le serveur sur lequel tourne l'API.
L'API contient une seule route :

- une route qui permet d'exécuter une commande donnée en paramètre (POST /exec)

Pour éviter que n'importe qui puisse exécuter du shell sur le serveur de l'entreprise, un système d'authentification par token a été implémenté. Vous êtes le seul à connaître ce token, et ne le partagez avec personne.
Analysez le code de l'API, et identifiez une mauvaise pratique qui pourrait facilement compromettre toute la sécurité du système par token. Ensuite, réécrivez le code en corrigeant cette mauvaise pratique.

## modelisation SQL

Vous souhaitez développer un site web de lecture en ligne (comme www.lirtuose.fr par exemple).
Vous êtes en charge des bases de données. Les développeurs du back et du front ne savent pas encore exactement ce qu'ils vont faire.
Pour simplifier, considérons que vous avez à votre disposition des données concernant les auteurs (leur nom, date de naissance, nationalité, les livres publiés, etc) et des données concernant les livres (le titre, la date de publication, le genre, le ou les auteurs, etc). Un auteur peut avoir écrit plusieurs livres, et un livre peut avoir été écrit par plusieurs auteurs.
Décrivez très brièvement comment vous modéliseriez les données dans une base SQL.

## racing game

Pas besoin d'écrire du code Python dans ce mini-cas. Du pseudo-code, ou une explication claire et concise suffit.
Vous développez un jeu de course. Dans ce jeu, vous voulez donner la possibilité au joueur de customiser sa voiture. En particulier, vous souhaitez qu'il puisse choisir :

- la couleur de la carosserie ;
- le type de peinture de la carosserie (métallique, mate, etc) ;
- la forme des jantes ;
- la couleur des jantes ;
- le type de peinture des jantes (métallique, mate, etc) ;
- la forme de l'aileron arrière ;
- le type de l'aileron (rétractable, fixe, etc)
- la couleur de l'aileron ;
- et très certainement d'autres choses qui vous viendront en tête au fur et à mesure du projet ;

Vous avez une classe qui se nomme "Car" et qui possède une méthode "draw" qui dessine la voiture à l'écran.
Comment structureriez-vous votre code, dans les grandes lignes, pour implémenter la méthode "draw" de "Car" ?

