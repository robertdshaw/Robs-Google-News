# Robs-Google-News
## Purpose
This Python program is designed to automate the process of reading data from an API (or CSV file/SQL database), processing the data (formatting, cleaning, etc.), and updating a SQL table with the processed data. The automation is achieved using the Windows Task Scheduler, which allows the program to execute at a predefined time without human intervention.The program ensures the data is formatted according to predefined rules, and logs any exceptions or errors that occur during execution.
I set out to fetch news articles related to the Swedish manufacturing company Alfa Laval's core product "heat exchanger", and then save these articles in a database.

## How the Program Works
1. **Data Loading**: The program begins by reading data from News API's API which is found at https://newsapi.org/docs/endpoints/everything and after logging in generates an API key which is used to fill a database name called news.db 
   
2. **Data Processing**: After loading the data, the script processes it by performing tasks such as:
   - Converting data types from ISO 8601 complete date to a basic date type, and sorting dates by most recent article first. 
   - Formatting data to ensure columns are extracted properly and that missing data is handled appropriately.

3. **SQL Table Update**: Once the data is processed and saved, the program connects to a local SQLite database and updates a newly-created table with the new, processed articles. It allows the database connection to be accessed by several programs in parallel. 
<img width="554" alt="image" src="https://github.com/user-attachments/assets/2548c6d1-60d4-4324-96d5-944985f6285c">

4. **Logging & Error Handling**: The script contains built-in error handling to catch exceptions during the data processing and database update steps. Errors and important events (like successful table updates) are logged in a `newsapi.log` file.
<img width="754" alt="image" src="https://github.com/user-attachments/assets/7d0a94e6-cdc8-4f32-b4da-3e28d3ad2c5a">

5. **Testing**: A separate test script called core_testing tests some of the classes from the NewsAPIClient module using unittest methods.
<img width="496" alt="image" src="https://github.com/user-attachments/assets/50886424-8422-4e72-8bf5-563fd1b0aaa9">

6. **Scheduled Execution**: The script is executed automatically 3 times a week at 8am using Windows Task Scheduler, ensuring the process runs without manual input.
<img width="780" alt="image" src="https://github.com/user-attachments/assets/a6935f5c-fe99-4ca8-85af-bac373fc799b">
