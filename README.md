# Spark-TP-Meteo

## But

Cette application Spark écrite en Python prend en entrée des fichiers de relevés de températures et calcule la température moyenne par mois.

## Fonctionnement

Le code est écrit en Python, et est exécuté à l'aide de PySpark en tant qu'application standalone.

On utilise la fonction map de Spark pour extraire les températures des fichiers d'entrée, puis on effectue un filtre pour éviter les valeurs de températures invalides, et garder les lignes pour lesquelles l'indicateur de qualité est parmi les valeurs (0, 1, 4, 5, 9).

On effectue ensuite un reduce et un tri et on affiche les résultats dans la console.

## Utilisation

Il faut préalablement avoir installé Spark et Python, et avoir configuré la variable d'environnement `path` pour pouvoir notamment lancer la commande `pyspark-submit`. Plus d'informations sur PySpark et son installation [ici](https://spark.apache.org/docs/0.9.0/python-programming-guide.html).

Les données d'entrée sont les relevés du [National Climatic Data Center](https://en.wikipedia.org/wiki/National_Climatic_Data_Center), disponibles à [cette adresse](https://www1.ncdc.noaa.gov/pub/data/noaa/). Vous pouvez télécharger plusieurs archives puis les mettre dans un répertoire `ressources` dans la racine du projet.

Vous pouvez ensuite exécuter le code dans votre console avec la commande suivante :
```
pyspark-submit Meteo.py ressources/.*gz
```
Les résultats s'affichent dans la console.
