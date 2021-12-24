# getBuildFromAppcenter
Получение сборки из аппцентра по номеру версии

## Зависимости:
`pip3 install click`</br>
`pip3 install json`</br>
`pip3 install requests`</br>

## Пример:
`python3 appcenterDownloadBuild.py version token app_name owner_name save_path`

version - версия билда</br>
token - api токен</br>
app_name - название приложения в appcenter</br>
owner_name - владелец приложения в appcenter</br>
save_path - путь, куда сохранять билд (без названия билда). Название формируется app_name + "_" + short_version + "." + version + "." + file_extension
