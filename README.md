# Фото менеджер

Сервис разработан на django rest framework


## Установка и запуск

1. Склонировать репозиторий с Github:

````
git clone https://github.com/Timur-Razzakov/Photo_manager.git
````
2. Перейти в директорию проекта

3. Создать виртуальное окружение:

````
python -m venv venv
````

4. Активировать окружение:
````
source\venv\bin\activate
````
5. В файле .evn заполнить необходимые данные
 
6. Установка зависимостей:

```
pip install -r requirements.txt
```

7. Создать и применить миграции в базу данных:
```
python manage.py makemigrations
python manage.py migrate
```
8. Запустить сервер
```
python manage.py runserver 0.0.0.0:8000
```
***
### Запуск тестов
``` 
python manage.py test
```
***
# Установка проекта с помощью docker-compose


1. Склонировать репозиторий с Github
```
git clone https://github.com/Timur-Razzakov/Photo_manager.git
```
2. Перейти в директорию проекта


3. В файле .evn заполнить необходимые данные


4. Запустить контейнеры 
``` 
sudo docker-compose up -d
 ```
5. Остановка работы контейнеров 
```
sudo docker-compose stop
```
***
```http://127.0.0.1:8000/auth/users/``` - список пользователей и создание

```http://127.0.0.1:8000/auth/token/login``` - авторизация пользователей

```http://127.0.0.1:8000/image/create/``` - форма для создания новых данных


```http://0.0.0.0:8000/image/<pk>/``` - изображение с метаданных

```http://0.0.0.0:8000``` - изображения без метаданных

```http://0.0.0.0:8000/docs/``` - документация проекта

***

**Техзадание:** 

## Задача

<p>Необходимо разработать REST фото менеджер</p>

## Пункты для успешного принятия 
<ul>
<li>1. Загружать фотографии авторизованным пользователям.</li>
<li>2. При загрузке можно указывать различную метадату: гео локацию, описание, имена людей на фото.</li>
<li>3. Отображать список фотографий, без метаданных.</li>
<li>4. Фильтровать фотографии по дате.</li>
<li>5. Фильтровать фотографии по геолокации.</li>
<li>6. Фильтровать фотографии по имени человека (по имени создателя фотографий).</li>
<li>7. Получать фотографию по айди с метаданными.</li>
</ul>

<p>доп задача: сделать апи автодополнение по поиску возможных имен людей присутствующих на фотографиях. </p>

## Дополнительно добавил:

<ul>

[//]: # (<li> Тестирование написанного кода.</li>)
<li> Подготовил docker-compose для запуска всех сервисов проекта одной командой.</li>
<li> Сделал так, чтобы по адресу /docs/ открывалась страница со Swagger UI и в нём отображалось описание разработанного API.</li>

</ul>