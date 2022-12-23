# Космический Телеграм
**Позволяет**:
-  Скачивать фотографии запусков spacex а так же астрономические фотографии NASA - Фотографию дня (APOD) и полихроматические изображения Земли (EPIC).
-  Загружать в автоматическом режиме данные фотографии в ТГ канал.

## Скачать фото запуска SpaceX
запустить файл `fetch_spacex_images.py` с аргументами  `-dir` <директория куда будут сохраняться файлы> `-id=` идентификационный номер запуска, если не указан будет скачаны фотографии с [последнего запуска](https://api.spacexdata.com/v5/launches/latest) ( если такие есть)\
__пример запуска__
```
python3 fetch_spacex_images.py -id=5eb87d47ffd86e000604b38a -dir=spacex
```

## Скачать EPIC-фото от NASA
запустить файл `fetch_nasa_epic_pictures.py` с аргументами  `-dir` <директория куда будут сохраняться файлы> по умолчанию - "nasa_epic_pictures"\
__пример запуска__
```
python3 fetch_nasa_epic_pictures.py  -dir=nasa_epic
```

## Скачать APOD-фото от NASA
запустить файл `fetch_nasa_apod_images.py` с аргументами  `-dir` <директория куда будут сохраняться файлы> `-noi=` <Количество фотографии для скачивания> по умолчанию = 1\
__пример запуска__
```
python3 fetch_nasa_apod_images.py  -dir=nasa_epic -noi=4
```

## Опубликовать фотографию на канал
**Загрузить одну фотографию в канал**.\
запустить файл `telegramAPI.py` с аргументами  `--img_path` <путь до фотографии>.\
__пример запуска__
```
python3 telegramAPI.py  --img_path="spacex_pictures/50291453997_aa715950e7_o.jpg"
```

**Запустить автоматическую загрузку фотографий**.\
запустить файл `upload_pictures_in_channel.py`
скрипт будет с паузой равной указанной в переменной окружения`PAUSE` загружать случайную фотографию из находящихся в директории.\
__пример запуска__
```
python3 upload_pictures_in_channel.py
```

## Что понадобится

токен от API NASA [ссылка на регистрацию](https://api.nasa.gov/)
токен от Telegram бота [ссылка на регистрацию если бота еще нет](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html)
`username` телеграмм канала [как создать канал](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/)
### Куда положить конфигурационные данные?
поместите необходимые данные в файл `.env` или создайте соответствующие переменные окружения
пример структуры `.env` файла
```
NASA_API =
TELEGRAM_BOT_TOKEN =
PAUSE =
CH_USERNAME =
```
где:
- `NASA_API` токен от API NASA
- `TELEGRAM_BOT_TOKEN ` - токен телеграмм бота
-  `PAUSE ` - размер паузы в отправке, указанная в секундах
-  `CH_USERNAME ` - уникальное имя канала указанное при регистрации
## Как установить
Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
