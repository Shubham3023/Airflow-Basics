from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def hello():
    print("Hello from Airflow!")

my_dag =  DAG(
    'hello_dag',
    start_date=datetime(2024, 1, 1),
    schedule='@daily',
    catchup=False
) 
task = PythonOperator(
        task_id='hello_task',
        python_callable=hello, 
        dag = my_dag
    )

task