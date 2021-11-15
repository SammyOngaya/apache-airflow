# Step 1 Import required libraries
from airflow import DAG
from datetime import datetime
from airflow.operators.dummy_operator import DummyOperator

# Step 2 Define default parameters

default_args={
    'owner':'airflow',
    'depends_on_past':False,
    'start_date': datetime.now(),
    'retries':3
}

# Step 3 Create DAG Object
dag=DAG(dag_id='DAG-1', default_args=default_args, catchup=False, schedule_interval='* * * * *')

# Step 4 Add Tasks to the DAG

start=DummyOperator(task_id='start', dag=dag)
end=DummyOperator(task_id='end',dag=dag)

# Step 5 Define Dependencies
start>>end


