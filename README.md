### Запуск Linux:
Создать вирт окружение: ```python3 -m venv env```  
Активировать вирт окружение: ```source env/bin/activate```  
Установить зависимости: ```pip install -r requirements.txt```  
Создать миграции: ```python3 manage.py makemigrations```  
Применить миграции: ```python3 manage.py migrate```  
  
### Эндпоинты:  
  
GET ```localhost:8000/api/v1/all``` - получить все товары  
GET ```localhost:8000/api/v1/<int:id>``` - получить товар по id  
POST ```localhost:8000/api/v1/add``` - добавить товар  
  
### Фильтрация/поиск товара  
Статусы вводить с пробелом, можно фильтровать по 3-м параметрам сразу  
GET ```localhost:8000/api/v1/all?name=товар_1&vendor_code=111222&status=in stock```  
  
Доступные статусы(status=):  
```in stock```  
```on order```  
```receipt expected```  
```not available```  
```not produced```  
  
### Пример добавления товара через Postman:
![Иллюстрация к проекту](https://github.com/georg220022/django_shops/blob/main/2022-12-12_17-08.png)
