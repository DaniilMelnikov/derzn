# Старт разработки

(*) - означает что можно упростить с помощью direnv. Подробнее в самом конце

## создать виртуальное окружение (*)

```bash
python: python -m venv env
```

## активировать вирт. окружение (*)
```bash
source env/bin/activate
```

## установить зависимости в вирт.окружение

```bash
pip install -r requirements.txt
```

## инициализировать тестовые переменные окружения (*)

Это придется делать каждый раз, аналогично активации вирт.окружения.

```bash
export SECRET_KEY=asdaaskdw9u2r4lfkjd32
export DEBUG=true
export ALLOWED_HOSTS='*'
export DB_URL=sqlite:///db.sqlite3
export BASE_URL=/
export EMAIL_HOST=localhost
export EMAIL_PORT=5822
export EMAIL_HOST_USER=admin
export EMAIL_HOST_PASSWORD=somepass
export EMAIL_USE_TLS=false
export EMAIL_USE_SSL=false
```


## инициализировать БД

```
./manage.py makemigration && ./manage.py migrate
```

## загрузить начальные данные

```
./manage.py loaddata dump.json
```


Файл dump.json спросить в чате или искать в закрепах.


## (*) [Direnv](https://direnv.net/)

TL;DR:
после установки `direnv` выполняем команду в каталоге проекта:
```bash
cat <<EOF > .envrc
layout python3
export SECRET_KEY=asdaaskdw9u2r4lfkjd32
export DEBUG=true
export ALLOWED_HOSTS='*'
export DB_URL=sqlite:///db.sqlite3
export BASE_URL=/
export EMAIL_HOST=localhost
export EMAIL_PORT=5822
export EMAIL_HOST_USER=admin
export EMAIL_HOST_PASSWORD=somepass
export EMAIL_USE_TLS=false
export EMAIL_USE_SSL=false
EOF
```

После этого разрашаем исполнение этого файла командой:
```
direnv allow .
```
Теперь можно поставить зависимости и все. Каджый раз когда вы зайдете в этот
каталог, будет активирован venv и установленны нужные переменные.

### развернутое пояснение
Данная утилита позволяет несколько упростить действия, требуемые для выполнения
на постоянной основе для конкретного проекта/каталога.

Идея проста - при заходе в каталог, `direnv` исполняет файл `./envrc`.

В Python мы используем virtual environment (venv) для разделения зависимостей
между проектами, потому при переключении между проектами, нужно деактивировать
старый venv и активировать текущий (для проекта).

Так же, в случае данного проекта, требуется инциализация многих переменных
(вы видели выше).

# Дополнительно

Для того, чтобы кодовая база была более однообразной, предлагается
использовать утилиты pre-commit с линтерами и форматтерами.
Установите `pre-commit`:
```bash
pip install pre-commit
pre-commit init
```
После этого, все измененные файлы перед коммитом будут проходить
проверку линтера `flake8` и форматирование утилитой `black`.
Как правило, это приводит к ошибке коммита, потому что `flake8` может сообщить
об ошибках в коде, а `black` выполнил переформатирование.
Потому, процесс коммита может выглядеть так:
```bash
git commit -m "fix issue"
git update && !!
```
`!!` это специальная команда `bash`: повтор предыдущей команды
(в этом случае - `git commit -m "fix issue"`).
Если же вы уверены, что все в порядке, flake8 ошибается, а `black`
форматирует неправильно, ~~страдайте во благо общества~~ можно воспользоваться
костылем:
```bash
git commit -nm "fix issue"
```
дополнительный параметр `-n` отменит все проверки. Это значит, что вы передаете
решение этих проблем другому.

В случае с `flake8` можно внести исключение конкретных ошибок в файл конфигурации
`.flake8`, но к этому стоит подходить с умом.
