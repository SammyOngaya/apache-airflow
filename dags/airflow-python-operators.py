# step 1 -- Import needed libraries
from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

# step 2 -- Define your Python functions
def hello_world():
 return ('Hello Wolrd Text')

def lorem_ipsum():
	return ("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")

# step 3 -- Define defaults parameters
default_args={
    'owner':'sam',
    'depends_on_past':False,
    'start_date': datetime(2021,11,11),
    'retries':3
}

# step 4 -- Define DAG Object. Run every 5 mins (schedule_interval='*/5 * * * *') 
dag = DAG(dag_id='Python-Operator-DAG',default_args=default_args, description='Sample DAG with 2 tasks for hello and lorem that runs every 5 mins', schedule_interval='*/5 * * * *', 
		catchup=False)

# step 5 -- Add Task to DAG
hello_operator = PythonOperator(task_id='hello_task', python_callable=hello_world, dag=dag)
lorem_operator = PythonOperator(task_id='lorem_task', python_callable=lorem_ipsum, dag=dag)

# step 6 Define dependency. Run the tasks sequentially from dummy operator to the python operator
hello_operator >> lorem_operator
