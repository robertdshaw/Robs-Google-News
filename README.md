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
![Screenshot 2024-09-17 163529](https://github.com/user-attachments/assets/c4342554-88aa-457a-badc-9cdc4c487b6e)

4. **Logging & Error Handling**: The script contains built-in error handling to catch exceptions during the data processing and database update steps. Errors and important events (like successful table updates) are logged in a `newsapi.log` file.
![Screenshot 2024-09-17 163927](https://github.com/user-attachments/assets/b26828b9-376c-4670-8352-be304f8fe66e)

5. **Testing**: A separate test script called core_testing tests some of the classes from the NewsAPIClient module using unittest methods.
![Screenshot 2024-09-17 165804](https://github.com/user-attachments/assets/0e94e03b-2a86-4c05-bf5a-4067a4e7cc2c)

6. **Scheduled Execution**: The script is executed automatically 3 times a week at 8am using Windows Task Scheduler, ensuring the process runs without manual input.
<img width="682" alt="image" src="https://github.com/user-attachments/assets/1f0a9d01-969a-4f05-b877-f93a606abb7b">
