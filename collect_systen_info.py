import getpass
import os
import socket
from datetime import datetime
from uuid import getnode as get_mac
# import pyautogui
from speedtest import Speedtest
# import telebot
import psutil
import platform
# from PIL import Image

name = getpass.getuser() # Имя пользователя
ip = socket.gethostbyname(socket.getfqdn()) # IР-адрес системы
mac = get_mac() # МАС-адрес
ost = platform.uname() # Название операционной системы

inet = Speedtest()
download = float(str(inet.download()) [0:2] +"."#Входящая скорость
+ str(round(inet.download(), 2)) [1]) * 0.125
uploads = float(str(inet.upload()) [0:2] + "." #Исходящая скорость
+ str(round(inet.download(), 2)) [1]) * 0.125

zone = psutil.boot_time() #Узнает время, заданное на компьютере
time = datetime.fromtimestamp(zone) # Переводит данные в читаемый вид
cpu = psutil.cpu_freq()

print(name, ip, mac, ost)
print(download, uploads)
print(zone, time, cpu)