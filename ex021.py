# Faça um programa em Python que abra e reproduza o aúdio de um arquivo MP3

from playsound import playsound

print('\n      ====== DESAFIO 21 ======     ')

file_path = "manda-foto-na-moral.mp3"
print(f'\nExecutando : {file_path}')
playsound(file_path)

