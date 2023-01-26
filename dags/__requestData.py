from airflow.macros import ds_add
from os.path import join

def requestData(data_interval_end,**context):
    key = '6XY7642GR46EWZZZS422QM2UN'
    cidade = 'Tubarao'
    url = join("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
               f"{cidade}/{data_interval_end}/{ds_add(data_interval_end, 7)}?unitGroup=metric&include=days&key={key}&contentType=csv")

    context['ti'].xcom_push(key='dataWeather',value=url)
