<h1>Проект API Yatube</h1>

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Tiro+Devanagari+Hindi&size=25&duration=2500&color=2F114D&height=60&lines=%D0%AD%D1%82%D0%BE+%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82+%D0%B4%D0%BB%D1%8F+%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%BA%D0%B8;API+%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0+Yatube.)](https://git.io/typing-svg)

<h2>Как запустить проект:</h2>

Клонировать репозиторий и перейти в него в командной строке:

<blockquote>git clone https://github.com/Ferdinand-I/api_final_yatube.git<br>
cd api_final_yatube</blockquote>

Cоздать и активировать виртуальное окружение:

<blockquote>python -m venv venv<br>
source venv/Scripts/activate<br>
</blockquote>

Установить зависимости из файла requirements.txt:

<blockquote>
python -m pip install --upgrade pip<br>
pip install -r requirements.txt
</blockquote>

Выполнить миграции:

<blockquote>
python manage.py migrate
</blockquote>

Запустить проект:

<blockquote>
python manage.py runserver
</blockquote>
