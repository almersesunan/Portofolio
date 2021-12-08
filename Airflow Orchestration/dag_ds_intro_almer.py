from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime
import requests
import json

default_arguments = {
    "owner": "almer",
    "email": "almer.sesunan@gmail.com",
    "start_date": datetime(2021, 10, 25)
}

dag = DAG(
    dag_id="etl_workflow_almer",
    default_args=default_arguments
)

# Operators
start = DummyOperator(
    task_id="start",
    dag=dag
)

def retrieve_data(url, filename):
    response = requests.get(url)
    todos = response.json()
    data = []
    for i in todos:
        data.append(i)
    with open(filename, "w") as file:
        file.write(json.dumps(data))
    
retrieve_todo_task = PythonOperator(
    task_id="retrieve_todo_list",
    python_callable=retrieve_data,
    op_kwargs={"url": "https://jsonplaceholder.typicode.com/todos", "filename": "todo_list.json"},
    dag=dag
)

status_task = BashOperator(
    task_id="print_status",
    bash_command="echo 'Data sudah ditarik dan berhasil disimpan pada file'",
    dag=dag
)

# Dependency
start >> retrieve_todo_task >> status_task
