# Robs-Google-News
## Purpose
This Python program is designed to automate the process of reading data from an API (or CSV file/SQL database), processing the data (formatting, cleaning, etc.), and updating a SQL table with the processed data. The automation is achieved using the Windows Task Scheduler, which allows the program to execute at a predefined time without human intervention.The program ensures the data is formatted according to predefined rules, and logs any exceptions or errors that occur during execution.
I set out to fetch news articles related to the Swedish manufacturing company Alfa Laval's core product "heat exchangers", and then save these articles in a database.

## How the Program Works
1. **Data Loading**: The program begins by reading data from News API's API. 
   
2. **Data Processing**: After loading the data, the script processes it by performing tasks such as:
   - Converting data types (e.g., converting strings to datetime).
   - Formatting data according to certain rules.

3. **SQL Table Update**: Once the data is processed, the program connects to a local SQLite database and updates an existing table with the new, processed data. The table is either replaced or updated with the latest data.

<table>
  <tr>
    <th style="width: 45%;">Article Title</th>
    <th style="width: 30%;">Published at</th>
    <th style="width: 15%;">Description</th>
    <th style="width: 10%;">URL</th>
  </tr>
  <tr>
    <td><strong>Mine water could heat thousands of Welsh homes</strong></td>
    <td>10-09-2024</td>
    <td>Energy bills could be cut by low carbon heat schemes which use water from abandoned Welsh coal mines.</td>
    <td><a href="https://www.bbc.com/news/articles/c0l867k70p8o">Link</a></td>
  </tr>
  <tr>
    <td><strong>Apheros says it can boost data center cooling by 90% with metal foam</strong></td>
    <td>19-08-2024</td>
    <td>Alpheros says its patented technology can cut down the energy requirements for data center cooling by at least 10%-20%.</td>
    <td><a href="https://venturebeat.com/data-infrastructure/apheros-says-it-can-boost-data-center-cooling-by-90-with-metal-foam/">Link</a></td>
  </tr>
</table>

4. **Logging & Error Handling**: The script contains built-in error handling to catch exceptions during the data processing and database update steps. Errors and important events (like successful table updates) are logged in a `newsapi.log` file.

<img width="629" alt="image" src="https://github.com/user-attachments/assets/abbe8edf-18e7-4880-8758-745c26790ef7">

5. **Scheduled Execution**: The script is executed automatically 3 times a week at 8am using Windows Task Scheduler, ensuring the process runs without manual input.
