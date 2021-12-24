# getBuildFromAppcenter
Получение сборки из аппцентра по номеру версии

Зависимости:
pip3 install click
pip3 install json
pip3 install requests

Пример:
python3 appcenterDownloadBuild.py version token app_name owner_name save_path

version - версия билда
token - api токен
app_name - название приложения в appcenter
owner_name - владелец приложения в appcenter
save_path - путь, куда сохранять билд (без названия билда). Название формируется app_name + "_" + short_version + "." + version + "." + file_extension
