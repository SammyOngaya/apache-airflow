# step 1 -- import needed libraries
from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator


# step 2 -- define the defaults arguments
default_args={
    'owner':'sam',
    'depends_on_past':False,
    'start_date': datetime(2021, 11, 11),
    'retries':3
    }

# step 3 -- define your DAG
# run every 5 mins (schedule_interval='*/5 * * * *') 
dag = DAG('Titanic_ETL_DAG-1',default_args=default_args, description='Sample DAG to execute Python Script', schedule_interval='*/5 * * * *', 
		catchup=False)


# step 4 -- instantiate your tasks
dummy_operator = DummyOperator(task_id='dummy_task', dag=dag)
titanic_bash_operator = BashOperator(task_id='titanic_bash_task',
	bash_command='python3 /mnt/c/Users/soongaya/Documents/datasets/TDE.py',
    dag=dag
)

titanic_bash_notebook_operator = BashOperator(task_id='titanic_bash_notebook_task',
	bash_command='jupyter nbconvert --execute --to notebook /mnt/c/Users/soongaya/Documents/datasets/Titanic_Twitter_Data_Extraction.ipynb',
    dag=dag
)

# step 5 -- set task dependencies
dummy_operator >> titanic_bash_operator
dummy_operator >> titanic_bash_notebook_operator