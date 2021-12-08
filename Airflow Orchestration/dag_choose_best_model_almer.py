from airflow.models import DAG
from airflow.operators.python_operator import BranchPythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

default_arguments = {
    "owner": "almer",
    "email": "almer.sesunan@gmail.com",
    "start_date": datetime(2021, 10, 26)
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

def _choose_best_model():
    accuracy = 6
    if accuracy > 5:
        return "accurate"
    else:
        return "inaccurate"
    
choose_best_model = BranchPythonOperator(
    task_id="choose_best_model",
    python_callable=_choose_best_model,
    dag=dag
)

accurate = DummyOperator(
    task_id="accurate",
    dag=dag
)

inaccurate = DummyOperator(
    task_id="inaccurate",
    dag=dag
)

# Dependency
start >> choose_best_model >> [accurate, inaccurate]
