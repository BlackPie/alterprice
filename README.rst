Alterprice
==========

Как развернуть
--------------

Что нужно сделать до развертки:

* Ставим питон;
* Ставим npm;
* Ставим `docker <https://docs.docker.com/>`_ (на линуксе) или `boot2docker <https://docs.docker.com/installation/mac/>`_.
  Все должно быть последних версий.


Далее клонируем репо и делаем::

    python bootstrap.py
    ./bin/buildout  # поставит локально вам всякие ништяки в ./bin (docker-compose, fab, etc)
    npm install  # поставит в ./bin еще ништяков (gulp, etc.)
    boot2docker up # только если вы на Mac
    ./bin/docker-compose build  # есть алиас этой команды ./bin/build
    ./bin/docker-compose up  # есть алиас этой команды ./bin/up
    ./bin/docker-compose run <WEB> ./bin/django migrate  # запустить миграции
    ./bin/docker-compose run <WEB> ./bin/django createsuperuser  # если нужно создать пользователя (админа)
    ./bin/docker-compose run <WEB> ./bin/django loaddata  # загрузить фикстуры (если есть)

<WEB> – заменить на имя контейнера из docker-compose.yml (скорее всего – web)

Обратите внимание на алиасы в папке .bin/, например ./bin/django