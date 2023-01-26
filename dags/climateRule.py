from __emailSend import sendEmail
from __requestData import requestData
from __treatmentData import treatmentData

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import pendulum


with DAG(
        "climateRule",
        start_date=pendulum.datetime(2022, 12, 26, tz='UTC'),
        schedule_interval='0 0 * * 1',
) as dag:
    task1 = BashOperator(
        task_id='installModules',
        bash_command='pip3 install openpyxl'
    )

    task2 = PythonOperator(
        task_id="requestData",
        python_callable=requestData,
        op_kwargs={'data_interval_end': '{{data_interval_end.strftime("%Y-%m-%d")}}'},
        provide_context=True
    )

    task3 = PythonOperator(
        task_id="dataTreatment",
        python_callable=treatmentData,
        provide_context=True
    )

    task4 = PythonOperator(
        task_id='sendEmail',
        python_callable=sendEmail,
        provide_context=True
    )

    task1 >> task2 >> task3 >> task4


