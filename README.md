# API для Yatube
Сервис API для проекта YaTube

Использованные технологии: Python3, 
Django, 
Django Rest Framework

## Установка

Клонируйте репозиторий и откройте в IDE среде
```sh
https://github.com/VankoID/api_final_yatube
```
Создайте виртуальное окружение:
```sh
python3 -m venv env
```
Активируйте виртуальное окружение:
```sh
source venv/bin/activate
```
Установите зависимости:
```sh
pip install -r requirements.txt
```
Выполните миграции:
```sh
python3 manage.py migrate
```
Запустите проект:
```sh
python3 manage.py runserver
```
## Примеры запросов и ответов API

Запрос всех постов
```sh
http://127.0.0.1:8000/api/v1/posts/
```
Ответ

```sh
[
    {
        "id": 1,
        "author": "User_second",
        "text": "Тестовый пост_1",
        "pub_date": "2022-06-01T09:17:40.064893Z",
        "image": null,
        "group": null
    },
    {
        "id": 2,
        "author": "User_second",
        "text": "Тестовый пост_2",
        "pub_date": "2022-06-01T09:17:53.643188Z",
        "image": null,
        "group": null
    }
]
```

Запрос второго поста
```sh
http://127.0.0.1:8000/api/v1/posts/2/
```
Ответ

```sh
{
    "id": 2,
    "author": "User_second",
    "text": "Тестовый пост_2",
    "pub_date": "2022-06-01T09:17:53.643188Z",
    "image": null,
    "group": null
}
```
Запрос первого комментария к первому посту
```sh
http://127.0.0.1:8000/api/v1/posts/1/comments/1
```
Ответ
```sh
{
    "id": 1,
    "author": "User_second",
    "text": "Тестовый комментарий к посту",
    "created": "2022-06-01T09:22:41.163606Z",
    "post": 1
}
```
Запрос неаутентифицированного пользователя
```sh
http://127.0.0.1:8000/api/v1/follow/
```

Ответ
```sh
{
    "detail": "Authentication credentials were not provided."
}
```
