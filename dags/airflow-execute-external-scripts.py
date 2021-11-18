# step 1 -- Import needed libraries
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

# step 2 -- Define defaults parameters
default_args={
    'owner':'Sam',
    'depends_on_past':False,
    'start_date': datetime(2021,11,11),
    'retries':3
}

# step 3 -- Define DAG Object. 
dag = DAG(dag_id='Magic_Number_Generator',default_args=default_args, schedule_interval='*/1 * * * *',
	description='DAG to execute external Python scripts', 
        catchup=False)

# step 4 -- Add Task to DAG
generate_magic_numbers_operator = BashOperator(task_id='Magic-Number-BashOperator-Task', 
	bash_command="python /scripts/generate_magic_numbers.py", 
    dag=dag)

# step 5 Define dependency. 
generate_magic_numbers_operator

