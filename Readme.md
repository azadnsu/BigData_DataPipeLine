# Install python
Import all dependencies
Setup PostgreSQL > Create a DB named: WeatherDB
Install airflow

Start airflow
airflow webserver -p 8080

airflow scheduler

Open http://0.0.0.0:8080/admin/

Test task: airflow test weatherDag get_weather 2019-05-26
airflow backfill weatherDag -s 2019-05-26 -e 2019-05-27

airflow clear <dag_id>


