import os
import shutil
i = 0
files = os.listdir()
while i < len(files):
	files = os.listdir()
	file = files[i]
	if file.endswith('.mp3') or file.endswith('.wav'):
		print("Переношу файл ",file," в папку Музыка.")
		original = file
		target = "Музыка/" + file
		print(target)
		os.replace(original,target)
	if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
		print("Переношу файл",file,"в папку Изображения.")
		original = file
		target = "Изображения/" + file
		print(target)
		os.replace(original,target)
	if file.endswith('.exe') or file.endswith('.msi'):
		print("Переношу файл",file,"в папку Программы.")
		original = file
		target = "Программы/" + file
		print(target)
		os.replace(original,target)
	if file.endswith('.zip') or file.endswith('.rar') or file.endswith('.7z'):
		print("Переношу файл",file,"в папку Архивы.")
		original = file
		target = "Архивы/" + file
		print(target)
		os.replace(original,target)
	if file.endswith('.txt'):
		print("Переношу файл",file,"в папку Текст.")
		original = file
		target = "Текст/" + file
		print(target)
		os.replace(original,target)
	if file.endswith('.torrent'):
		print("Переношу файл",file,"в папку Торренты.")
		original = file
		target = "Торренты/" + file
		print(target)
		os.replace(original,target)
	if file.endswith('.xcf'):
		print("Переношу файл",file,"в папку GIMP.")
		original = file
		target = "GIMP/" + file
		print(target)
		os.replace(original,target)
	if file.endswith('.mp4') or file.endswith('.webm'):
		print("Переношу файл",file,"в папку Видео.")
		original = file
		target = "Видео/" + file
		print(target)
		os.replace(original,target)
	i+=1