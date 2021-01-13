# step 1 -- import needed libraries
from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

# step 2 -- define your python functions

def hello_world():
 return ('Hello Wolrd Text')

def lorem_ipsum():
	return ("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")

# step 3 -- define the defaults arguments
default_args={
    'owner':'sam',
    'depends_on_past':False,
    'start_date': datetime.now(),
    'retries':3
}

# step 4 -- define your DAG
# run every 5 mins (schedule_interval='*/5 * * * *') 
dag = DAG('Sample_DAG-1',default_args=default_args, description='Sample DAG with three tasks', schedule_interval='*/5 * * * *', 
		catchup=False)

# step 5 -- instantiate your tasks
dummy_operator = DummyOperator(task_id='dummy_task', dag=dag)
hello_operator = PythonOperator(task_id='hello_task', python_callable=hello_world, dag=dag)
lorem_operator = PythonOperator(task_id='lorem_task', python_callable=lorem_ipsum, dag=dag)

# step 6 -- run the tasks sequentially
dummy_operator >> hello_operator
hello_operator >> lorem_operator