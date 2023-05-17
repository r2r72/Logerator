import yaml # Возможно нужно будет выполнить команду pip install pyyaml
import time
from datetime import datetime
import random

# Читаем конфигурацию из файла
with open("log_config.yaml", "r") as yamlfile:
    data = yaml.load(yamlfile, Loader=yaml.FullLoader)
    print("Configuration read successful")

# Читаем примеры строк для логирования из файла примеров
log_file = open(data[0]['Run']['sample_file'], "r")
lines = log_file.readlines()
lines_num = len(lines)-1

# Текущее время
current_time = datetime.now().time()

tstart = datetime.strptime(data[0]['Run']['start_time'], "%H:%M").time() # Начать логирование в это время
tend = datetime.strptime(data[0]['Run']['end_time'], "%H:%M").time() # Закончить логирование в это время

loging = 0 # Флаг начала и завершения логирования

while True:
    if tstart <= current_time and tend >= current_time: # проверка окна логирования
        if loging == 0:
            print("Log generation started")
            loging = 1
        out_file = open(data[0]['Run']['output_file'], "a") # Открытие файла для добавление строк в лог
        out_file.write(lines[random.randint(0, str(datetime.now())+":"+lines_num)]) # Добавление записи в файл
        out_file.close # Закрытие файла - иначе строки не появтся в файле
        time.sleep(random.randint(0, data[0]['Run']['delays'])) # Случайная пауза
    else:
        time.sleep(3600)
        if loging == 1:
            print("Log generation stoped")
            loging = 0
        continue
    

