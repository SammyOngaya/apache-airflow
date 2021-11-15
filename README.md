# Apache Airflow

# What is Apache Airflow?
Apache Airflow is a platform for authoring, scheduling and monitoring workflows/data pipeline programmatically. Airflow is primarily written in Python and uses directed acyclic graphs (DAGs) to manage workflow orchestration. It's an open source data-pipeline orchestration tool that allows you to extend the library to suite complex business use-cases. Airflow comes with an intuitive modern web interface for monitoring and managing workflows. Airflow is highly scalable platform and provides robust integration with numerous systems. 
 

# Airflow Features
1.	Python-based. Airflow is written in Python. This enables the user to write workflows in Python with flexibility. 
2.	Web interface. Apache airflow comes with an intuitive modern web user interface for scheduling, monitoring and managing data pipelines via web interface. It eliminates the need to manage workflows on a traditional command line cron-based interface.
3.	 Open Source. It is free and you can customise different component to fit your business use-case. Being open source airflow has a large active community.
4.	Ease of Use. Airflow requires only Python knowledge to begin using it to manage infinite number of pipelines and workflows.
5.	Robust Integration. Apache airflow supports wide range of technologies.

# Airflow Concepts
1.	Directed Acyclic Graphs (DAGs). A DAG is a collection of all tasks ready to run and organized according to their relationships and dependencies.
2.	Tasks. A task is a unit of work in a DAG usually represented as a node.
3.	Operator. An Operator describes a single task in a workflow. They are building blocks of a single tasks. Examples of Operators are; PythonOperator, BashOperator, EmailOperator, HiveOperator etc.
4.	Hooks. Hooks are interfaces to external systems like Hive, S3, MySQL, Postgres, etc.
5.	Variables. A variable is an airflow component that allows the storage and access of data. 

For more Concepts in airflow refer to airflow documentation. https://airflow.apache.org/docs/apache-airflow/1.10.12/concepts.html 

# Airflow Core Components
1.	Executors. Airflow Executor is mechanism by which work actually gets done. Executors available in Airflows are LocalExecutor, SequentialExecutor, the CeleryExecutor, or the KubernetesExecutor.
2.	Web Server. Airflow Web Server enables users to manage and monitor dworkflows in a web interface. https://airflow.apache.org/docs/apache-airflow/stable/security/webserver.html 
3.	Scheduler. Airflow scheduler is a service that is responsible for monitoring and running tasks and DAGs.  https://airflow.apache.org/docs/apache-airflow/stable/concepts/scheduler.html 
4.	Metadata Database. Airflow metadata database is used to store airflow configurations like user details, connections, variables etc. It also serves as the main point of reference for Airflow Scheduler. https://www.astronomer.io/guides/airflow-database 
Visit the Astronomer site for more details on each component. https://www.astronomer.io/guides/airflow-components 

# Where to Use Airflow
1.	Automation of data pipelines. Easily schedule, run, monitor and manage ETL and ELT pipelines.
2.	Automation of Machine learning workflows. Automate data collection, processing, training and other machine learning processes.
3.	Efficiently monitor how tasks in a DAG are running in real-time, retry tasks on failure and send alerts for task failures.
4.	Automation of DevOps workloads such as back-ups.
5.	Automation of analytics reports.
