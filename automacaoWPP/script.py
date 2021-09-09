from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")


while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(1)

# já estamos com o login feito no whatsapp web
numero = "+5511999999999"
texto = "teste"
x = 1

while x < 20: 

    msg = str(texto)

    link = f"https://web.whatsapp.com/send?phone={numero}&text={msg}"

    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(2)
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]/button').click()
    time.sleep(2)

    x += 1 
