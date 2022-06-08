from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
            'owner': 'Meng m',
            'retries': 2,
            'retry_delay': timedelta(minutes=1)
             }


with DAG('dist_example',
      start_date=datetime(2022, 5, 13, 16, 34),
      schedule_interval="*/10 * * * *",
  ) as dag:
    
    create_command = 'echo $(hostname)'
    t1 = BashOperator(
      task_id='task_for_q1',
      bash_command=create_command,
      dag=dag
    )
    t2 = BashOperator(
      task_id= 'task_for_q2',
      bash_command=create_command,
      dag=dag
    )
    t1 >> t2


