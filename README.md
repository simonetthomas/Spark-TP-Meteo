# Spark-TP-Meteo

## But

Cette application Spark écrite en Python prend en entrée des fichiers de relevés de températures et effectue des statistiques sur les températures.

* Le premier fichier `Meteo.py` calcule la température max par mois en utilisant un RDD (*Resilient Distributed Dataset*).
* Le deuxième fichier `Meteo_dataframes.py` calcule la température min, max et moyenne par mois en utilisant un RDD et un *DataFrame*.

## Fonctionnement

Le code est écrit en Python, et est exécuté à l'aide de PySpark en tant qu'application standalone.

* Dans le premier cas (`Meteo.py`):  
On utilise la fonction Map de Spark pour extraire les températures des fichiers d'entrée, puis on effectue un filtre pour éviter les valeurs de températures invalides, et garder les lignes pour lesquelles l'indicateur de qualité est parmi les valeurs (0, 1, 4, 5, 9).  
On effectue ensuite un reduce et un tri et on affiche les résultats dans la console.

* Dans le deuxième cas (`Meteo_dataframe.py`):  
On utilise la fonction Map de Spark pour extraire les températures des fichiers d'entrée. Puis le filtrage et la requête pour calculer la valeur min, max, et moyenne de chaque mois sont effectués sur un [*DataFrame*](https://spark.apache.org/docs/latest/sql-programming-guide.html).

## Utilisation

Il faut préalablement avoir installé Spark et Python, et avoir configuré la variable d'environnement `path` pour pouvoir notamment lancer la commande `spark-submit`. Plus d'informations sur PySpark et son installation [ici](https://spark.apache.org/docs/0.9.0/python-programming-guide.html).

Les données d'entrée sont les relevés du [National Climatic Data Center](https://en.wikipedia.org/wiki/National_Climatic_Data_Center), disponibles à [cette adresse](https://www1.ncdc.noaa.gov/pub/data/noaa/). Vous pouvez télécharger plusieurs archives puis les mettre dans un répertoire `ressources` dans la racine du projet.

Vous pouvez ensuite exécuter le code dans votre console avec la commande suivante :
```
spark-submit Meteo.py ressources/.*gz
```
Les résultats s'affichent dans la console.
