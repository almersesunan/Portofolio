This DWH is using Snowflake Schema designed for logistic/delivery department which can be used to analyze and track all shipping activity like estimate products arrival time etc.

ERD:
![image](https://user-images.githubusercontent.com/80158731/151664956-277379fa-46a6-4529-8ad4-496902199247.png)

Notes:
-	City/State table not created to avoid more complex join (Denormalize for decreasing runtime & memory used), in trade off with persistent data (city & state redundancy used more storage usage).
-	Price column included in fact_orders table in case wants to estimate insurance (Example: price x n% = insurance).
