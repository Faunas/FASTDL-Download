import urllib.request
import os
import zipfile
import wget

# Основной функционал работает.
# Осталось написать код для следующего:
# Перенос файлов в папку с игрой, по пути указанному от пользователя.

print(
    'Путь до игры по дефолту: D:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\nЕсли твой путь от игры отличается даже на одну букву - введи его самостоятельно')
print('В случае, если путь соответствует тому, что ты увидел выше - в ответе напиши цифру "0"')
csgo_url = input('Введи путь до папки с CS GO: ')
if csgo_url == 0:
    csgo_url = 'D:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo'
file_url = 'https://my-files.su/Save/ogjicc/objects.zip'
print('Загрузка началась, время загрузки 30 минут. Не останавливайте процесс! Повторный запуск программы начинает скачивать файлы с начала!')
wget.download(file_url, csgo_url)
print('Загрузка завершена!')
print('Начинаём распаковку файлов, это может занять до 5 минут')
# Распаковка .zip в папку, для получения драйвера в .ехе виде
zip = zipfile.ZipFile(csgo_url + '\objects.zip') # Запаковывает файл в .zip формат
zip.extractall(csgo_url + '\objects.zip') # Распаковка файла
zip.close()
print('Распаковка завершена, все файлы успешно загружены!')