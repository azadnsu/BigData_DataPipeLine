from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator


default_args = {
		'owner' : 'Azad',
		'depends_on_past' :False,
		'email' :['azadnsu@gmail.com'],
		'email_on_failure': False,
		'email_on_retry': False,
		'retries': 5,
		'retry_delay': timedelta(minutes=5)
		}

dag = DAG(
	'FirstDag',
	default_args=default_args,
	start_date=datetime(2019,5,26,17,42),
	schedule_interval=timedelta(minutes=1))


task1 = BashOperator(
		task_id='make_a_file',
		bash_command='touch ~/desktop/hello_world.txt',
		dag=dag)

