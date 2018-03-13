import sys
from pyspark import SparkContext
from pyspark.conf import SparkConf

# Configuration
conf = SparkConf().setMaster("local[2]").setAppName("My app")
sc = SparkContext(conf=conf)

# Retourne le contenu ligne par ligne des fichiers dans un RDD
lines = sc.textFile(sys.argv[1]) 

# Recuperation du mois, de la temperature et de la qualite
values=lines.map(lambda lamb: (lamb[19:21], lamb[87:92], lamb[92]))\
# Filtrage sur la temperature et la qualite
.filter(lambda (mois, temp, qual) : int(temp) != 9999 and int(qual) in (0,1,4,5,9))\
# Map pour ne garder que le mois et la temperature
.map(lambda (mois, temp, qual): (mois, temp))\
# Reduce par mois en gardant la temperature max
.reduceByKey(max)\
# Tri par clef
.sortByKey()\
.collect()

print values