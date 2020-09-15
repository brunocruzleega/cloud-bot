import airflow
from airflow import DAG
from datetime import timedelta
from airflow.operators.bash_operator import BashOperator

default_args = {
    'start_date': airflow.utils.dates.days_ago(0),
    'retries': 0,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'malha_bash_error',
    default_args=default_args,
    description='Malha de teste CI/CD',
    schedule_interval=None,
    dagrun_timeout=timedelta(minutes=60)
    )

"""
INICIO -- TASKS
"""

bash_task = BashOperator(
	task_id='bash_task',
	bash_command='exit 1 ',
	dag=dag,
	depends_on_past=False
)

bash_task