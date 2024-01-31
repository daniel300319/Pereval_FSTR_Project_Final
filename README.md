### Детализация задачи:


Это учебный проект для виртуальной стажировки курса SkillFactory.

Федерация Спортивного Туризма России (ФСТР) ведёт базу горных перевалов, которая пополняется туристами. Для отправки туристами данных в ФСТР разрабатывается мобильное приложение для Android и IOS Планируется, что в горах туристы будут вносить данные о перевале в приложение и отправлять их в ФСТР, как только появится доступ в Интернет. Модератор из федерации будет верифицировать и вносить в базу данных информацию, полученную от пользователей, а те в свою очередь смогут увидеть в мобильном приложении статус модерации и просматривать базу с объектами, внесёнными другими.

В данном проекте разрабатывается REST API, которое будет обслуживать это мобильное приложение.

Работа разбита на 3 этапа:

1.Создание базы данных (СУБД - PostgreSQL), разработка классов по работе с БД и одного метода submitData для REST API.

2.Разработка ещё трёх методов для Rest API;

3.Создание документации и проверка кода тестами.

### Решение и документация по работе с API:

База данных создана и настроена, СУБД - Postresql

Бэк реализован на Django

Модели сущности БД реализованы через Django ORM

Разработан класс, который реализует REST API, используя Django REST Framework. 
В этом API доступны различные методы, они описаны ниже.

Метод PATCH изменен конкретно под нашу задачу

Для фильтрации перевалов по email пользователя использовались django-filters

### Доступные методы REST API :


| Эндпоинты |Маршруты                        | Описание                                                 |
|-----|--------------------------------|----------------------------------------------------------|
| GET | submitData/                    | Вывод списка перевалов                                   |
| POST | submitData/                    | Добавление нового перевала                               |
| GET | submitData/{id}/               | Детализация по определенному перевалу                    |
| PATCH| submitData/{id}/               | Редактирование существующего перевала                    |
| GET | submitData/?user__email={email} | Получение списка перевалов от определенного пользователя |

#### Зависимости

- Django==5.0.1
- django-filter==23.5
- djangorestframework==3.14.0
- psycopg2==2.9.9
- python-dotenv==1.0.1
