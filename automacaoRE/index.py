from selenium import webdriver
import time

navegador = webdriver.Chrome()

navegador.get("https://leomadeiras.routeasy.com.br/#!/dashboard")
time.sleep(3)

username = navegador.find_element_by_xpath('//*[@id="page-top"]/section/div/div/div/div/div[1]/form[1]/div[1]/input')
password = navegador.find_element_by_xpath('//*[@id="page-top"]/section/div/div/div/div/div[1]/form[1]/div[2]/input')
username.send_keys("bruno.marques@leomadeiras.com.br")
password.send_keys("Broyz@1998")
navegador.find_element_by_xpath('//*[@id="page-top"]/section/div/div/div/div/div[1]/form[1]/div[3]/button').click()
time.sleep(3)


qtde = 20
aux = 2

while aux < qtde:    
    navegador.get("https://leomadeiras.routeasy.com.br/#!/routings/list")
    time.sleep(3)
    navegador.find_element_by_xpath('/html/body/section/ui-view/div/div/div[' + str(aux) + ']').click()
    time.sleep(3)
    navegador.find_element_by_xpath('/html/body/section/ui-view/div/div/div[1]/div[1]/div/div[3]/span').click()
    time.sleep(3)
    navegador.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div/div/div[10]').click()
    time.sleep(3)
    navegador.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div/div/div[7]').click()
    time.sleep(3)
    navegador.find_element_by_css_selector('body > div.modal.fade.ng-isolate-scope.custom-options-modal-relatory.in > div > div > div > div.modal-header-options > a').click()
    time.sleep(5)
    aux += 1