def get_sftp():
    print('sftp 작업을 시작합니다')
    

def regist(name, sex, *args):
    print(f'이름: {name}')
    print(f'성별: {sex}')
    print(f'기타옵션들: {args}')


def regist2(name, sex, *args, **kwargs):
    print(f'이름: {name}')
    print(f'성별: {sex}')
    print(f'기타옵션들: {args}')
    email = kwargs['email'] or 'empty'
    phone = kwargs['phone'] or 'empty'
    if email:
        print(email)
    if phone:
        print(phone)
    data_interval_start = kwargs.get('data_interval_start')
    data_interval_end = kwargs.get('data_intergal_end')
    print(data_interval_start, data_interval_end)

    
    #kwargs에서 key가 data_interval_start 와 data_interval_end 인 두 값을 꺼내어 출력할 수 있도록 아래 2개 실습을진행해보세요.
    #실습 1) plugins/common/common_func.py 의 regist2 함수를 수정하고 dags_python_with_op_kwargs 실행
