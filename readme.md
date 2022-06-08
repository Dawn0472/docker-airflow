
## 簡介
- airflow+mysql+rabbitmq
- 利用docker-compose建構分散式環境
- 搭配lsyncd進行數據同步

## 目錄架構
- 依照文章所述架構目錄
- 如已架設lsyncd，serverB應會同步產生sample-dag.py，此為避免重複無再添加檔案
```
|- 單機
|    |- dags    # dags目錄
|    |- logs    # logs目錄
|    |- plugins # plugins目錄
|- 分散式
|    |- serverA # master
|    |	|- data 
|    |	|	|- airflow
|    |	|	|	|- dags
|    |	|	|	|	|- sample-dag.py
|    |	|	|	|- plugins
|    |	|	|- mysql
|    |	|- logs 
|    |	|- docker-compose.yml		
|    |- serverB # worker
|    |	|- data 
|    |	|	|- airflow
|    |	|	|	|- dags
|    |	|	|	|- plugins
|    |	|- logs 
|    |	|- docker-compose_worker.yml

```

## 依照文章所述建構airflow
- 單機版本：https://dawn0472.github.io/articles/2022/06/07/Airflow-with-docker-compose-airflow-mysql-rabbitmq-單機/
- 分散式版本：https://dawn0472.github.io/articles/2022/06/08/Airflow-with-docker-compose-airflow-mysql-rabbitmq-分散式環境/