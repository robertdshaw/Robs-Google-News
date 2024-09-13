# Robs-Google-News
## Purpose
This Python program is designed to automate the process of reading data from an API (or CSV file/SQL database), processing the data (formatting, cleaning, etc.), and updating a SQL table with the processed data. The automation is achieved using the Windows Task Scheduler, which allows the program to execute at a predefined time without human intervention.The program ensures the data is formatted according to predefined rules, and logs any exceptions or errors that occur during execution.
I set out to fetch news articles related to the Swedish manufacturing company Alfa Laval's core product "heat exchangers", and then save these articles in a database.

## How the Program Works
1. **Data Loading**: The program begins by reading data from News API's API. 
   
2. **Data Processing**: After loading the data, the script processes it by performing tasks such as:
   - Converting data types (e.g., converting strings to datetime).
   - Cleaning data (e.g., removing null values or duplicates).
   - Formatting data according to certain rules.

3. **SQL Table Update**: Once the data is processed, the program connects to a local SQLite database and updates an existing table with the new, processed data. The table is either replaced or updated with the latest data.

4. **Logging & Error Handling**: The script contains built-in error handling to catch exceptions during the data processing and database update steps. Errors and important events (like successful table updates) are logged in a `pipeline.log` file.

5. **Scheduled Execution**: The script is executed automatically at a set time using Windows Task Scheduler, ensuring the process runs without manual input.


## Task Scheduler Setup
1. Opened Windows Task Scheduler.
2. Created a new task.
3. Set up triggers weekly at 8 AM
4. Choose my Python interpreter and script path under Actions.


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>description</th>
      <th>url</th>
      <th>publishedAt</th>
      <th>source</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mine water could heat thousands of Welsh homes</td>
      <td>Energy bills could be cut by low carbon heat s...</td>
      <td>https://www.bbc.com/news/articles/c0l867k70p8o</td>
      <td>2024-09-10T22:00:10Z</td>
      <td>BBC News</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Apheros says it can boost data center cooling ...</td>
      <td>Alpheros says its patented technology can cut ...</td>
      <td>https://venturebeat.com/data-infrastructure/ap...</td>
      <td>2024-08-19T14:44:13Z</td>
      <td>VentureBeat</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Snøhetta Builds A Timber School In Norway with...</td>
      <td>Snøhetta Builds A Timber School In Norway with...</td>
      <td>https://www.yankodesign.com/2024/08/30/snohett...</td>
      <td>2024-08-30T23:30:21Z</td>
      <td>Yanko Design</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Timber school tackles extreme cold with impres...</td>
      <td>Situated north of the Arctic Circle in Norway,...</td>
      <td>https://newatlas.com/architecture/coarvematta-...</td>
      <td>2024-08-23T13:13:01Z</td>
      <td>New Atlas</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Porsche 911 Type 901/14 Engine at No Reserve</td>
      <td>This Porsche Type 901/14 2.0-liter flat-six wa...</td>
      <td>https://bringatrailer.com/listing/engine-40/</td>
      <td>2024-08-24T12:45:38Z</td>
      <td>Bringatrailer.com</td>
    </tr>
  </tbody>
</table>
</div>
