from airflow import DAG
import pendulum
from airflow.operators.bash import BashOperator
from airflow.models import Variable

with DAG(
    dag_id="dags_bash_with_variable",
    schedule="10 9 * * *",
    start_date=pendulum.datetime(2023, 4, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    var_value = Variable.get("sample_key")

    bash_var_1 = BashOperator(
    task_id="bash_var_1",
    bash_command=f"echo variable:{var_value}"
    )

    bash_var_2 = BashOperator(
    task_id="bash_var_2",
    bash_command="echo variable:{{var.value.sample_key}}"
    )#에어플로우는 2안을 권장합니다. 성능때문에
    #에어플로우가 주기적으로 댁을 파싱할때 스케줄러가 하는데 이때 내부적으로 실행을 함
    # 오타도 검사해주고..그래서 부하 원인이 되므로1안은 권장하지 않습니다
    # {{}}안에 있는 템플릿까지 검사하진 않습니다. 이건 런타임 실행시간에만 함 파싱할때는 안해줌 그래서 부하 적음
    #  