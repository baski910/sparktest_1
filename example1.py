from pyspark.sql import SparkSession
columns = ["language","users_count"]
data = [("Java", "20000"), ("Python", "100000"), ("Scala", "3000")]

# create a Spark RDD from a collection List by calling parallelize() function from SparkContext 

spark = SparkSession.builder.appName('myApp').getOrCreate()
rdd = spark.sparkContext.parallelize(data)

# PySpark RDD’s toDF() method is used to create a DataFrame from the existing RDD. 
# Since RDD doesn’t have columns, 
# the DataFrame is created with default column names “_1” and “_2” as we have two columns.

dfFromRDD1 = rdd.toDF()
dfFromRDD1.printSchema()  
