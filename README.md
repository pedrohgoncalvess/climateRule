<h1 align="center">Airflow Weather Forecast.</h1>

<h4 align='center'>"climate rule" with visualcrossing API and airflow.</h4>

<p>For a better understanding of the code i will explain what is the role of the tasks and the challenges I encountered. Feel free to send me a message and give me your feedback on the code. The scheduler is set to send the week's weather forecasts every Monday.</p>


<h2 align='center'>Getting started</h2>

<p>In the repository there is the yaml file of the image. 
In the dockerfile there are some commands to run and install the predefined packages in requirements.txt.</p> 
<p>Run this code in terminal.</p>

```
docker build . --tag extending_airflow:latest
```

<p>This command will generate a new image based on the image in the directory but will install the packages defined in requirements.txt. Then change the name of the env AIRFLOW IMAGE_NAME in the yaml file to extending_airflow or the other name you put.</p>
<p>Then, run this code</p>

``` 
docker-compose up -d --no-deps --build airflow-webserver airflow-scheduler
```

<p>It will load airflow scheduler and web server services. You can also load the entire airflow image</p>


<h2 align='center'>Tasks</h2>

- Task 1 - installModules
<p>I had problems with the "openpyxl" module in the processing stage of the data that the API returns. I tried to create an image with the module already installed (as I did with the rest) but without success, so I created this task with a bash operator.</p>

- Task 2 - requestData
<p>The visual crossing API asks for 3 pieces of information, the key generated when creating the account, the request interval days and the city where you want the information. This task just makes the request, the python operator receives the current day's date and adds another 7 to bring 1 week, after that it passes to xcom for the next task. <i>It is important to emphasize that it is not the request package that makes the request, but the lib path with the join module.</i></p>

- Task 3 - treatmentData
<p>Xcom receive the results of This task is responsible for handling the data (excluding non-essential information) and formatting the message, then leaves the message in xcom for the next and last task</p>

- Task 4 - emailSend
<p>the last task is the one that sends the email. xcom receives the value of the last task and sends the email with the weather information for the week. It is important to point out that it was not done with the airflow emailOperator, since it serves more for "triggers" of errors and not for customized messages.</p>
