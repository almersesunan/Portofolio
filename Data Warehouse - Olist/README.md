## Olist Data Warehouse

1. Ingest CSV dataset "Brazilian E-Commerce Public Dataset by Olist" to MySQL using Python (Pandas, SQLAlchemy, MySQL Connector)

2. DWH created using Snowflake Schema designed for logistic/delivery department which can be used to analyze and track all shipping activity like measure the accuracy of delivery time, analyze if product weight/dimension affect delivery duration/price etc.

ERD:

![image](https://user-images.githubusercontent.com/80158731/151682669-6df4fd16-262c-42ec-9117-2fe89de5004a.png)

Notes:
-	City/State table not created to avoid more complex join (Denormalize for decreasing runtime & memory used), in trade off with persistent data (city & state redundancy used more storage usage).
-	Price column included in fact_orders table in case wants to estimate insurance (Example: price x n% = insurance).
