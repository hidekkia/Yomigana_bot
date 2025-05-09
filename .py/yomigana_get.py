import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from openpyxl import load_workbook
from bs4 import BeautifulSoup
import time
import re

driver = webdriver.Chrome() # Cria interação entre o código e o site do Chrome
driver.get("https://www.clubdam.com/karaokesearch/") #Carregar site em que os dados serão coletados
time.sleep(3)

data_frame = pd.read_excel('D:yomigana_bot\Lista geral karaoke (HIDEKI).xlsx') #Carregar o arquivo Excel com os nomes dos cantores e músicas
arquivo_excel = 'D:yomigana_bot\yomigana_bot.xlsx' # Carregar o arquivo Excel que receberás os dados coletados
workbook = load_workbook(arquivo_excel)
song_line = 0 # Precisa colocar 2 a menos do valor original da linha, Primeira linhas da lista_geral_karaoke que serão coletados os nomes de cantor e música

planilha = workbook["Plan1"] # Selecionar a planilha que receberá os novos dados
line = 1 # Linha em que será passado os novos dados
column = 'A' # Coluna que será passado os novos dados
last_song_line = 0

driver = webdriver.Chrome() # Cria interação entre o código e o site do Chrome
driver.get("https://www.clubdam.com/karaokesearch/") #Carregar site em que os dados serão coletados
time.sleep(3)


while last_song_line < 500: # Loopin principal
    singer_name = data_frame.iloc[song_line, 1]
    music_name = data_frame.iloc[song_line, 22]

    if singer_name == 'final da lista': # Condicional para finalizar código no fim da lista (colocar "final_da_lista" na ultima linha da coluna de nomes
        workbook.save(arquivo_excel)
        break

    # Faz a pesquisa do nome do cantor e música
    search_box = driver.find_element(By.CLASS_NAME, "keyword")
    search_box.send_keys(singer_name, ' ', music_name)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)

    find_song = driver.find_element(By.CLASS_NAME, 'maybe-search')
    maybe_search = find_song.text
    if maybe_search != '見つかりませんでした。':
        song_name = driver.find_element(By.CLASS_NAME, "song-wrap")
        song_name.click()
        time.sleep(3)
        # Encontra a tag do Yomigana da música e pega o texto dela
        text_field = driver.find_element(By.CLASS_NAME, "song-yomi")
        song_name = text_field.text.replace(' ]', '').replace('[ ', '')
        # Coloca o texto armazenado no arquivo excel
        cell = planilha[column + str(line)]
        text = song_name
        cell.value = text
        workbook.save(arquivo_excel)
        song_line += 1
        line += 1
        last_song_line += 1

    else:
        time.sleep(2)
        search_box = driver.find_element(By.CLASS_NAME, 'keyword')
        search_box.clear()
        cell = planilha[column + str(line)]
        text = 'não tem'
        cell.value = text
        workbook.save(arquivo_excel)
        song_line += 1
        line += 1
        last_song_line += 1

# Salvar as alterações no arquivo Excel
workbook.save(arquivo_excel)
driver.quit()


