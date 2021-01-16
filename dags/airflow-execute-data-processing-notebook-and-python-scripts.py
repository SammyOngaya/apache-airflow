# step 1 -- import needed libraries
from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator


# step 2 -- define your python functions


# step 3 -- define the defaults arguments
default_args={
    'owner':'sam',
    'depends_on_past':False,
    'start_date': datetime(2020, 12, 26),
    'retries':3
    }

# step 4 -- define your DAG
# run every 5 mins (schedule_interval='*/5 * * * *') 
dag = DAG('Tweet_Analysis_DAG-1',default_args=default_args, description='Sample DAG to execute Python Script', schedule_interval='*/5 * * * *', 
		catchup=False)

# step 5 -- instantiate your tasks
dummy_operator = DummyOperator(task_id='dummy_task', dag=dag)
tweets_python_bash_operator = BashOperator(task_id='tweet_python_analysis_task',
    bash_command='python3 /mnt/c/Users/soongaya/Documents/datasets/Twitter_Data_Extraction.py',
    dag=dag
)

twitter_bash_notebook_operator = BashOperator(task_id='tweet_analysis_task',
	bash_command='jupyter nbconvert --execute --to notebook /mnt/c/Users/soongaya/Documents/datasets/Twitter_Data_Extraction.ipynb',
    dag=dag)
# )/mnt/c/Users/soongaya/Documents/Data Science/Big Data/usecases/Natural-Language-Processing/Social Analytics/Twitter Data Extraction.ipynb'

# step 6 -- set task dependencies
dummy_operator >> twitter_bash_notebook_operator
# dummy_operator >> tweets_python_bash_operator