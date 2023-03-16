"""
In this task, I assume data from OLTP stored in MySQL DB engine
The spark below read data from MySQL DB and transform to new format with the new designed schema
"""


import os
import pyspark
from pyspark.sql import SparkSession
from pyspark import pandas as ps

# Please get the connector file via this link:
# https://dev.mysql.com/downloads/connector/j/

spark = SparkSession.builder.appName("SQL Tables")\
    .config("spark.jars", "mysql-connector-java.jar")\
    .getOrCreate()


# Format is "jdbc:mysql://localhost:3306/<db_name>"
url = os.environ['DB_URL']
driver = "com.mysql.jdbc.Driver"
user = os.environ['DB_user']
password = os.environ['DB_PASSWORD']

list_tables = [
    'BRANCH_TYPES',
    'ADDRESSES',
    'BRANCHES',
    'TRANSACTION_TYPES',
    'CUSTOMERS',
    'ACCOUNT_TYPES',
    'STATUSES'
    'ACCOUNT',
    'TRANSACTIONS'
]

dict_spark_df = {}
for table_name in list_tables:
    dict_spark_df[table_name] = spark.read\
        .format("jdbc")\
        .option("driver", driver)\
        .option("url", url)\
        .option("user", user)\
        .option("password", password)\
        .option("dbtable", table_name)\
        .load()

