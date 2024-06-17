from airflow import DAG
import pendulum
import datetime
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.decorators import dag

#매월둘째주금요일13:00
@dag(start_date=datetime.datetime(2024, 5, 1), 
     tags = ["homework"],
     schedule="0 13 * * 5#2")

def dags_bash_operator_decorator():
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami"
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME"
    )

    bash_t1 >> bash_t2

dags_bash_operator_decorator()