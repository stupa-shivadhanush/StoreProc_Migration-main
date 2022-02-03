# StoreProc_Migration
Migrate Stored Procedure to Python based code to run in lambda

The server bulk pushes are disabled in the repository. Uncomment the lines containing
the phrase ".to_sql" to push to the server

Data Used during this Migration:</br>
1. Match No. 717 </br>
2. Match ID: 1311 </br>

Data is for testing, so the data will be deleted everytime. For production Deployment change the line of code:</br></br>**From:**</br> ```if (refinedold.equals(refinednew) != False):```
</br>**To:** </br>
```if (refinedold.equals(refinednew) == False):```</br>
</br>**FILE: main.py**
