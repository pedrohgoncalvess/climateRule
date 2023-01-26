<h1 align="center">Airflow Weather Forecast.</h1>

<h4 align='center'>"climate rule" with visualcrossing API and airflow.</h4>

<p>For a better understanding of the code i will explain what is the role of the tasks and the challenges I encountered. Feel free to send me a message and give me your feedback on the code.</p>

- Task 1 - installModules
<p>I had problems with the "openpyxl" module in the processing stage of the data that the API returns. I tried to create an image with the module already installed (as I did with the rest) but without success, so I created this task with a bash operator.</p>

- Task 2 - requestData
<p>The visual crossing API asks for 3 pieces of information, the key generated when creating the account, the request interval days and the city where you want the information. This task just makes the request, the python operator receives the current day's date and adds another 7 to bring 1 week, after that it passes to xcom for the next task.</p>
