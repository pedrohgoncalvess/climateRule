import pandas as pd
from pandas import DataFrame
from datetime import datetime


def treatmentData(**context):
    data = context['ti'].xcom_pull(key='dataWeather')
    dados = pd.read_csv(data)
    dados:DataFrame = dados[['datetime', 'tempmax', 'tempmin',
                   'feelslikemax', 'feelslikemin','icon']]
    msg:str = ''
    for dia in range(len(dados)):
        data = datetime.strptime(dados['datetime'][dia], '%Y-%m-%d').strftime('%d/%B')
        msg = msg + f" >>>>>>>>>>>>>>>>>>> {data} it will {dados['icon'].iloc[dia]}. Max temperature is {dados['tempmax'].iloc[dia]}" \
                    f" and minimum {dados['tempmin'].iloc[dia]} <<<<<<<<<<<<<<<<<<< \n"

    context['ti'].xcom_push(key='sendmsgEmail', value=msg)