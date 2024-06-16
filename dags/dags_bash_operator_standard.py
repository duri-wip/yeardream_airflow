from airflow import DAG
import pendulum

import datetime

from airflow.operators.bash import BashOperator

### 스케줄: 매주 월요일, 금요일 09:00 - start_date: 2024-06-01 - tag: homework

my_dag = DAG(
     dag_id="dags_bash_operator_standard",
     start_date=datetime.datetime(2024, 6, 1),
     tag = "homework",
     schedule="0 9 * * 1,5"
)

bash_t1 = BashOperator(task_id="bash_task1",
            bash_command="echo whoami",
            dag=my_dag)

bash_t2 = BashOperator(task_id="bash_task2",
              bash_command="echo $HOSTNAME",
              dag=my_dag)

bash_task1 >> bash_task2