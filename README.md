# django_bootstrap_table

> 安装django:`pip install Django`  
进入工程根目录执行:`python manage.py startapp django_bootstrap_table_web`来创建应用  
执行`python manage.py runserver 8080` 启动server  
查看django版本:`python -m django --version`  
安装mysql库支持`pip install mysqlclient`  
创建基础表:`python manage.py migrate`  
创建应用表结构:`python manage.py makemigrations django_bootstrap_table_web`  
执行生成表结构:`python manage.py migrate django_bootstrap_table_web`  
更新表结构:`python manage.py makemigrations`  
执行更新表:`python manage.py migrate`  
创建用户`python manage.py createsuperuser`  