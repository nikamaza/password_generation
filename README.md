# Ocean of Keys

## :pushpin: **Описание проекта**

Приложение для генерации случайных паролей с графическим интерфейсом, разработанное с использованием PyQt5. Приложение позволяет:

* Сохранять самому придуманный пароль
* Генерировать случайные пароли
* Сохранять пароли с названием социальной сети в файл `passwords.txt`
* Использовать простой и удобный интерфейс с фоновым изображением

## :dart: **Цель проекта**

Создать приложение для генерации случайных паролей с возможностью их сохранения и добавления названия социальной сети.

## :hammer_and_wrench: **Используемые технологии**

:snake: Python 3

:desktop_computer: PyQt5

:desktop_computer: QPixmap (для фонового изображения)

:1234: Random (для генерации паролей)

:file_folder: **Файлы проекта**

- `code.py` — основной файл приложения
- `win.ui` — файл пользовательского интерфейса (Qt Designer)
- `fon.jpg` — фоновое изображение
- `passwords.txt` — файл для хранения паролей (создается автоматически при сохранении первого пароля)

## :arrow_forward: **Запуск проекта**

1. Установите зависимости:

   ```
   pip install PyQt5
   ```
2. Запустите приложение:
   ```
   python code.py
   ```
## :bar_chart: Функционал

* Генерация случайного пароля длиной 16 символов

* Проверка длины пароля перед сохранением (минимум 4 символа)

* Сохранение пароля с названием социальной сети пользователя в файл passwords.txt

* Графический интерфейс с фоновым изображением

## :robot: Как использовать

1. Нажмите "Сгенерировать" для создания случайного пароля.

2. Введите социальную сеть и нажмите "Сохранить" для сохранения пароля в файл passwords.txt.

3. Файл паролей будет храниться в той же папке, что и приложение.
