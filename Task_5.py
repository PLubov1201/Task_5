from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("WordCount").setMaster("local")
sc = SparkContext(conf=conf)

text_rdd = sc.textFile("example.txt")

words_rdd = text_rdd.flatMap(lambda line: line.split())
print(words_rdd.count())
