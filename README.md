# Проект API Yatube <img src="https://cdn.mypanel.link/fv2dwk/tlrqq5seo8xf7c91.png" width=48>

Реализация API для для сервиса *Yatube*

Данный проект реализован на связке **Django + Django REST Framework** и предоставляет открытые **API** методы для работы с сервисом.

Детали реализации:
* JWT авторизация, организованныя с помощью приложения **djoser** и встроенного пакеты *rest_framework_simplejwt.authentication*
* Описание моделей БД и описание поведения сериализаторов данных на основе этих моделей (**DRF**)
* Роут запросов с помощью объекта **DefaultRouter** модуля *rest_framework.routers*
* Описание пермишенов

Чтобы запустить проект локально:

1. Клонируйте репозиторий себе на компьютер, находясь в директории, откуда вы хотите в будущем запускать проект (в примере испоьзуется ссылка для подключения с помощью протокола **SSH** в консоли **BASH** для **WINDOWS**)

```BASH
git clone git@github.com:Ferdinand-I/api_final_yatube_django_rest.git
```

2. Создайте и активируйте виртуальное окружение (в примере используется утилита **venv**), перейдите в директорию проекта

```BASH
python -m venv venv
source venv/Scripts/activate
cd api_final_yatube_django_rest
```

3. Обновите **PIP** и установите зависимости **requirements.txt**

```BASH
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Перейдите в корневую директорию джанго проекта и сделайте миграции

```BASH
cd yatube_api
python manage.py migrate
```

5. Загрузите тестовые данные в БД

```BASH
python manage.py loaddata dump.json
```

6. Для доступа к админке сайта создайте суперпользователя

```BASH
python manage.py createsuperuser
```

7. Запустите проект на локальном сервере разработчика

```BASH
python manage.py runserver
```

Корень API приложения будет доступен по <a href="http://127.0.0.1:8000/api/v1/">этому</a> адресу

Админка будет доступна <a href="http://127.0.0.1:8000/admin/">здесь</a>

<a href="http://127.0.0.1:8000/redoc/">Документация</a> с описанием доступных методов
