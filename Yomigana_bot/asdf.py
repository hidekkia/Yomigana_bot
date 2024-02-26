from selenium import webdriver
import time

driver = webdriver.Chrome() # Cria interação entre o código e o site do Chrome
driver.get("https://www.clubdam.com/karaokesearch/") #Carregar site em que os dados serão coletados
time.sleep(10)