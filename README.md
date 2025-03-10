# Django + Stripe API

## Описание ✏️
stripe.com - платёжная система с подробным API и бесплатным тестовым режимом для имитации и тестирования платежей. С помощью python библиотеки stripe можно удобно создавать платежные формы разных видов, сохранять данные клиента, и реализовывать прочие платежные функции. 

В данном проекте простой сервер с простеньким html, который общается со Stripe и создает платёжные формы для товаров. 


## Функционал 🛠
- GET /buy/{id}: c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса


- GET /item/{id}: c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)


## Технологии ⚙️
* *Python* 
* *Django*
* *PostgreSQL*
* *Docker*
* *Docker Compose*
* *Stripe*


## Запуск 🚀 
1. Клонировать проект на свою локальную машину:

    ```bash
    git clone https://github.com/Sura1096/app.git
    ```

    ```bash
    git clone git@github.com:Sura1096/app.git
    ```
   
2. В корне проекта создать для проекта виртуальное окружение:

    ```bash
    python3.12 -m venv venv
    ```

3. Активировать виртуальное окружение:

   ```bash
    source venv/bin/activate
    ```

4. Установить Docker, Docker Compose.


5. Собрать контейнер:

   ```bash
    docker compose build
    ```
   
6. Запустить контейнер:

   ```bash
    docker compose up
    ```

7. Применить миграции:

   ```bash
    docker compose run --rm web-app sh -c "python manage.py migrate"
    ```

8. Создать пользователя для админки:

   ```bash
    docker compose run --rm web-app sh -c "python manage.py createsuperuser"
    ```
