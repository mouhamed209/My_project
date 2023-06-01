"# My_project" 
"# My_project" 
nstallation d’une version officielle avec¶
C’est la façon recommandée d’installer Django.

Installez pip. La manière la plus simple est d’utiliser l”installeur pip autonome. Si votre distribution contient déjà une version installée de pip, il pourrait être nécessaire de la mettre à jour si elle est trop ancienne. Dans ce cas, vous le verrez bien car l’installation ne fonctionnera pas.

Jetez un œil à venv. Cet outil fournit des environnements Python isolés qui sont bien plus pratiques que d’installer des paquets au niveau de tout le système. Il permet aussi d’installer des paquets sans avoir besoin de privilèges administrateurs. Le tutoriel de contribution vous guide pour la création d’un environnement virtuel.

Après avoir créé et activé un environnement virtuel, entrez la commande :

/ 
$ python -m pip install Django
Installation d’un paquet de la distribution¶
Parcourez les notes spécifiques aux distributions pour vérifier que votre plate-forme/distribution propose des paquets ou installeurs officiels de Django. Les paquets fournis par les distributions permettent généralement de profiter de l’installation automatique des dépendances et de mises à niveau prises en charge ; toutefois, ces paquets correspondent rarement aux dernières versions de Django.

Installation de la version de développement¶
Suivi du développement de Django
Si vous aimeriez pouvoir mettre à jour occasionnellement votre version de Django avec les dernières corrections et améliorations, suivez ces instructions :

Vérifiez que Git est installé et que vous pouvez lancer ses commandes depuis un terminal (saisissez git help à l’invite de commande pour le tester).

Créez une copie de travail de la branche principale de développement de Django comme ceci :

/ 
$ git clone https://github.com/django/django.git
Un répertoire django sera créé dans le répertoire actuel.

Vérifiez que l’interpréteur Python peut charger le code de Django. La façon la plus pratique de faire cela est d’utiliser un environnement virtuel et pip. Le tutoriel de contribution vous guide pour la création d’un environnement virtuel.

Après avoir configuré et activé l’environnement virtuel, exécutez la commande suivante :

/ 
$ python -m pip install -e django/
Ceci rendra le code Django importable et mettra aussi à disposition la commande utilitaire django-admin. En d’autres mots, vous serez fin prêt !

Lorsque vous souhaitez mettre à jour votre copie du code source de Django, lancez la commande git pull à partir du répertoire django. Quand vous faites cela, Git télécharge toutes les modifications.
Voici quelques commandes couramment utilisées avec Django :
python manage.py runserver : Démarre le serveur de développement Django.
python manage.py startapp app_name : Crée une nouvelle application Django avec le nom spécifié.
python manage.py makemigrations : Génère les fichiers de migration pour les modifications de modèle.
python manage.py migrate : Applique les migrations et met à jour la base de données.
python manage.py createsuperuser : Crée un superutilisateur pour l'administration de Django.
