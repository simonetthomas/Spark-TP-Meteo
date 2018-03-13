# Spark-TP-Meteo

## But

Cette application spark écrite en python prend en entrée des fichiers de relevés de températures et calcule la température moyenne par mois.

## Fonctionnement

Le code est écrit en python, et est exécuté à l'aide de pyspark.

On utilise la fonction map de Spark pour extraire les températures des fichiers d'entrée, puis on effectue un filtre pour éviter les valeurs de températures invalides, et garder les lignes pour lesquelles l'indicateur de qualité est parmi les valeurs (0, 1, 4, 5, 9).

On effectue ensuite un reduce et un tri et on affiche les résultats.

## Utilisation

Il faut avoir installé Spark préalablement et avoir configuré la variable d'environnement `path` pour pouvoir lancer la commande pyspark-submit.

Les données d'entrée sont les relevés du [National Climatic Data Center](https://en.wikipedia.org/wiki/National_Climatic_Data_Center), disponibles à [cette adresse](https://www1.ncdc.noaa.gov/pub/data/noaa/). Téléchargez des archives et mettez-les dans un répertoire `ressources` dans la racine du projet.

Vous pouvez ensuite exécuter le code dans votre console avec la commande suivante :
```
pyspark-submit Meteo.py ressources/
```
