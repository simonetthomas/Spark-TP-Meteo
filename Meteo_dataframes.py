# -*- coding: utf-8 -*-
import sys
from pyspark.conf import SparkConf
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql import functions as F

# Configuration
conf = SparkConf().setMaster("local[2]").setAppName("My app")
sc = SparkContext(conf=conf)

# Lecture des fichiers d'entrée dans un RDD
if len(sys.argv)>1:
	lines = sc.textFile(sys.argv[1])
else:
	print "* Veuillez indiquer les fichiers sources en argument."
	sys.exit(2)

# Recuperation du mois, de la temperature et de la qualite dans un RDD
values=lines.map(lambda lamb: (lamb[19:21], float(lamb[87:92])/10, lamb[92]) ).collect()

# Configuration SparkSession
spark = SparkSession \
.builder.appName("AppName") \
.config("master", "local[2]") \
.getOrCreate()

# Récupération du rdd dans un DataFrame
df=spark.createDataFrame(values,['mois','temperature','qualite'])
#df.show()
#df.printSchema()

# Avec une requête SQL : filtrage sur les valeurs de température et de qualité et mapping pour ne garder qu’un tuple (mois,température)
df.createTempView("meteo_filtre")
spark.sql("select mois, temperature from meteo_filtre where temperature <> 999.9 and qualite in (0,1,4,5,9)")

# Sur le DataFrame : grouper et trier par mois et aggréger pour obtenir les 3 éléments min, max et avg
df.select(df.mois, df.temperature)\
.filter(df.temperature != 999.9)\
.groupby(df.mois)\
.agg(F.max(df.temperature).alias("temp_max"),F.min(df.temperature).alias("temp_min"), F.avg(df.temperature).alias("temp_moyenne"))\
.orderBy(df.mois).show()